from encryptor.core import generate_key, encrypt_file, decrypt_file, encrypt_text


def show_menu():
    print("""\


███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   
    """)

    print("_"*40)
    print()
    print("1 → Create a new key")
    print("2 → Encrypt file")
    print("3 → Decrypt file")
    print("4 → Encrypt text rn")
    print("0 → Log out")
    print("_"*40)

def run_cli():
    while True:
        show_menu()
        choice = input("\nSelect → ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            path = input("Enter the file directory: ").strip()
            if path:
                encrypt_file(path)
        elif choice == "3":
            path = input("Path to the .encrypted file: ").strip()
            if path:
                decrypt_file(path)
        elif choice == "4":
            encrypt_text()
        elif choice == "0":
            print("👋 See you later")
            break
        else:
            print("❌ The wrong choice")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    run_cli()
