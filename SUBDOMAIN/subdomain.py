import sys
import subprocess
import requests
from colorama import Fore
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def scan_subdomain(domain):
    results = []  # Сохранять все активные поддомены 

    try:
        subdomains_file = os.path.join(os.path.dirname(__file__), "subdomains.txt")
        with open(subdomains_file, "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("subdomains.txt not found!")
        return

    print(f"\nScanning subdomains for {domain}...\n")
    
    # Проверить sub.domain
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400: # Active
                line = f"[🟢 LIVE SUBDOMAIN] {url} - {r.status_code}"
                print(Fore.GREEN + line)
                results.append(line)
        except (requests.ConnectionError, requests.Timeout):
            pass

    # Проверить domain.sub
    for sub in subdomains:
        url = f"http://{domain}.{sub}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code < 400:
                line = f"[🟢 LIVE SUBDOMAIN] {url} - {r.status_code}"
                print(Fore.GREEN + line)
                results.append(line)
        except (requests.ConnectionError, requests.Timeout):
            pass

    # Спросить о сохранении результатов
    if results:
        save_choice = input(Fore.CYAN + "\nDo you want to save the results to a .txt file? (y/n): ").strip().lower()
        if save_choice == "y":
            file_name = input("Enter filename (without .txt): ").strip()
            with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(results))
            print(Fore.YELLOW + f"[+] Results saved to {file_name}.txt")
    else:
        print(Fore.RED + "\nNo live subdomains found.")

def main():
    print(f"""
    {Fore.RED} SUBDOMAIN SCANNER {Fore.WHITE}
    """)

    print(f"""{Fore.YELLOW}
    [1] Subdomain Scanner
    [2] Back
    """)

    try:
        choice = int(input(f"{Fore.CYAN}Enter your choice (1 or 2): "))
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter 1 or 2.{Fore.WHITE}")
        clear_screen()
        main()
        return
    except KeyboardInterrupt:
        print(f"{Fore.RED}(CTRL+C) is not in an option.{Fore.WHITE}")
        return

    if choice == 1:
        domain = input(f"{Fore.CYAN}Enter root domain (e.g. testfire.net): ").strip()
        scan_subdomain(domain)

    elif choice == 2:
        main_script = os.path.join(os.getcwd(), "redrecon.py")
        subprocess.run([sys.executable, main_script])

    else:
        print(f"{Fore.RED}Invalid choice. Exiting.{Fore.WHITE}")
        
if __name__ == "__main__":
    clear_screen()
    main()
