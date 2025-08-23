import sys
import requests
from colorama import Fore
import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_path(url, path, results):
    full_url = f"{url.rstrip('/')}/{path.lstrip('/')}"
    try:
        r = requests.get(full_url, timeout=3)
        if r.status_code < 400:
            line = f"[🟢 LIVE PATH] {full_url} - {r.status_code}"
            print(Fore.GREEN + line)
            results.append(line)
    except (requests.ConnectionError, requests.Timeout):
        pass

def main():
    print(f"""
    {Fore.RED}PATH SCANNER {Fore.WHITE}
    """)

    print(f"""{Fore.YELLOW}
    [1] Path Scanner
    [2] Back
    """)

    try:
        choice = int(input(f"{Fore.CYAN}Enter your choice (1 or 2): "))
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter 1 or 2.{Fore.WHITE}")
        return
    except KeyboardInterrupt:
        print(f"{Fore.RED}(CTRL+C) is not in an option.{Fore.WHITE}")
        return

    if choice == 1:
        url = input(f"{Fore.CYAN}Enter target URL (e.g. https://example.com): ").strip()
        try:
            wordlist_file = os.path.join(os.path.dirname(__file__), "wordlist.txt")
            with open(wordlist_file, "r") as file:
                paths = file.read().splitlines()
        except FileNotFoundError:
            print("wordlist.txt not found!")
            return

        results = []
        print(f"\nScanning paths in {url}...\n")
        for path in paths:
            scan_path(url, path, results)

        # Спросить о сохранении результатов
        if results:
            save_choice = input(Fore.CYAN + "\nDo you want to save the results to a .txt file? (y/n): ").strip().lower()
            if save_choice == "y":
                file_name = input("Enter filename (without .txt): ").strip()
                with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(results))
                print(Fore.YELLOW + f"[+] Results saved to {file_name}.txt")
        else:
            print(Fore.RED + "\nNo live paths found.")

    elif choice == 2:
        main_script = os.path.join(os.getcwd(), "redrecon.py")
        subprocess.run([sys.executable, main_script])

    else:
        print(f"{Fore.RED}Invalid choice. Exiting.{Fore.WHITE}")

if __name__ == "__main__":
    clear_screen()
    main()
