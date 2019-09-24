stepCounter: int = 0
lifeCounter = 3
combination = "SSNWES"

play = True


class LosingLife:
    if stepCounter == 10:
        lifeCounter - 1
        stepCounter = 0


class LifeChecker:
    if lifeCounter == 0:
        play = False
        print("You have lost, please try again")


while play:
    print("You are in the magic maze. Which way to go? (N,S,E,W)")
    if input() == "S":
        print("you may continue")
        stepCounter+1
        LifeChecker
        if input() == "S":
            print("well done, you may continue")
            stepCounter + 1
            LifeChecker
            if input() == "N":
                print("well done, you may continue")
                stepCounter + 1
                LifeChecker
                if input() == "W":
                    print("well done, you may continue")
                    stepCounter + 1
                    LifeChecker
                    if input() == "E":
                        print("well done, you may continue")
                        stepCounter + 1
                        LifeChecker
                        if input() == "S":
                            stepCounter + 1
                            LifeChecker
                            print("well done, you have escaped the maze, you may leave")
                            print(stepCounter)
                            play = False

                        else:
                            print("wrong move")
                            stepCounter + 1
                            LifeChecker
                    else:
                        print("wrong move")
                        stepCounter + 1
                        LifeChecker
                else:
                    print("wrong move")
                    stepCounter + 1
                    LifeChecker
            else:
                print("wrong move")
                stepCounter+1
                LifeChecker
        else:
            print("wrong move")
            stepCounter + 1
            LifeChecker

    else :
        print("wrong move")
        stepCounter + 1
        LifeChecker