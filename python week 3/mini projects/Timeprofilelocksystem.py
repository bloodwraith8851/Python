# This system allow a user to create and edit a profile (name,age,address,phone number)
#  for a limited time.
#  after that it automatically 
#  locks the profile (converted to tuples) and disallows further changes.

import time 
import threading
import threading
import getpass
import json
import os
import hashlib
import random
import string
import csv
from cryptography.fernet import Fernet
from colorama import init, Fore, Style
init(autoreset=True)

ASCII_BANNER = """
  _____       _ _     _           _   _           _     _             
 |  __ \     (_) |   | |         | | | |         | |   (_)            
 | |__) |__ _ _| | __| | ___ _ __| |_| |__   ___ | |__  _ _ __   __ _ 
 |  _  // _` | | |/ _` |/ _ \ '__| __| '_ \ / _ \| '_ \| | '_ \ / _` |
 | | \ \ (_| | | | (_| |  __/ |  | |_| | | | (_) | |_) | | | | | (_| |
 |_|  \_\__,_|_|_|\__,_|\___|_|   \__|_| |_|\___/|_.__/|_|_| |_|\__, |
                                                                __/ |
                                                               |___/ 
"""

HELP_TEXT = """
Advanced Profile Management System - Help

- Register: Create a new user account.
- Login: Access your profile and features.
- Admin: Special user with privileges to manage all users.
- 2FA: Two-Factor Authentication for extra security.
- Export/Import: Save/load users to/from files (encrypted JSON, CSV).
- Backup: Create/restore encrypted backups.
- Timer: You have limited time to edit your profile before it locks.
- All sensitive data is encrypted for your safety.
- For more info, see the README or contact the developer.
"""

"""
 Function to display countdown in background thread
"""

def countdown_timer(seconds, lock_event):
    while seconds > 0 and not lock_event.is_set():
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\rTime left to edit profile: {timer}", end='')
        time.sleep(1)
        seconds -= 1
    lock_event.set()
    print("\nTime limit exceeded. Profile locked.")

