exec(open("combinations.py").read())
exec(open("functions.py").read())
exec(open("builds.py").read())
exec(open("gemBuilds.py").read())
exec(open("centerBuilds1p.py").read())


def main():
    # turn on failsafe and starts
    pyautogui.FAILSAFE = True
    countDownTimer(2)

    round = 1


    # runs until good rng is achieved
    while 1 == 1:

        # when true bot will reset
        remake = False


        while checkStart() == None:
                continue
        time.sleep(1.5)


        # clicks into game and gets ready to build
        pydirectinput.leftClick(800, 500)
        selectHero()

        # sets up build order for each attempt
        tempBuilds = []
        tempCenterBuilds1P = []
        gemBuilds = []

        for each in gemBuildsStart:
            gemBuilds.append(each)

        for each in builds:
            tempBuilds.append(each)

        for each in centerBuilds1P:
            tempCenterBuilds1P.append(each)

        

        # settled Gems
        settledGems = []

        ####start####

        while remake == False:
            
            # gems for each build round
            roundGems = []

            for i in range(1, 6):

                if i > 1:
                    # check for oneshot
                    testOneShots = []
                    for each in gemBuilds:
                        test = checkOneShot(each)
                        if test != None:
                            testOneShots.append(test)

                # places gem using placeGem and adds it to roundGems table
                seated = SeatedGem(placeGem(tempBuilds[0][0], tempBuilds[0][1]),[tempBuilds[0][0], tempBuilds[0][1]],False)
                roundGems.append(seated)

                # Removes index 0 from tempBuilds
                tempBuilds.pop(0)


            checkList = []
            for each in roundGems:
                checkList.append(str(each.tower))
            
            take = buildables(checkList)

            if take != None:
                if take [1] != 1:
                
                    if take[1] == 2:
                        take[0] = take[0][:-1] + str(int(take[0][-1])-1)
                    else:

                        if take[1] == 3:
                            take[0] = take[0]-1+str(int(take[0][-1])-2)
                        else:
                            print("Take a picture of this button")
                            while True:
                                continue

                for each in roundGems:
                    if str(each.tower) == take[0]:
                        lookAt(each.location[0],each.location[1])
                        time.sleep(0.1)
                        searchClick("buttons/take"+str(take[1])+".png")
                        gemBuilds.pop(take[0])
                        settledGems.append(each)
                        time.sleep(0.5)
                        break
                
                selectHero()
                pydirectinput.moveTo(900,500)
                time.sleep(0.5)

                keyPress("9")
                time.sleep(1)

                while checkStart() == None:
                    image = pyautogui.locateCenterOnScreen("buttons/present2.png", grayscale=False, confidence=.9, region=(1654, 502, 1768, 576))
                    time.sleep(.1)
                    if image == None:
                        remake = True
                        break

            else:
                remake = True



            if remake == True:
                restart()
                while checkStart() == None:
                    continue
                time.sleep(1.5)

            


main()
