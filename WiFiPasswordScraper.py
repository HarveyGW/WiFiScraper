import subprocess
from colorama import Fore

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    print(Fore.WHITE + wifi)
    if "'" in wifi:
        print(Fore.RED + "Cannot Get Password For {} Due To The Apple Having Bad Encoding :/".format(wifi))
    else:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        try:
            print(Fore.GREEN)
            print(f'Name: {wifi}, Password: {results[0]}')
        except IndexError:
            print(Fore.RED)
            print(f'Name: {wifi}, Password: Cannot Be Read!')
    print("\n")

print(Fore.RESET)
