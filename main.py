import thread 
from tkinter import * as tk
# init environment
def startCOC():
    # switch to Bluestacks, if Bluestacks is not running, start it
    switchApp("C:\Program Files (x86)\BlueStacks\HD-StartLauncher.exe")
    # aviod full screen
    waitVanish("1404874951038.png")
    sleep(3)
    
    if exists("1404874624486.png"):
        type(Key.F11)
        print "To aviod full screen, F11 pressed!"
    #start COC, not working?
    wait("1404873600708.png",30)
    click("1404873600708.png")

def openSiderBar():
    sidebarOpenerRegion = Region(sidebarRegion.x, sidebarRegion.y + 140, 50, 100)
    if sidebarOpenerRegion.exists("1405564549169.png",0):
        click(sidebarOpenerRegion.getLastMatch())
        sleep(0.5)
    if sidebarOpenerRegion.exists("1405564549169.png",0):
        click(sidebarOpenerRegion.getLastMatch())
    print "SliderBar opened", time.time() - loopStart

def closeSiderBar():
    sidebarCloserRegion = Region(sidebarRegion.x + 260, sidebarRegion.y + 140, 50, 100)
    if sidebarCloserRegion.exists("1405565294613.png",0):
        click(sidebarCloserRegion.getLastMatch())
        sleep(0.5)
    if sidebarCloserRegion.exists("1405565294613.png",0):
        click(Location(cocRegion.x + 1064, cocRegion.y + 290))            
        click(sidebarCloserRegion.getLastMatch())
    print "SliderBar closed", time.time() - loopStart


def openDonateDialog(Reg):
    mmd = Settings.MoveMouseDelay # save default/actual value
    Settings.MoveMouseDelay = 0
    requestImages = ["1404963677861.png", "1404893661366.png", "1404973195624.png", "1405000459163.png", "1405039582725.png", "1404889472348.png", "1404955811222.png","1405039210619.png", "1405039285639.png", "1405039311968.png"]
    donateTypeRegOffsetX = 75
    donateTypeRegOffsetY = 27
    
    if Reg.exists(Pattern("1404875979174.png").similar(0.90), 15):
        print("donate icon found")
        for d in Reg.findAll("1404875979174.png"):
            donateTypeReg = Region(d.x - donateTypeRegOffsetX, d.y - donateTypeRegOffsetY, d.w + 2*donateTypeRegOffsetX ,18)
            #donateTypeReg.highlight(1)
            donatetype = 0
            #test
            searchStartTime = time.time();
            donateTypeRetVal = donateTypeNew(requestImages,  first = True, reg = donateTypeReg)
            print "search time:", time.time()- searchStartTime, "s"
            print "found results:", donateTypeRetVal
            if donateTypeRetVal:
                if True in donateTypeRetVal[0:5]:
                    donatetype = 4
                elif True in donateTypeRetVal[5:]:
                    donatetype = 2
            #test
            #can donate
            if donatetype > 0:
                print "donatetype is", donatetype
                #avoid donate image move due to new chat
                if d.exists(Pattern("1404875979174.png").similar(0.90),0):
                    click (d)
                elif d.below(50).exists("1404875979174.png",0):
                    newd = d.below(50).find("1404875979174.png")
                    click (newd)
                    d = newd
                sleep(0.5)#wait for donate dialog to show up
                donateTroops(d, donatetype)
    Settings.MoveMouseDelay = mmd # reset to original value
        
   
#https://answers.launchpad.net/sikuli/+faq/1731
def donateTypeNew(imgs, first = False, reg = None):
   if not reg: reg = SCREEN
   res = [False for img in imgs]
   for i in range(len(imgs)):
       if reg.exists(imgs[i], 0):
           res[i] = True
           if first: return res
       if True in res: return res
   return None # nothing found within time 

