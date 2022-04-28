class Score:
    nominalScore = 0    # usually 501
    currentScore = 0

    doubleOut = True    # if you want to play with Double-Out at the end or not
    finished = False    # if the score is 0 and the game is finished


    def __init__(self, nominalScore, doubleOut):
        self.nominalScore = nominalScore
        self.currentScore = nominalScore
        self.doubleOut = doubleOut


    def setNominalScore(self, points):
        self.nominalScore = points


    def getCurrentScore(self):
        return self.currentScore


    def setCurrentScore(self, points):
        self.currentScore = points


    # Subtract the scored points from the current score and check, if the game is finished.
    def pointsScored(self, points, hitDouble):
        if self.doubleOut:
            if ((self.currentScore - points) >= 2):
                self.currentScore -= points
            else:
                if hitDouble:
                    if ((self.currentScore - points) == 0):
                        self.currentScore -= points
                    else:
                        print("Overthrown! You have only " + str(self.currentScore) + " points left!")
                else:
                    print("You cannot finish without hitting a Double!")
        else:
            if ((self.currentScore - points) >= 0):
                self.currentScore -= points
            else:
                print("Overthrown! You have only " + str(self.currentScore) + " points left!")

        # Check, if the player has won the game
        if self.currentScore == 0:
            finished = True
            print("Congratulations!!! You won the game!")


    # Calculate the thrown points and check, if a double field was hit.
    # The inputs are directly the fields, which were hit.
    def calculatePoints(self, firstThrow, firstMultiplier, secondThrow, secondMultiplier, thirdThrow, thirdMultiplier):
        if (0 <= firstThrow <= 20) and (0 <= secondThrow <= 20) and (0 <= thirdThrow <= 20):
            if (1 <= firstMultiplier <= 3) and (1 <= secondMultiplier <= 3) and (1 <= thirdMultiplier <= 3):
                hitDouble = False
                if (firstMultiplier == 2) or (secondMultiplier == 2) or (thirdMultiplier == 2):
                    hitDouble = True
                return firstThrow * firstMultiplier + secondThrow * secondMultiplier + thirdThrow * thirdMultiplier, hitDouble
        print("Invalid Throw! Could not calculate the points.")