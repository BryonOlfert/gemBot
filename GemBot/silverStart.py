exec(open("functions.py").read())
exec(open("builds.py").read())
exec(open("gemBuilds.py").read())
exec(open("centerBuilds1p.py").read())

def main():
    #turn on failsafe and starts
    pyautogui.FAILSAFE = True
    countDownTimer(2)

    
    
        

    silverTest = False
    
    while silverTest == False:
        
        #clicks into game and gets ready to build
        pydirectinput.leftClick(800, 500)
        selectHero()

        #sets up build order for each attempt
        tempBuilds = []
        tempCenterBuilds1P = []

        for each in builds:
            tempBuilds.append(each)

        for each in centerBuilds1P:
            tempCenterBuilds1P.append(each)


        #gems for each build round
        roundGems = []

        #settled Gems
        placements = []

        #when true bot will reset
        remake = False

        # builds for 5 rounds
        for i in range(0,5):
            
            # This places a gem and adds it to roundGems table
            placeGem()

            testy = False
            testd = False
            testb = False

            test = 0

            for each in roundGems:
                if testy == False and each == "y1":
                    testy = True
                    test += 1
                if testd == False and each == "d1":
                    testd = True
                    test += 1
                if testb == False and each == "b1":
                    testb = True
                    test += 1
            if test == 2:
                tempBuilds.insert(0,tempCenterBuilds1P[0])
                tempCenterBuilds1P.pop(0)
            if (5 - i) - (3 - test) < 1:
                remake = True
                break

        if remake == True or test < 3:
            restart()
        else:
            silverTest = True
        
main()