def donateTroops(d, donatetype):
    donateTroopsPannelRegion = Region(d.x + 68, d.y - 117, 505, 285)
    #donateTroopsPannelRegion.highlight(1)
    donateMatchImg = ["1405058824552.png", "1405004776299.png", "1405058846435.png", "1405058867849.png", "1405058887125.png"]

    startTime = time.time()
    while donateTroopsPannelRegion.exists(donateMatchImg[donatetype-1],0):
        hover(donateTroopsPannelRegion.getLastMatch())
        mouseDown(Button.LEFT)
        print "donatetype", donatetype, "donated!"
        #connection lost
        if time.time() - startTime > 10:
            reloadGame(cocRegion)
    mouseUp(Button.RIGHT)

    donateTroopsPannelCloseRegion = Region(d.x +  523, d.y - 91, 26, 26)
    donateTroopsPannelCloseRegion.highlight(1)
    if donateTroopsPannelCloseRegion.exists("1405323529373.png",0):
        click(donateTroopsPannelCloseRegion.getLastMatch())

def sidebarToTop(Reg):
    if Reg.exists("1404956625662.png",0):
     click(Reg.getLastMatch())


def reloadGame(Reg):
    dialogRegion = Region(Reg.x + 255, Reg.y + 225, 555, 157)
    if dialogRegion.exists("1405043079549.png",0):
        click("1405043089333.png")
        sleep(3)
        trophyRegion = Region(Reg.x + 8, Reg.y + 93, 50, 50)
        wait("1405043219918.png", 30)
        mapCentered = False
        print "game reloaded from idle!", time.time() - loopStart       
    elif dialogRegion.exists("1405052462366.png",0):
        click("1405052476880.png")
        sleep(3)
        trophyRegion = Region(Reg.x + 8, Reg.y + 93, 50, 50)
        wait("1405043219918.png", 30)
        mapCentered = False
        print "game reloaded from connection lost!", time.time() - loopStart       
    elif dialogRegion.exists("1405390862071.png",0):
        click("1405052476880.png")
        sleep(3)
        trophyRegion = Region(Reg.x + 8, Reg.y + 93, 50, 50)
        wait("1405043219918.png", 30)
        print "game reloaded from login failed!", time.time() - loopStart  
    elif dialogRegion.exists("1405491920221.png",0):
        while dialogRegion.exists("1405491920221.png"):
            sleep(30)        
            click("1405491933067.png")
            mapCentered = False
        trophyRegion = Region(Reg.x + 8, Reg.y + 93, 50, 50)
        wait("1405043219918.png", 30)
        print "game reloaded from take a break!", time.time() - loopStart  
def blockAppWindowToQuit(Reg):
    appIconRegion = Region(Reg.x - 20, Reg. y - 20 , 50, 50)
    #appIconRegion.highlight(1)
    if not appIconRegion.exists("1405048905914.png"):
        exit(0)

def reloadGameFallback(Reg):
    if loop % 10 == 0:
        click(Location(cocRegion.x + 1064, cocRegion.y + 290))


def centerMap():
    closeSiderBar() # otherwise sidebar will move

    #zoom in max
    for x in range(0,4):
        type( '-' , KEY_CTRL )
        sleep(0.1)
    if cocRegion.exists(Pattern("1405090403276.png").similar(0.60),0):
        stone =  cocRegion.getLastMatch()
        #print stone
        dragDrop(stone.getCenter(), Location(cocRegion.x + 150, cocRegion.y + 400))
    
    mapCentered = True
        
def buildTroops():
    pass

def connectionLost():
    pass

def loginFailed():
    pass

def availableLoot():
    moneyLootReg = Region(cocRegion.x + 45 ,cocRegion.y + 82, 65, 17)
    elixirLootReg = Region(cocRegion.x + 45 ,cocRegion.y + 107, 65, 17)
    darkElixirLootReg = Region(cocRegion.x + 45 ,cocRegion.y + 131, 65, 17)
    #moneyLootReg.highlight(1)
    #elixirLootReg.highlight(1)    
    #darkElixirLootReg.highlight(1)    
    availableMoney = numberOCR(moneyLootReg)
    availableElixir = numberOCR(elixirLootReg)    
    availableDarkElixir = numberOCR(darkElixirLootReg)
    #print availableMoney, availableElixir, availableDarkElixir
    return availableMoney, availableElixir, availableDarkElixir

