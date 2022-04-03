import pyautogui
import time
import math
from PIL import Image
import cv2
from os.path import exists
import array
import pydirectinput


gems = {"p","r","g","b","y","d","e","q"}
screenWidth, screenHeight = pyautogui.size()

def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def keyPress(x):
    pydirectinput.press(x)

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

def selectHero():
    pydirectinput.press('f1')
    

def move(x,y):
    pyautogui.moveTo(16+6*x, 1066-6*y)
    time.sleep(0.5)
    pyautogui.rightClick()

def lookAt(x,y):
    pyautogui.moveTo(16+6*x, 1066-6*y)
    time.sleep(0.19)
    pyautogui.click()
    pyautogui.moveTo(screenWidth/2,screenHeight/2)
    time.sleep(0.19)
    pyautogui.click()

def build(x,y):

    keyPress('q')

    time.sleep(0.1)
    pyautogui.moveTo(16+x*6,1066-6*y)
    time.sleep(0.1)
    pyautogui.click()

    image = None
    timer = 0

    while image == None:
        image = pyautogui.locateCenterOnScreen("buttons/building.png", grayscale=False, confidence=.7)
        time.sleep(0.005)
        timer += 0.005
        if timer > 10:
            break
        
    time.sleep(0.05)
    

#places gme and returns the gem that is placed and it's position    
def placeGem(x,y):
    # This allows bot to select build
    selectHero()

    # Builds a gem from index o of tempBuilds table
    build(x,y)
    time.sleep(.3)

    # Focuses the gem that has just been built
    keyPress("tab")
    time.sleep(0.05)
    
    # Checks which gem has been placed
    return checkGem()


def checkGem():
    found = False
    for gem in gems:
        
        if found == True:
            break

        for i in range(1, 6):

            path = 'gems/'+str(gem)+str(i)+'.png'
        
            if exists(path):
                if pyautogui.locateCenterOnScreen(path, grayscale=False, confidence=.9, region=(589,913, 689, 960)) != None:
                    return gem+str(i)
                    test = True 
                    break
                else:
                    continue
            else:
                continue
        
            


def searchClick(x,*args):
    image = pyautogui.locateCenterOnScreen(x)
    conf = 1.0
    gScale = True
    
    if not args:
        y = 0.09
    else:
        y = args[0]

    while image == None:
        image = pyautogui.locateCenterOnScreen(x, grayscale=gScale, confidence=conf)
        #print("still looking for "+str(x))
        time.sleep(0.1)
        conf = conf - 0.005
        if conf < 0.55:
            gScale = True

    time.sleep(.2)
    conf = conf - .05
    while image != None:
        time.sleep(.25)
        #pyautogui.click(pyautogui.locateCenterOnScreen(x, grayscale=gScale, confidence=conf))
        pyautogui.moveTo(image)
        time.sleep(.1)
        pydirectinput.click()
        time.sleep(y)
        image = pyautogui.locateCenterOnScreen(x, grayscale=gScale, confidence=conf) 
        conf = conf + 0.01
    time.sleep(.25)
    

#returns bool for image search results x = image y = timeout
def search(x,y):
    image = pyautogui.locateCenterOnScreen(x)
    timeout = time.time() + y
    while image == None:
        image = pyautogui.locateCenterOnScreen(x)
        if time.time() > timeout:
            break
    return image

def restart():
    
    #keyPress('enter')
    #time.sleep(.1)
    #keyPress('-')
    #time.sleep(0.05)
    #keyPress('w')
    #time.sleep(0.05)
    #keyPress('t')
    #time.sleep(0.05)
    #keyPress('f')
    #time.sleep(0.05)
    #keyPress('enter')
    #time.sleep(0.05)

    searchClick("buttons/exitButton.png")

    searchClick("buttons/disconnect.png")

    searchClick("buttons/leaveGame.png")

    searchClick("buttons/play.png")

    searchClick("buttons/accept.png")

    searchClick("buttons/startGame.png",3.5)

    image = pyautogui.locateCenterOnScreen("buttons/gameLoad.png", grayscale=False, confidence=.99)
    while image == None:
        image = pyautogui.locateCenterOnScreen("buttons/gameLoad.png", grayscale=False, confidence=.99)
        time.sleep(0.05)  

#returns list of basic builds when given a combination tower
def getTowerGems(x):
  gems = []
  if hasattr(x,'gem1'):
    builds = [x.gem1,x.gem2,x.gem3]

  for each in builds:
    if hasattr(each,'gem1'):
      for each in getTowerGems(each):
        gems.append(each)
    else:
      gems.append(each)
  return gems

#returns what is needed to oneshot a tower
def checkOneShot(tower):

    if type(tower) == str:

        if int(tower[1]) > 1:

            if int(tower[1]) > 2:

                x = tower[0]+str(int(tower[1])-1)
                y = tower[0]+str(int(tower[1])-2)
                return([[x,x],[y,y,y,y]])

            else:

                x = tower[0]+str(int(tower[1])-1)
                return([x,x])    
        else:

            return(str(tower))

    else:

        return(getTowerGems(tower))
        


# This function returns a list of all builds it can take, compared to the list of builds we want.
# roundBuilds is the gems the bots placed this round
def buildables(roundBuilds):

    isBuildable = []

    for each in gemBuilds:

        if type(each) == Tower:

            if all(item in roundBuilds for item in checkOneShot(each)) == True:
                isBuildable.append(each)

        else:
            if each in roundBuilds:
                isBuildable.append(each)
            else:
                oneShots = checkOneShot(each)
                if len(oneShots[1]) > 2:
                    x = oneShots[1][0]
                    if roundBuilds.count(x) >= oneShots[1].count(x):
                        isBuildable.append(each)
                    else:

                        x = oneShots[0][0]
                        if roundBuilds.count(x) >= oneShots[0].count(x):
                            isBuildable.append(each)

                else:
                    x = oneShots[0]
                    if roundBuilds.count(x) >= oneShots.count(x):
                        isBuildable.append(each)
    return isBuildable                
    

    