"""
profile system
"""
class profilesystem:
    def __init__(self):
        self.profile = {
            "name": "",
            "age": "",
            "address": "",
            "phone_number": ""
        }
        self.is_locked = False
        self.lock_event = None
        self.lock = threading.Lock()
        self._password = None
    
    def hash_password(self, pwd):
        return hashlib.sha256(pwd.encode()).hexdigest()

    def _check_locked(self):
        if self.is_locked or (self.lock_event and self.lock_event.is_set()):
            print("\n[!] Profile is locked. No further actions are allowed.")
            return True
        return False

    def set_password(self):
        while True:
            if self._check_locked():
                return
            pwd = getpass.getpass("Set a password for your profile: ")
            if not pwd.strip():
                print("Password cannot be empty. Please try again.")
                continue
            pwd2 = getpass.getpass("Confirm password: ")
            if pwd != pwd2:
                print("Passwords do not match. Please try again.")
            else:
                self._password = self.hash_password(pwd)
                print("Password set successfully!\n")
                break

    def verify_password(self):
        for _ in range(3):
            if self._check_locked():
                return False
            pwd = getpass.getpass("Enter your profile password: ")
            if self.hash_password(pwd) == self._password:
                return True
            else:
                print("Incorrect password. Try again.")
        print("Too many failed attempts. Access denied.")
        return False
    
    def validate_name(self, name):
        return name.strip() != "" and name.replace(' ', '').isalpha()

    def validate_age(self, age):
        try:
            age_int = int(age)
            return 1 <= age_int <= 120
        except ValueError:
            return False

    def validate_address(self, address):
        return address.strip() != ""

    def validate_phone(self, phone):
        return phone.isdigit() and 10 <= len(phone) <= 15

    def create_profile(self):
        if self._check_locked():
            return
        print("\n[Create Your Profile]")
        self.set_password()
        for key in self.profile:
            while True:
                if self._check_locked():
                    return
                value = input(f"Enter your {key}: ")
                if key == "name":
                    if not self.validate_name(value):
                        print("Invalid name. Please enter alphabetic characters only.")
                        continue
                elif key == "age":
                    if not self.validate_age(value):
                        print("Invalid age. Please enter a number between 1 and 120.")
                        continue
                elif key == "address":
                    if not self.validate_address(value):
                        print("Address cannot be empty.")
                        continue
                elif key == "phone_number":
                    if not self.validate_phone(value):
                        print("Invalid phone number. Enter 10-15 digits.")
                        continue
                self.profile[key] = value
                break
    
    def update_profile(self):
        with self.lock:
            if self._check_locked():
                return
            if not self.verify_password():
                return
            print("\n[Update Your Profile]")
            for key in self.profile:
                while True:
                    if self._check_locked():
                        return
                    new_value = input(f"{key} [{self.profile[key]}]: ")
                    if new_value.strip() == "":
                        break  # keep old value
                    if key == "name":
                        if not self.validate_name(new_value):
                            print("Invalid name. Please enter alphabetic characters only.")
                            continue
                    elif key == "age":
                        if not self.validate_age(new_value):
                            print("Invalid age. Please enter a number between 1 and 120.")
                            continue
                    elif key == "address":
                        if not self.validate_address(new_value):
                            print("Address cannot be empty.")
                            continue
                    elif key == "phone_number":
                        if not self.validate_phone(new_value):
                            print("Invalid phone number. Enter 10-15 digits.")
                            continue
                    self.profile[key] = new_value
                    break
    
    def lock_profile(self):
        with self.lock:
            self.profile = tuple(self.profile.items())
            self.is_locked = True

    def display_profile(self):
        if self._check_locked():
            return
        print("\n[Profile Information]")
        if self.is_locked or (self.lock_event and self.lock_event.is_set()):
            for key, value in self.profile:
                print(f"{key}: {value}")
        else:
            for key in self.profile:
                print(f"{key}: {self.profile[key]}")

    def delete_profile(self):
        with self.lock:
            if self._check_locked():
                return
            if not self.verify_password():
                return
            confirm = input("Are you sure you want to delete your profile? (yes/no): ").strip().lower()
            if confirm == "yes":
                for key in self.profile:
                    self.profile[key] = ""
                print("Profile deleted.")
            else:
                print("Delete cancelled.")

    def save_profile(self, filename='profile.json'):
        if self._check_locked():
            return
        data = {
            'profile': self.profile,
            'password': self._password
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Profile saved to {filename}.")

    def load_profile(self, filename='profile.json'):
        if self._check_locked():
            return
        if not os.path.exists(filename):
            print(f"No saved profile found at {filename}.")
            return
        with open(filename, 'r') as f:
            data = json.load(f)
        self.profile = data.get('profile', self.profile)
        self._password = data.get('password', self._password)
        print(f"Profile loaded from {filename}.")

# =====================
# User and Admin Classes
# =====================

class User:
    """Represents a user profile with authentication and profile data."""
    def __init__(self, username, password_hash, is_admin=False):
        self.username = username
        self.password_hash = password_hash
        self.is_admin = is_admin
        self.profile = {
            "name": "",
            "age": "",
            "address": "",
            "phone_number": "",
            "email": "",
            "gender": "",
            "dob": "",
            "profile_picture": ""
        }
        self.activity_log = []
        self.locked = False
        self.failed_attempts = 0
        self.lock_event = None
        self.twofa_enabled = False
        self._last_2fa_code = None
        self._undo_stack = []
        self._redo_stack = []

    def log_activity(self, action):
        self.activity_log.append((time.strftime('%Y-%m-%d %H:%M:%S'), action))

    def is_profile_locked(self):
        return self.locked or (self.lock_event and self.lock_event.is_set())

    def save_undo(self):
        """Save current profile state for undo."""
        self._undo_stack.append(self.profile.copy())
        if len(self._undo_stack) > 20:
            self._undo_stack.pop(0)
        self._redo_stack.clear()

    def undo(self):
        """Undo last profile change."""
        if self._undo_stack:
            self._redo_stack.append(self.profile.copy())
            self.profile = self._undo_stack.pop()
            self.log_activity("Undo profile edit")
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    def redo(self):
        """Redo last undone profile change."""
        if self._redo_stack:
            self._undo_stack.append(self.profile.copy())
            self.profile = self._redo_stack.pop()
            self.log_activity("Redo profile edit")
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    def enable_2fa(self):
        self.twofa_enabled = True
        print("2FA enabled for your account.")
        self.log_activity("2FA enabled")

    def disable_2fa(self):
        self.twofa_enabled = False
        print("2FA disabled for your account.")
        self.log_activity("2FA disabled")

    def generate_2fa_code(self):
        code = ''.join(random.choices(string.digits, k=6))
        self._last_2fa_code = code
        return code

    def verify_2fa_code(self, code):
        return code == self._last_2fa_code

class UserManager:
    """Manages user registration, login, and admin functions."""
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.admin_username = 'admin'
        self.admin_password = 'Admin@123'  # Default admin password (should be changed)
        self.create_admin()

    def create_admin(self):
        if self.admin_username not in self.users:
            admin_hash = hashlib.sha256(self.admin_password.encode()).hexdigest()
            self.users[self.admin_username] = User(self.admin_username, admin_hash, is_admin=True)

    def register_user(self):
        print("\n[User Registration]")
        while True:
            username = input("Enter a username: ").strip()
            if not username or username in self.users:
                print("Invalid or already taken username. Try again.")
                continue
            password = self.get_strong_password()
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.users[username] = User(username, password_hash)
            print(f"User '{username}' registered successfully!")
            break

    def get_strong_password(self):
        while True:
            password = getpass.getpass("Set a strong password: ")
            if self.validate_password_strength(password):
                confirm = getpass.getpass("Confirm password: ")
                if password == confirm:
                    return password
                else:
                    print("Passwords do not match. Try again.")
            else:
                print("Password must be at least 8 characters, include uppercase, lowercase, digit, and special character.")

    def validate_password_strength(self, password):
        if (len(password) >= 8 and any(c.islower() for c in password) and
            any(c.isupper() for c in password) and any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return True
        return False

    def login_user(self):
        print("\n[User Login]")
        for _ in range(5):
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            user = self.users.get(username)
            if user and user.password_hash == hashlib.sha256(password.encode()).hexdigest():
                if user.failed_attempts >= 3:
                    print("Account locked due to too many failed attempts.")
                    return False
                # 2FA check
                if user.twofa_enabled:
                    code = user.generate_2fa_code()
                    print(f"[2FA] Your authentication code is: {code}")
                    entered = input("Enter the 2FA code: ").strip()
                    if not user.verify_2fa_code(entered):
                        print("Invalid 2FA code. Try again.")
                        user.failed_attempts += 1
                        continue
                self.current_user = user
                user.failed_attempts = 0
                print(f"Welcome, {username}!")
                user.log_activity("Logged in")
                return True
            else:
                if user:
                    user.failed_attempts += 1
                print("Invalid credentials. Try again.")
        print("Too many failed attempts. Account locked.")
        if user:
            user.failed_attempts = 3
        return False

    def logout_user(self):
        if self.current_user:
            print(f"User '{self.current_user.username}' logged out.")
            self.current_user.log_activity("Logged out")
            self.current_user = None

    def is_admin(self):
        return self.current_user and self.current_user.is_admin

    def list_users(self):
        print("\n[Registered Users]")
        for username in self.users:
            print(f"- {username}{' (admin)' if self.users[username].is_admin else ''}")

def main_menu(user_manager):
    """Main menu for login, registration, help, and admin access."""
    while True:
        print(Fore.CYAN + Style.BRIGHT + ASCII_BANNER + Style.RESET_ALL)
        print(f"{Fore.GREEN}{Style.BRIGHT}==== Welcome to the Advanced Profile Management System ===={Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Login{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Register{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Help{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.YELLOW}Select an option (1-4): {Style.RESET_ALL}").strip()
        if choice == "1":
            if user_manager.login_user():
                if user_manager.is_admin():
                    admin_menu(user_manager)
                else:
                    user_session(user_manager)
        elif choice == "2":
            user_manager.register_user()
        elif choice == "3":
            print(Fore.YELLOW + Style.BRIGHT + HELP_TEXT + Style.RESET_ALL)
            input(f"{Fore.YELLOW}Press Enter to return to the main menu...{Style.RESET_ALL}")
        elif choice == "4":
            print(f"{Fore.MAGENTA}Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please select 1-4.{Style.RESET_ALL}")

def admin_menu(user_manager):
    """Admin menu for managing users."""
    while user_manager.current_user and user_manager.is_admin():
        print(f"\n==== Admin Menu (Logged in as: {user_manager.current_user.username}) ====")
        print("1. List Users")
        print("2. View User Activity Log")
        print("3. Reset User Password")
        print("4. Enable/Disable 2FA for User")
        print("5. Search/Filter Users")
        print("6. View Statistics Dashboard")
        print("7. Export Users (JSON/CSV)")
        print("8. Import Users (JSON)")
        print("9. Create Backup")
        print("10. Restore Backup")
        print("11. Logout")
        choice = input("Select an option (1-11): ").strip()
        if choice == "1":
            user_manager.list_users()
        elif choice == "2":
            username = input("Enter username to view activity log: ").strip()
            user = user_manager.users.get(username)
            if user:
                print(f"\nActivity log for {username}:")
                for entry in user.activity_log:
                    print(f"- {entry[0]}: {entry[1]}")
            else:
                print("User not found.")
        elif choice == "3":
            username = input("Enter username to reset password: ").strip()
            user = user_manager.users.get(username)
            if user:
                new_password = user_manager.get_strong_password()
                user.password_hash = hashlib.sha256(new_password.encode()).hexdigest()
                print(f"Password for {username} has been reset.")
                user.log_activity("Password reset by admin")
            else:
                print("User not found.")
        elif choice == "4":
            username = input("Enter username to enable/disable 2FA: ").strip()
            user = user_manager.users.get(username)
            if user:
                if user.twofa_enabled:
                    user.disable_2fa()
                else:
                    user.enable_2fa()
            else:
                print("User not found.")
        elif choice == "5":
            admin_search_filter(user_manager)
        elif choice == "6":
            admin_statistics_dashboard(user_manager)
        elif choice == "7":
            admin_export_users(user_manager)
        elif choice == "8":
            admin_import_users(user_manager)
        elif choice == "9":
            admin_create_backup(user_manager)
        elif choice == "10":
            admin_restore_backup(user_manager)
        elif choice == "11":
            user_manager.logout_user()
            break
        else:
            print("Invalid option. Please select 1-11.")

def admin_search_filter(user_manager):
    """Admin: Search and filter users by name or email."""
    print("\n[Search/Filter Users]")
    query = input("Enter name or email to search: ").strip().lower()
    found = False
    for user in user_manager.users.values():
        if (query in user.profile.get('name', '').lower() or
            query in user.profile.get('email', '').lower()):
            print(f"- Username: {user.username}, Name: {user.profile.get('name','')}, Email: {user.profile.get('email','')}")
            found = True
    if not found:
        print("No users found matching that query.")

def admin_statistics_dashboard(user_manager):
    """Admin: Show statistics dashboard (user count, gender, age distribution)."""
    print("\n[Statistics Dashboard]")
    total_users = len(user_manager.users)
    gender_count = {'male': 0, 'female': 0, 'other': 0, 'unspecified': 0}
    age_buckets = {'<18': 0, '18-30': 0, '31-50': 0, '51+': 0, 'unspecified': 0}
    for user in user_manager.users.values():
        gender = user.profile.get('gender', '').strip().lower()
        if gender in gender_count:
            gender_count[gender] += 1
        else:
            gender_count['unspecified'] += 1
        age = user.profile.get('age', '').strip()
        try:
            age = int(age)
            if age < 18:
                age_buckets['<18'] += 1
            elif age <= 30:
                age_buckets['18-30'] += 1
            elif age <= 50:
                age_buckets['31-50'] += 1
            else:
                age_buckets['51+'] += 1
        except:
            age_buckets['unspecified'] += 1
    print(f"Total users: {total_users}")
    print("Gender breakdown:")
    for g, c in gender_count.items():
        print(f"  {g.capitalize()}: {c}")
    print("Age distribution:")
    for b, c in age_buckets.items():
        print(f"  {b}: {c}")

def get_encryption_key():
    """Prompt for encryption key or use default for demo."""
    key_file = 'encryption.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return key

def encrypt_data(data, key):
    """Encrypt data (bytes) with Fernet key."""
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(token, key):
    """Decrypt data (bytes) with Fernet key."""
    f = Fernet(key)
    return f.decrypt(token)

def admin_export_users(user_manager):
    """Export all users to encrypted JSON and CSV files."""
    users_data = {}
    for username, user in user_manager.users.items():
        users_data[username] = {
            'profile': user.profile,
            'password': user.password_hash,
            'activity_log': user.activity_log,
            'is_admin': user.is_admin,
            'twofa_enabled': user.twofa_enabled
        }
    # Export to encrypted JSON
    key = get_encryption_key()
    json_bytes = json.dumps(users_data, indent=2).encode()
    encrypted = encrypt_data(json_bytes, key)
    with open('users_export.json.enc', 'wb') as f:
        f.write(encrypted)
    # Export to CSV (profile fields only, not encrypted)
    with open('users_export.csv', 'w', newline='') as f:
        fieldnames = ['username'] + list(next(iter(users_data.values()))['profile'].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for username, data in users_data.items():
            row = {'username': username}
            row.update(data['profile'])
            writer.writerow(row)
    print("Users exported to users_export.json.enc (encrypted) and users_export.csv.")

def admin_import_users(user_manager):
    """Import users from an encrypted JSON file."""
    filename = input("Enter encrypted JSON filename to import from (default: users_export.json.enc): ").strip() or 'users_export.json.enc'
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    key = get_encryption_key()
    with open(filename, 'rb') as f:
        encrypted = f.read()
    try:
        json_bytes = decrypt_data(encrypted, key)
        users_data = json.loads(json_bytes.decode())
    except Exception as e:
        print(f"Decryption failed: {e}")
        return
    for username, data in users_data.items():
        user = User(username, data['password'], is_admin=data.get('is_admin', False))
        user.profile = data.get('profile', user.profile)
        user.activity_log = data.get('activity_log', [])
        user.twofa_enabled = data.get('twofa_enabled', False)
        user_manager.users[username] = user
    print(f"Imported users from {filename} (decrypted).")

def admin_create_backup(user_manager):
    """Create an encrypted backup of all users (JSON)."""
    import datetime
    backup_name = f"users_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json.enc"
    users_data = {}
    for username, user in user_manager.users.items():
        users_data[username] = {
            'profile': user.profile,
            'password': user.password_hash,
            'activity_log': user.activity_log,
            'is_admin': user.is_admin,
            'twofa_enabled': user.twofa_enabled
        }
    key = get_encryption_key()
    json_bytes = json.dumps(users_data, indent=2).encode()
    encrypted = encrypt_data(json_bytes, key)
    with open(backup_name, 'wb') as f:
        f.write(encrypted)
    print(f"Encrypted backup created: {backup_name}")

def admin_restore_backup(user_manager):
    """Restore users from an encrypted backup JSON file."""
    filename = input("Enter encrypted backup filename to restore from: ").strip()
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    key = get_encryption_key()
    with open(filename, 'rb') as f:
        encrypted = f.read()
    try:
        json_bytes = decrypt_data(encrypted, key)
        users_data = json.loads(json_bytes.decode())
    except Exception as e:
        print(f"Decryption failed: {e}")
        return
    for username, data in users_data.items():
        user = User(username, data['password'], is_admin=data.get('is_admin', False))
        user.profile = data.get('profile', user.profile)
        user.activity_log = data.get('activity_log', [])
        user.twofa_enabled = data.get('twofa_enabled', False)
        user_manager.users[username] = user
    print(f"Restored users from {filename} (decrypted).")

def user_session(user_manager):
    """User session: profile management, timer, activity log, 2FA, undo/redo."""
    user = user_manager.current_user
    edit_time = 30
    user.lock_event = threading.Event()
    timer_thread = threading.Thread(target=countdown_timer, args=(edit_time, user.lock_event))
    timer_thread.start()
    while not user.is_profile_locked():
        print(f"\n==== User Menu (Logged in as: {user.username}) ====")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Delete Profile")
        print("4. View Activity Log")
        print("5. Save Profile")
        print("6. Load Profile")
        print("7. Enable/Disable 2FA")
        print("8. Undo Last Edit")
        print("9. Redo Last Edit")
        print("10. Logout")
        choice = input("Select an option (1-10): ").strip()
        if user.is_profile_locked():
            print("\n[!] Profile is now locked. No further actions are allowed.")
            break
        if choice == "1":
            display_user_profile(user)
        elif choice == "2":
            user.save_undo()
            update_user_profile(user)
        elif choice == "3":
            confirm = input("Are you sure you want to delete your profile? (yes/no): ").strip().lower()
            if confirm == "yes":
                user.save_undo()
                for key in user.profile:
                    user.profile[key] = ""
                print("Profile deleted.")
                user.log_activity("Profile deleted")
            else:
                print("Delete cancelled.")
        elif choice == "4":
            print(f"\nActivity log for {user.username}:")
            for entry in user.activity_log:
                print(f"- {entry[0]}: {entry[1]}")
        elif choice == "5":
            save_user_profile(user)
        elif choice == "6":
            load_user_profile(user)
        elif choice == "7":
            if user.twofa_enabled:
                user.disable_2fa()
            else:
                user.enable_2fa()
        elif choice == "8":
            user.undo()
        elif choice == "9":
            user.redo()
        elif choice == "10":
            user_manager.logout_user()
            break
        else:
            print("Invalid option. Please select 1-10.")
    user.locked = True
    print("\n[Profile is now locked. Final state:]")
    display_user_profile(user)

def display_user_profile(user):
    print("\n[Profile Information]")
    for key in user.profile:
        print(f"{key}: {user.profile[key]}")

def update_user_profile(user):
    print("\n[Update Your Profile]")
    for key in user.profile:
        new_value = input(f"{key} [{user.profile[key]}]: ")
        if new_value.strip() != "":
            user.profile[key] = new_value
    user.log_activity("Profile updated")

def save_user_profile(user, filename=None):
    if not filename:
        filename = f"{user.username}_profile.json"
    data = {
        'profile': user.profile,
        'password': user.password_hash,
        'activity_log': user.activity_log
    }
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Profile saved to {filename}.")
    user.log_activity("Profile saved")

def load_user_profile(user, filename=None):
    if not filename:
        filename = f"{user.username}_profile.json"
    if not os.path.exists(filename):
        print(f"No saved profile found at {filename}.")
        return
    with open(filename, 'r') as f:
        data = json.load(f)
    user.profile = data.get('profile', user.profile)
    user.password_hash = data.get('password', user.password_hash)
    user.activity_log = data.get('activity_log', user.activity_log)
    print(f"Profile loaded from {filename}.")
    user.log_activity("Profile loaded")

# Entry point
if __name__ == "__main__":
    user_manager = UserManager()
    main_menu(user_manager)
