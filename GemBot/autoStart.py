exec(open("functions.py").read())

def main():
    while 1 == 1:
        image = pyautogui.locateCenterOnScreen("buttons/accept.png", grayscale=False, confidence=.8)

        if image != None:
            pydirectinput.click(image[0],image[1])
        time.sleep(1)

main()