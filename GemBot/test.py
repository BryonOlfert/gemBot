exec(open("combinations.py").read())
exec(open("functions.py").read())
exec(open("builds.py").read())
exec(open("gemBuilds.py").read())
exec(open("centerBuilds1p.py").read())

blah = ["p1","r1","r1","r1","r1 "]

#gemBuilds = what we need

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

def main():
    for each in buildables(blah):
        print(each)

main()


