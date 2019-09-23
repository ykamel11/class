stepCounter = 0
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
        if input() == "S":
            print("well done, you may continue")
            if input() == "N":
                print("well done, you may continue")
                if input() == "W":
                    print("well done, you may continue")
                    if input() == "E":
                        print("well done, you may continue")
                        if input() == "S":
                            print("well done, you have escaped the maze, you may leave")
                            play = False

                        else:
                            print("wrong move")
                    else:
                        print("wrong move")
                else:
                    print("wrong move")
            else:
                print("wrong move")
        else:
            print("wrong move")

    else :
        print("wrong move")


