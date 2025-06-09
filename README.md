# 🔐 **Local Password Manager**

A simple and secure password manager built with Python. It provides an easy-to-use graphical interface for storing, viewing, and managing your credentials locally. All passwords are encrypted using industry-standard encryption and stored securely in a local database.

# 📌 **Features**
- Graphical User Interface (GUI) using tkinter

- Secure password encryption using the cryptography module (Fernet)

- Local storage using SQLite database

- Add new credentials (website, username/email, password)

- View saved credentials

- Delete credentials

- All data is stored offline, on your local machine

# 🏗️ **Project Structure**


├── generate_key.py              # Script to generate encryption key

├── main.py                       # Main application script

├── passwords.db                 # SQLite database storing encrypted passwords

├── README.md                    # Project documentation

  # 🛠️ **Requirements**
- Python 3.x

- tkinter – GUI framework

- sqlite3 – Built-in local database

- cryptography – For secure encryption of passwords

Make sure you have Python installed. Then install these dependencies:

pip install -r requirements.txt


# 🔑**Encryption Key**
- The app uses Fernet symmetric encryption from the cryptography library.

- A key is generated.

- This key is used to encrypt and decrypt passwords.

- Do not delete key — without it, your stored data cannot be decrypted.


# 🧠 **How It Works**
1. On first run:

- Generates a unique encryption key and stores it in key.key

- Initializes a local SQLite database named passwords.db

2. When a password is added:

- The password is encrypted using the key

- Encrypted data is saved in the database

3. When viewing:

- The encrypted password is decrypted using the key and shown in the GUI