def numberOCR(Reg):
    numberImages = ["1405312945137.png","n1.png","1405310129098.png","1405310109194.png","1405309941282.png","1405310662779.png","1405310613718.png","1405310652149.png","1405310601618.png","1405310585463.png"]
    #find digital images
    digitalNumber = 0 #digital number
    resultList = list()
    t1 = time.time()
    Reg.highlight(1)
    for x in numberImages:
        if Reg.exists(x,0):
            Reg.findAll(x)
            #digital find result into list            
            digitalList = list(Reg.getLastMatches())
            #convert list into tuple(image, digital)
            for y in digitalList:
                #resultList.append(tuple(y,0))
                t = (y,digitalNumber)
                resultList.append(t)
        digitalNumber = digitalNumber+1        
    sortedResultList = sorted(resultList,key=lambda x: x[0].x)
    #print sortedResultList
    ret = 0
    listLen = len(sortedResultList)
    for x, i in enumerate(sortedResultList):
        ret += 10 **(listLen - x - 1) * i[1]
    return ret

def beginAttack():
    closeSiderBar()
    attackReg = Region(cocRegion.x + 14 ,cocRegion.y + 480, 90, 90) 
    if attackReg.exists("1405497859508.png",1):
        click(attackReg.getLastMatch())
    #else:
    
    findAMatchReg = Region(cocRegion.x + 100 ,cocRegion.y + 400, 170, 85) 
    
    if findAMatchReg.exists("1405497468202.png",3):
        click(findAMatchReg.getLastMatch())

    searchTimer = 20
    while searchTimer != 0:
        searchTimer = searchTimer -1
        searchTimer = searchFish(searchTimer)
        print "searchTimer", searchTimer

def searchFish(searchTimer):
    endBattleRegion = Region(cocRegion.x + 16, cocRegion.y + 431, 100, 35)    
    findNextRegion = Region(cocRegion.x + 917, cocRegion.y + 396, 70, 70)    
    endBattleRegion.exists("1405498017741.png", 15)
    endBattleRegion.getLastMatch().highlight(3)    
    loot =  availableLoot()
    findNext = True
    if resourceLimitType == "or":
        if moneyLimit != 0:
            if loot[0] >= moneyLimit:
                sendTroops()
                findNext = False
        if elixirLimit != 0 and findNext:
            if loot[1] >= elixirLimit:
                sendTroops()
                findNext = False
        if darkElixirLimit != 0 and findNext:
            if loot[2] >= darkElixirLimit:
                sendTroops() 
                findNext = False    
    elif resourceLimitType == "and":
        if (moneyLimit - loot[0])* moneyLimit <= 0:
            if (elixirLimit - loot[0])* elixirLimit <= 0:
                if (darkElixirLimit - loot[0])* darkElixirLimit <= 0:
                    sendTroops() 
                    findNext = False    

    
    #no find a suiteable fish
    if findNext == True:
        if findNextRegion.exists("1405503842861.png",1):
            #findNextRegion.highlight(1) 
            click(findNextRegion.getLastMatch())
            sleep(1)
    else:
        searchTimer = 0
    return searchTimer


def sendTroops():
   popup("FISH!") 
    #attackPattern1()


def attackPatten1():
    deployPoints = [Location(cocRegion.x + 216, cocRegion.y + 463),
            Location(cocRegion.x + 217, cocRegion.y + 446),
            Location(cocRegion.x + 139, cocRegion.y + 392),
            Location(cocRegion.x + 128, cocRegion.y + 268),
            Location(cocRegion.x + 188, cocRegion.y + 222),
            Location(cocRegion.x + 260, cocRegion.y + 165),
            Location(cocRegion.x + 946, cocRegion.y + 265),
            Location(cocRegion.x + 914, cocRegion.y + 235),
            Location(cocRegion.x + 802, cocRegion.y + 151),
            Location(cocRegion.x + 839, cocRegion.y + 469),
            Location(cocRegion.x + 942, cocRegion.y + 406),
            Location(cocRegion.x + 1000, cocRegion.y + 341)]
    troopsRegion = Region(cocRegion.x + 200, cocRegion.y + 483, 600, 74)        
    troopsRegion.highlight(1)
    while troopsRegion.exists("1405581483191.png"):
        click(troopsRegion.getLastMatch())
        for x in deployPoints:
            click(x)
    while troopsRegion.exists("1405581789516.png"):
        click(troopsRegion.getLastMatch())
        for x in deployPoints:
            click(x)
    while troopsRegion.exists("1405581812872.png"):
        click(troopsRegion.getLastMatch())
        for x in deployPoints:
            click(x)
    while troopsRegion.exists("1405581827297.png"):
        click(troopsRegion.getLastMatch())
        for x in deployPoints:
            click(x)
