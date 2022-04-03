import pyautogui
import time

def initializePyAutoGui():
    #turn on failsafe
    pyautogui.FAILSAFE = True

def countDownTimer(var):
    print("starting")
    for i in range(0,var):
        print(var-i)
        time.sleep(1)
    print("Go")

def reportMousePosition(var):
    for i in range(0, var):
        print(pyautogui.position())
        time.sleep(3)

def main():

    initializePyAutoGui()
    countDownTimer(2)

    reportMousePosition(2)



main()