exec(open("combinations.py").read())
exec(open("functions.py").read())
exec(open("builds.py").read())
exec(open("gemBuilds.py").read())
exec(open("centerBuilds1p.py").read())



def main():
    # turn on failsafe and starts
    pyautogui.FAILSAFE = True
    countDownTimer(2)
    
    while 1 == 1:
        image = pyautogui.locateCenterOnScreen("buttons/present2.png", grayscale=False, confidence=.9, region=(1654, 502, 1768, 576))
        time.sleep(.1)
        if image == None:
            remake = true


main()