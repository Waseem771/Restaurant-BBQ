# 🔐 ADD WASEEM USER - QUICK GUIDE

**Status**: ✅ User creation script ready

---

## 📋 USER CREDENTIALS

| Field | Value |
|-------|-------|
| **Username** | waseem |
| **Email** | waseem@bbq.com |
| **Password** | iba@123waseem |
| **Role** | Manager |
| **Name** | Waseem Hassan |
| **Title** | Restaurant Manager |

---

## 🚀 HOW TO ADD THE USER

### Option 1: Automatic (Windows - Easiest)
```bash
# Double-click this file from the project root:
add_user_waseem.bat
```

This will:
1. Activate the Python environment
2. Create the user in the database
3. Show confirmation message
4. Display login credentials

### Option 2: Manual (All Platforms)
```bash
cd backend

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate.bat  # Windows

# Run the user creation script
python add_waseem_user.py
```

### Option 3: Command Line
```bash
cd backend
.venv\Scripts\python.exe add_waseem_user.py
```

---

## ✅ AFTER ADDING THE USER

### 1. Start the Dashboard
```bash
start-servers.bat
```

### 2. Login with New Credentials
- **URL**: http://localhost:3000
- **Username**: waseem
- **Password**: iba@123waseem

### 3. Dashboard Opens
- Full access as Manager
- All features available
- All data visible

---

## 📝 PASSWORD DETAILS

**Why the extended password?**
- Dashboard requires passwords with at least 12 characters
- "iba@123" (7 chars) is too short
- "iba@123waseem" (13 chars) meets requirements

**Security Note:**
- This is for development/testing
- Change password before production
- Use stronger passwords in production

---

## 🔑 LOGIN FLOW

### Before User Creation
1. Open http://localhost:3000
2. Click "Try Demo" → Demo access only

### After User Creation
1. Open http://localhost:3000
2. Enter username: `waseem`
3. Enter password: `iba@123waseem`
4. Click "Sign In"
5. Full access to dashboard

---

## ✨ USER DETAILS

### Profile Information
```
Username:    waseem
Email:       waseem@bbq.com
Name:        Waseem Hassan
Role:        Manager
Title:       Restaurant Manager
Status:      Active
```

### Permissions
- ✅ View all dashboards
- ✅ Access analytics
- ✅ View products
- ✅ See anomalies
- ✅ Use AI chat
- ✅ Configure settings

---

## 🛠️ TROUBLESHOOTING

### User Already Exists?
The script uses `ON CONFLICT` - if the user exists, it will be updated with new credentials.

### User Not Found After Adding?
1. Restart the backend server
2. Clear browser cache (Ctrl+Shift+R)
3. Try logging in again

### Password Not Working?
1. Ensure password is exactly: `iba@123waseem`
2. Check CAPS LOCK is off
3. Clear browser storage: DevTools → Application → Clear Storage

### Database Error?
1. Check `data/bbq.db` exists
2. Verify backend is not running when adding user
3. Run script from `backend/` directory

---

## 📊 USER MANAGEMENT

### View All Users
```bash
cd backend
sqlite3 data/bbq.db "SELECT username, email, role, status FROM app_users;"
```

### Delete User (if needed)
```bash
cd backend
sqlite3 data/bbq.db "DELETE FROM app_users WHERE username='waseem';"
```

### Change Password
Use the create_user script to update:
```bash
cd backend
python scripts/create_user.py --username waseem --email waseem@bbq.com
# Then enter new password when prompted
```

---

## ✅ VERIFICATION

After adding the user, verify with:

```bash
# Check user in database
cd backend
sqlite3 data/bbq.db "SELECT username, email, role FROM app_users WHERE username='waseem';"

# Should show:
# waseem|waseem@bbq.com|Manager
```

---

## 🎯 QUICK START AFTER USER CREATION

1. **Run the Dashboard**
   ```bash
   start-servers.bat
   ```

2. **Login**
   - Username: `waseem`
   - Password: `iba@123waseem`

3. **Access Dashboard**
   - Overview with KPIs
   - Analytics and charts
   - Product performance
   - Anomaly alerts
   - AI chat

---

## 📝 FILES CREATED

- `add_user_waseem.bat` - Automatic user creation script (Windows)
- `add_waseem_user.py` - Python script to create the user
- `ADD_USER_WASEEM.md` - This guide

---

## ✨ SUMMARY

✅ User script created
✅ Batch file ready
✅ Instructions provided
✅ Ready to add user to dashboard

### Next Steps:
1. Run `add_user_waseem.bat`
2. Start `start-servers.bat`
3. Login with waseem / iba@123waseem
4. Enjoy the dashboard!

---

**Username**: waseem
**Password**: iba@123waseem
**Status**: Ready to add ✅

