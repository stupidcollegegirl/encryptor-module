from cryptography.fernet import Fernet
import datetime
from pathlib import Path
from typing import Optional


def generate_key() -> bytes:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("✅ The key was successfully generated and saved to the file: secret.key")
    return key


def load_key() -> Optional[bytes]:
    try:
        with open("secret.key", "rb") as f:
            key = f.read()
        print("✅ Key loaded successfully")
        return key
    except FileNotFoundError:
        print("❌ File secret.key not found. Create a key.")
        return None
    except Exception as e:
        print(f"❌ Error loading key: {e}")
        return None


def encrypt_file(input_path: str) -> bool:
    key = load_key()
    if key is None:
        return False

    f = Fernet(key)
    path = Path(input_path)

    try:
        data = path.read_bytes()
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        return False
    except Exception as e:
        print(f"❌ File read error: {e}")
        return False

    encrypted = f.encrypt(data)
    output_path = path.with_suffix(path.suffix + ".encrypted")

    output_path.write_bytes(encrypted)
    print(f"✅ Text is encrypted → {output_path}")
    return True


def decrypt_file(encrypted_path: str) -> bool:
    key = load_key()
    if key is None:
        return False

    f = Fernet(key)
    path = Path(encrypted_path)

    try:
        data = path.read_bytes()
    except FileNotFoundError:
        print(f"❌ File read error: {path}")
        return False

    try:
        decrypted = f.decrypt(data)
    except Exception:
        print("❌ Error: invalid key or corrupted file")
        return False

    original_path = path.with_suffix("")

    original_path.write_bytes(decrypted)
    print(f"✅ Text is encrypted → {original_path}")
    return True


def encrypt_text() -> bool:
    print("Enter text :")
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    if not lines:
        print("❌ Text is empty")
        return False

    text = "\n".join(lines)
    data = text.encode("utf-8")

    key = load_key()
    if key is None:
        return False

    f = Fernet(key)
    encrypted = f.encrypt(data)

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"encrypted_text_{now}.txt.encrypted"

    with open(filename, "wb") as file:
        file.write(encrypted)

    print(f"✅ Text is encrypted → {filename}")
    return True
