import pyfiglet as pf
import sys, time, requests, os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
try: 
    ascii_banner = pf.figlet_format("Un-Bored")
    print(bcolors.OKGREEN + ascii_banner)
    print(bcolors.OKCYAN + "Made by Yiit#3276 on discord")
    print(bcolors.WARNING+"WARNING: Prices cannot be accurate do this at your own risk."+bcolors.OKCYAN)
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    y_n = input(str("Are you ready to fun? (y/n): "))

    def aktivite():
        response = requests.get("https://www.boredapi.com/api/activity/")
        data = response.json()
        activity = data["activity"]
        a_type = data["type"]
        participants = data["participants"]
        price = str(data["price"])+"$"
        link = data["link"]
        if response.status_code == 200:
            print("-" *21+"ACTIVITY" + "-" *21)
            print("[*] Activity: " + str(activity))
            print("[*] Type: " + str(a_type))
            print("[*] Participants: " + str(participants))
            print("[*] Price: " + str(price))
            print("[*] Link: " + str(link))
            print("-" *50)
            again = input(str(bcolors.OKBLUE + "An other activity? (y/n): "))
            if(again.lower() == "y"):
                cls()
                print(bcolors.OKGREEN + ascii_banner + bcolors.OKCYAN)
                aktivite()
            else:
                sys.exit(0)
        else:
            print(bcolors.FAIL+"An error occurred\n error code: " + str(response.status_code))

    if(y_n.lower() == "y"):
        cls()
        print(bcolors.OKGREEN + ascii_banner + bcolors.OKCYAN)
        response = requests.get("https://www.boredapi.com/api/activity/")
        data = response.json()
        activity = data["activity"]
        a_type = data["type"]
        participants = data["participants"]
        price = str(data["price"])+"$"
        link = data["link"]
        aktivite()
    else:
        sys.exit(0)
except KeyboardInterrupt:
    print(bcolors.FAIL+"\n\n\n\nSystem has been terminated.")
    sys.exit(0)