##    while troopsRegion.exists("1405581483191.png"):
#        click(troopsRegion.getLastMatch())
#        for x in deployPoints:
#            click(x)
            
        


def trainTroops():
    
    click(Location(cocRegion.x + 1064, cocRegion.y + 290))
    if not mapCentered:
        centerMap()
    #avoid build selection text block barracks
    trainTroopsIconRegion = Region(cocRegion.x + 584, cocRegion.y + 483, 68, 68)    
    trainBarbarianRegion = Region(cocRegion.x + 312, cocRegion.y + 248, 90, 90)        
    trainArcherianRegion = trainBarbarianRegion.right(90)
    trainGoblinRegion = trainArcherianRegion.right(90)    
    trainGiantRegion = trainGoblinRegion.right(90)    
    trainWBRegion = trainGiantRegion.right(90)   
    #......

    if cocRegion.exists(Pattern("1405577695617.png").similar(0.60), 0) and not trainTroopsIconRegion.exists("1405566641801.png", 0):
        click(cocRegion.getLastMatch())
    if trainTroopsIconRegion.exists("1405566641801.png", 1):
        click(trainTroopsIconRegion.getLastMatch())
        trainBarbarianRegion.wait("1405567702748.png")
        #barracks #1
        g = trainGiantRegion
        if trainGiantRegion.exists("1405578421081.png"):
            hover(trainGiantRegion.getLastMatch())
            mouseDown(Button.LEFT)
            sleep(3)
            mouseUp(Button.LEFT)
        sleep(1)
        click(Location(cocRegion.x + 827, cocRegion.y + 310))
        #barracks #2
        if trainWBRegion.exists("1405578455807.png"):
            hover(trainWBRegion.getLastMatch())
            mouseDown(Button.LEFT)
            sleep(1)
            mouseUp(Button.LEFT)              
        if trainGoblinRegion.exists("1405577880629.png"):
            hover(trainGoblinRegion.getLastMatch())
            mouseDown(Button.LEFT)
            sleep(2)
            mouseUp(Button.LEFT)
      
        sleep(1)
        click(Location(cocRegion.x + 827, cocRegion.y + 310))            
        #barracks #3
        if trainBarbarianRegion.exists("1405578393272.png"):
            hover(trainBarbarianRegion.getLastMatch())
            mouseDown(Button.LEFT)
            sleep(3)
            mouseUp(Button.LEFT)
        sleep(1)
        click(Location(cocRegion.x + 827, cocRegion.y + 310))            
        #barracks #4
        if trainArcherianRegion.exists("1405578407858.png"):
            hover(trainArcherianRegion.getLastMatch())
            mouseDown(Button.LEFT)
            sleep(3)
            mouseUp(Button.LEFT)
        trainTroopsPannelCloseRegion = Region(cocRegion.x + 777, cocRegion.y + 124, 42, 42)
        trainTroopsPannelCloseRegion.highlight(1)
        if trainTroopsPannelCloseRegion.exists("1405579252006.png",0):
            click(trainTroopsPannelCloseRegion.getLastMatch())

        
######################## Main Loop #######################
#startCOC()
#set Regtions

cocRegion = App("Bluestacks").window(0)
sidebarRegion = Region(cocRegion.x + 2, cocRegion.y + 128, 270, cocRegion.h - 175)


#debug parameters:
loop = 10000
loopSleepTime = 3

#global settings
setShowActions(True)
Settings.MinSimilarity = 0.8
Settings.MoveMouseDelay = 0
setFindFailedResponse(SKIP)
moneyLimit = 200000
elixirLimit = 0
darkElixirLimit = 0
resourceLimitType = "or"
loopStart = time.time()
mapCentered = False

for n in range(loop):
    loopStart = time.time()
    
    reloadGame(cocRegion)
    
    openSiderBar()
    
    sidebarToTop(sidebarRegion)
    
    openDonateDialog(sidebarRegion)
    
    closeSiderBar()
    
    sleep(loopSleepTime)

    blockAppWindowToQuit(cocRegion)
    
    reloadGameFallback(cocRegion)
    
    print "Time used in this loop:[", n, "]", time.time() - loopStart

#attackPatten1()
#centerMap()
#trainTroops()
beginAttack()
