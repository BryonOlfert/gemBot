exec(open("functions.py").read())

def main():
    # turn on failsafe and starts
    pyautogui.FAILSAFE = True
    countDownTimer(2)

    restart()

main()

