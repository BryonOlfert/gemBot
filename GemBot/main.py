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

        # clicks into game and gets ready to build
        pydirectinput.leftClick(800, 500)
        selectHero()

        # sets up build order for each attempt
        tempBuilds = []
        tempCenterBuilds1P = []

        for each in builds:
            tempBuilds.append(each)

        for each in centerBuilds1P:
            tempCenterBuilds1P.append(each)

        # gems for each build round
        roundGems = []

        # settled Gems
        settledGems = []

        ####start####

        for i in range(1, 6):

            if i > 1:
                # check for oneshot
                testOneShots = []
                for each in gemBuilds:
                    test = checkOneShots(each)
                    if test != None:
                        testOneShots.append(test)

            # places gem using placeGem and adds it to roundGems table
            roundGems.append([placeGem(tempBuilds[0][0], tempBuilds[0][1]), [
                             tempBuilds[0][0], tempBuilds[0][1]]])

            # Removes index 0 from tempBuilds
            tempBuilds.pop(0)

        for each in roundGems:
            print(each[0])
            print(each[1])

        print(" ")

        for each in testOneShots:
            print(each)


main()
