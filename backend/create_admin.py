"""Direct database script to create admin user with proper password."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app import db
from app.security import ensure_user_table, hash_password

# Ensure table exists
ensure_user_table()

# Create admin user with valid password
username = "admin"
email = "admin@bbq.com"
password = "iba@123admin"  # 12 characters - meets requirement
name = "Administrator"
role = "Administrator"
title = "System Administrator"

try:
    # Delete existing admin if it exists
    db.execute_write("DELETE FROM app_users WHERE username = ?", (username.lower(),))

    # Insert new admin user
    db.execute_write(
        """INSERT INTO app_users (id, username, email, password_hash, name, role, title, status)
           VALUES (lower(hex(randomblob(16))), ?, ?, ?, ?, ?, ?, 'Active')""",
        (username.lower(), email.lower(), hash_password(password), name, role, title),
    )

    print("✅ Admin user created successfully!")
    print("")
    print("Login Credentials:")
    print("=" * 50)
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email:    {email}")
    print("=" * 50)
    print("")
    print("The password meets the 12+ character requirement.")
    print("You can now login to the dashboard with these credentials.")

except Exception as e:
    print(f"❌ Error creating admin user: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
