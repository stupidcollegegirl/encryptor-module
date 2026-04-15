# 🔐 Python Encrypt Tool

**A clean, secure and user-friendly TUI (Text User Interface) utility for encrypting and decrypting files using symmetric encryption.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Fernet](https://img.shields.io/badge/Encryption-Fernet-2ECC71?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## ✨ Features

- **Secure file encryption** using `cryptography.fernet` (AES-128 + HMAC-SHA256)
- **Simple and intuitive TUI** with beautiful terminal interface
- Support for **any file type** — documents, photos, videos, archives, etc.
- Fast text encryption mode (great for passwords and notes)
- Automatic file handling with `.encrypted` extension
- Built-in error handling and user-friendly messages
- Cross-platform (Windows, Linux, macOS)


## 🚀 Quick Start

### Installation

```
git clone https://github.com/stupidcollegegirl/encryptor-module.git
cd python-encrypt-tool
pip install -r requirements.txt
```

### Usage
```
python main.py
Then choose from the menu:

1 — Generate a new encryption key
2 — Encrypt a file
3 — Decrypt a file
4 — Encrypt text
0 — Exit
```

🔑 Important Security Notes

Keep your secret.key file in a safe place. Anyone who has this key can decrypt your files.
It is recommended to store the key on a separate encrypted USB drive or in a password manager.
After encryption, delete the original files if they contain sensitive information.
Lost key = lost data permanently.

🛠️ Technologies Used

Python
cryptography — Fernet symmetric encryption
rich — Beautiful terminal interface
pathlib — Modern file path handling


📁 Project Structure
```
textpython-encrypt-tool/
├── encryptor/          # Main
│   ├── __init__.py
│   ├── core.py         # Логика
│   ├── cli.py          # TUI
│   └── utils.py
├── main.py             # Start
├── requirements.txt
└── README.md
