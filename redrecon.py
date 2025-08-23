import os
import sys
from colorama import Fore
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    try:
        print(f"""       
  {Fore.GREEN}  


    ======================================================================     
    ███╗   ██╗██╗   ██╗██╗  ██╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗      
    ████╗  ██║██║   ██║██║ ██╔╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
    ██╔██╗ ██║██║   ██║█████╔╝ ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
    ██║ ╚████║╚██████╔╝██║  ██╗██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
    ======================================================================
        {Fore.RED}@Inspired From AnonKryptiQuz {Fore.YELLOW} ----- {Fore.RED}   @Version 1.0{Fore.YELLOW} 
        {Fore.YELLOW}

        [1] Subdomain Scanner
        [2] Path Scanner
        [0] Exit
 {Fore.WHITE}
""")

        options = int(input(f"{Fore.CYAN}Enter The Option Please: "))

        if options == 1:
            print(Fore.YELLOW + "Subdomain Scanner Is Activating..." + Fore.WHITE)
            script_path = os.path.join(os.getcwd(), "SUBDOMAIN", "subdomain.py")
            subprocess.run([sys.executable, script_path])
            input("\nPress ENTER to return to menu...")
            clear_screen()
            menu()

        elif options == 2:
            print(Fore.YELLOW + "Path Scanner Is Activating..." + Fore.WHITE)
            script_path = os.path.join(os.getcwd(), "PATH SCANNER", "pathscanner.py")
            subprocess.run([sys.executable, script_path])
            input("\nPress ENTER to return to menu...")
            clear_screen()
            menu()

        elif options == 0:
            print("Exit")
            sys.exit(0)

        else:
            print("Invalid Entry")
            clear_screen()
            menu()

    except ValueError:
        print("Invalid input! Please enter option numbers.")
        clear_screen()
        menu()

    except KeyboardInterrupt:
        print(f"\n(CTRL+C) is not in the option.")

if __name__ == "__main__":
    clear_screen()
    menu()
