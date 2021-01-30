import subprocess

from pyfiglet import print_figlet


# Function for user to choose scan type
# Runs chosen scan type and restarts if choice is invalid
def user_choice():
    while True:
        try:
            choice = input("Start Scan? (Y/N): ")
            if choice == 'Y':
                subprocess.call("standard_scan.py", shell=True)
            elif choice == 'N':
                break
            else:
                print("Not a valid option.")
                print("Restarting! \n")
                continue
        except Exception as e:
            print(e)
            print('Restarting! \n')
            continue
        else:
            break


if __name__ == '__main__':
    # Banner and User Interface
    colors = "95;197;220:"
    print_figlet("Port Scanner", font='slant', colors=colors)
    print("Welcome to a Python Port Scanner \n")

    user_choice()
