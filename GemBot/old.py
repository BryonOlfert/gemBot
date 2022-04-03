exec(open("functions.py").read())

def main():
    #turn on failsafe
    pyautogui.FAILSAFE = True
    countDownTimer(2)

    while True:
        
        time.sleep(1)
        selectHero(17,20)
        time.sleep(0.5)

    
        lookAt(17,20)
        selectHero(17,20)
        time.sleep(0.5)

        #start

        #build phase 1
        
        roundGems = []
        

        build(4,19)

        build(9,18)
        
        build(10,18)

        build(11,18)

        lookAt(4,19)
        roundGems.append(checkGem())

        lookAt(9,18)
        roundGems.append(checkGem())

        lookAt(10,18)
        roundGems.append(checkGem())

        lookAt(11,18)
        roundGems.append(checkGem())

        r1Test = 0
        r1Test2 = False
        for each in roundGems:
            if each == "r1":
                r1Test = r1Test + 1
            else:
                continue
        if r1Test > 3:
            break
        else:
            restart()




        
        
            #lookAt(17,18)
        #if checkGem() != "r1":
         #   restart()
        #else:

        #    if testGem == True:
         #       lookAt(17,18)
          #      searchClick("buttons/upgrade.png")
           #     break

            #else:
                
             #   restart()        
    
        #centerHero(9,10)


    #build(12,18)


    print("Done")
        

main()
