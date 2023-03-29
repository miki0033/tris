import os

def clearTerminal():
    sys = os.name
    print(sys)
    if (sys == 'posix'):
        os.system('clear')
    if (sys == "nt"):
        os.system('cls')

