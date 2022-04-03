exec(open("functions.py").read())
exec(open("builds.py").read())
exec(open("gemBuilds.py").read())

def main():
    #turn on failsafe
    pyautogui.FAILSAFE = True
    countDownTimer(2)

    roundGems = []
    placements = []

    for i in range(0,5):

       
        
        time.sleep(0.1)
        lookAt(builds[0][0],builds[0][1])
        time.sleep(0.1)
        testGem = checkGem()
        roundGems.append(testGem)

       
        time.sleep(0.1)
        placements.append([builds[0][0],builds[0][1]])
        builds.pop(0)

    rCount= 0 
    for i in range(0,5):
        if roundGems[i] == "r1":
            rCount = rCount + 1
        
    if rCount < 3:
        restart()

main()