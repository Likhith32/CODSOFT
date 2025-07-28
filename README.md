✅ Goal:
Nuvvu app lo use chestunna jntu_quiz.db lo existing users, exams, questions, results ni PostgreSQL loki shift cheyyali. So data safe untundi, and malli .db file kavalsina avasaram ledu.

🪜 STEP-BY-STEP:
🥇 STEP 1: SQLite Dump File Create Cheyyadam
Terminal open chey and:

bash
Copy
Edit
# If sqlite3 not installed:
sudo apt install sqlite3

# Go to your project folder (where instance/jntu_quiz.db exists)
cd your_project_directory

# Create SQL dump of your data:
sqlite3 instance/jntu_quiz.db .dump > backup_jntu_data.sql
🧼 STEP 2: Clean the Dump File (optional)
Open backup_jntu_data.sql with Notepad or VS Code and remove lines like:

sql
Copy
Edit
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
COMMIT;
This is optional but recommended for smooth PostgreSQL compatibility.

🥈 STEP 3: Upload dump to PostgreSQL
If you are using Render, go to Dashboard > PostgreSQL > Connect and get your DATABASE_URL (like postgresql://...)

Now use:

bash
Copy
Edit
# Terminal command to load data:
psql "your_postgres_url" < backup_jntu_data.sql
⚠️ If psql not installed:

bash
Copy
Edit
sudo apt install postgresql-client
💻 Alternate: Use GUI Tool
If you prefer GUI:

Open pgAdmin or DBeaver

Connect to your PostgreSQL DB

Run the backup_jntu_data.sql using SQL query window

✅ STEP 4: Update Your App
Update your config.py like this:

python
Copy
Edit
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://your_user:your_pass@host:port/dbname"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
🧹 STEP 5: Delete old SQLite references
You can delete:

instance/jntu_quiz.db

app.py lo sqlite:///... references

✅ RESULT:
App now uses PostgreSQL fully

Old exam & user data intact

SQLite .db file unnecessary

❓ Need Automation?
If you say Yes, I’ll give a Python script that:

Connects to jntu_quiz.db

Fetches data using SQLAlchemy

Inserts into PostgreSQL models

Ready to proceed?

Type: Yes, write Python migration script — for automatic migration

Or ask anything else 💡









Ask ChatGPT
