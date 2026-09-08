"""Quick script to add waseem user to the database."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app import db
from app.security import ensure_user_table, hash_password

# Create/update user table
ensure_user_table()

# Add waseem user with password iba@123waseem (12+ characters)
username = "waseem"
email = "waseem@bbq.com"
password = "iba@123waseem"  # Extended to meet 12+ character requirement
name = "Waseem Hassan"
role = "Manager"
title = "Restaurant Manager"

try:
    db.execute_write(
        """INSERT INTO app_users (id, username, email, password_hash, name, role, title, status)
           VALUES (lower(hex(randomblob(16))), ?, ?, ?, ?, ?, ?, 'Active')
           ON CONFLICT(username) DO UPDATE SET email=excluded.email, password_hash=excluded.password_hash,
             name=excluded.name, role=excluded.role, title=excluded.title, status='Active'""",
        (username.lower(), email.lower(), hash_password(password), name, role, title),
    )
    print(f"✅ User '{username}' created successfully!")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"\nYou can now login with these credentials on the dashboard.")
except Exception as e:
    print(f"❌ Error creating user: {e}")
    sys.exit(1)
