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
        image = pyautogui.locateCenterOnScreen("buttons/present2.png", grayscale=False, confidence=.9, region=(1210, 478, 1301, 605))
        time.sleep(.1)
        if image == None:
            print("restart boi")
        else:
            print("all good")


main()