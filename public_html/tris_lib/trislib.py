import os
import sys


def clearTerminal():
    sys = os.name
    print(sys)
    if sys == "posix":
        os.system("clear")
    if sys == "nt":
        os.system("cls")


def printTerminal(str):
    print(str, file=sys.stdout)
