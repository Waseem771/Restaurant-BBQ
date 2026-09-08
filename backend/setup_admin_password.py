"""Create admin user with custom password."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app import db
from app.security import ensure_user_table, hash_password

# Ensure table exists
ensure_user_table()

# Create admin user with custom password
username = "admin"
email = "admin@bbq.com"
# Password extended to meet 12+ character requirement
password = "iba@12345admin"  # 14 characters - meets requirement
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
    print("✓ Password meets the 12+ character requirement")
    print("✓ You can now login to the dashboard")
    print("")
    print("To login:")
    print("1. Run: start-servers.bat")
    print("2. Open: http://localhost:3000")
    print(f"3. Enter username: {username}")
    print(f"4. Enter password: {password}")
    print("5. Click Sign In")

except Exception as e:
    print(f"❌ Error creating admin user: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
