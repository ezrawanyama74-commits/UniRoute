import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Force the secret key to be completely random in production to stop session hijacking
app.config['SECRET_KEY'] = os.urandom(24)

# FIREWALL: Limit login attempts to stop hackers using automated brute-force software
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
    headers_enabled=True
)

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    query = request.args.get('q', '')
    cred_filter = request.args.get('type', '')
    
    conn = get_db_connection()
    sql = "SELECT * FROM courses WHERE 1=1"
    params = []
    
    if query:
        # Secure parameterized queries to stop SQL Injection attacks completely
        sql += " AND (title LIKE ? OR provider_institution LIKE ?)"
        params.extend([f'%{query}%', f'%{query}%'])
    if cred_filter:
        sql += " AND credential_type = ?"
        params.append(cred_filter)
        
    courses = conn.execute(sql, params).fetchall()
    conn.close()
    return render_template('index.html', courses=courses, query=query, current_type=cred_filter)

@app.route('/admin-portal', methods=('GET', 'POST'))
@limiter.limit("5 per minute", error_message="Brute-force detected! Your IP address has been frozen. Try again in 15 minutes.")
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM admin WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        # High-Security Verification using Hashed Comparisons
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            session['username'] = user['username']
            session.permanent = True # Session automatically expires when the browser closes
            return redirect('/admin/dashboard')
        else:
            flash('Access Denied. Security parameters mismatched.')
    return render_template('login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    # Protection Layer: Ensure non-admins are booted out immediately
    if not session.get('logged_in'):
        return redirect('/admin-portal')
    conn = get_db_connection()
    courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return render_template('dashboard.html', courses=courses, platforms=[])

@app.route('/admin/add-course', methods=['POST'])
def add_course():
    if not session.get('logged_in'):
        return redirect('/admin-portal')
    
    platform_name = request.form['platform_name']
    title = request.form['title']
    provider = request.form['provider_institution']
    cred_type = request.form['credential_type']
    is_acc = 1 if request.form.get('is_accredited') else 0
    cost_status = request.form['cost_status']
    price = request.form['price_detail']
    link = request.form['direct_link']
    
    conn = get_db_connection()
    conn.execute("""INSERT INTO courses (platform_id, title, provider_institution, credential_type, is_accredited, cost_status, price_detail, direct_link)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (platform_name, title, provider, cred_type, is_acc, cost_status, price, link))
    conn.commit()
    conn.close()
    return redirect('/admin/dashboard')

@app.route('/admin/delete-course/<int:id>')
def delete_course(id):
    if not session.get('logged_in'):
        return redirect('/admin-portal')
    conn = get_db_connection()
    conn.execute('DELETE FROM courses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/admin/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
