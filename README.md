# 🗺️ UniRoute - Global Education Navigator

An interactive web application designed to democratize access to global higher education. **UniRoute** serves as a direct gateway linking students to verified, free, or highly affordable online educational pathways, certificates, and accredited university degrees worldwide.

📊 **Live Deployment:** [uniroute.onrender.com](https://uniroute.onrender.com)

## 🎯 Core Engineering & Features
* **Dynamic Search & Filtering Ecosystem:** Instantly queries across multi-category educational assets including Free Courses, Diplomas, Certificates, Degrees, and MBAs.
* **Relational Data Mapping:** Powered by a clean relational SQLite schema (`schema.sql` & `uniroute.db`) mapping out structural education costs, institutional providers, and access pathways.
* **Lightweight Mobile Deployments:** Engineered entirely from a mobile terminal environment for seamless deployment to production infrastructure via a streamlined setup.

## 🛠️ Mobile Workstation & Tech Stack
This entire application was developed, local-hosted, and pushed to production using a smartphone:
* **Backend Framework:** Python (Flask Engine)
* **Database Management:** SQLite3
* **Production Configurations:** Gunicorn / WSGI (via `Procfile`)
* **Development Workstation:** Termux App / Pydroid 3 (Android terminal)
* **Cloud Infrastructure:** Render Cloud Platform

## 📦 Architecture & Directory Mapping
* `app.py` - Core Flask routing engine handling dynamic search and category sorting queries.
* `init_db.py` - Database instantiation pipeline.
* `schema.sql` / `uniroute.db` - Relational tables tracking verified institutional course metrics.
* `templates/` - Rendered frontend views optimized for cross-device mobile execution.

## 🚀 How to Spin It Up in Termux

To run this education index server locally on your smartphone terminal:

```bash
# 1. Clone this repository
git clone https://github.com/ezrawanyama74-commits/UniRoute.git

# 2. Enter the workspace directory
cd UniRoute

# 3. Initialize the SQL Database
python init_db.py

# 4. Fire up the local Flask server
python app.py
```

---
*Developed line-by-line as part of The Smartphone Scientist initiative — Nakuru, Kenya.*
