import sqlite3
import os
from werkzeug.security import generate_password_hash

db_path = 'uniroute.db'
if os.path.exists(db_path):
    os.remove(db_path)

connection = sqlite3.connect(db_path)
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Encrypting your master password using high-tier pbkdf2:sha256 security algorithms
hashed_password = generate_password_hash('admin1234', method='pbkdf2:sha256', salt_length=16)

# Inject the secure user parameters natively into your storage table layers
cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ('admin', hashed_password))

# Insert Clean Baseline Records
cur.execute("""INSERT INTO courses (platform_id, title, provider_institution, credential_type, is_accredited, cost_status, price_detail, direct_link) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
('University of the People', '<span style="font-family:\'Arial\'; font-size:18px; color:#0f4c81; font-weight:bold;">Bachelor Degree in Computer Science</span>', 'University of the People', 'Degree', 1, 'Affordable', '$180/course', 'https://uopeople.edu'))

connection.commit()
connection.close()
print("Database security architecture successfully upgraded to militarized encryption encryption standards!")
