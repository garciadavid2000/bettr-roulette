from bet import Bet
import config
import exceptions

class BetManager:

    def __init__(self):
        self.bets = []


    def __str__(self):

        if len(self.bets) == 0:
            return "There are no bets placed"

        outString = ""
        for x in self.bets:
            outString += str(x) + "\n"
        
        return outString
    

    def getBetManagerPayout(self, rouletteOutcome: str) -> int:
        netPayout = 0

        for x in self.bets:
            netPayout += x.getBetPayout(rouletteOutcome)
        
        return netPayout
    

    # function to increment ALL bets that cover specific value by some amount
    def incrementBetVal(self, val: str, amount: int) -> None:
        for x in self.bets:
            if x.coversValue(val):
                x.increaseBetAmount(amount)
    

    def checkValidBetArgs(self, betNumbers: [], numBetNums: int, tag: str) -> None:
        if betNumbers not in config.ROULETTE_OUTCOMES.keys() or len(betNumbers) != numBetNums:
            raise exceptions.InvalidBetNumbers(f"{betNumbers} is invalid for a {tag} bet")
        
    
    def checkBetAmount(self, betAmount: int) -> None:
        if betAmount < 1:
            raise exceptions.InvalidBetAmount(f"{betAmount} is an invalud bet amount.")
        
    
    def checkSelectionValue(self, selectionVal: int, validValues: []) -> None:
        if selectionVal not in validValues:
            raise exceptions.InvalidSelectionValue(f"{selectionVal} is an invalid value for selection.")
        
    

    # function to create a single Bet
    def makeSingle(self, betNumbers: [], betAmount:int) -> None:
        self.checkValidBetArgs(betNumbers, 1, "single")
        self.checkBetAmount(betAmount)
        self.bets.append(Bet([betNumbers], "single", 35, betAmount))


    # function to make a split Bet
    def makeSplit(self, betNumbers: [], betAmount) -> None:
        self.checkValidBetArgs(betNumbers, 2, "split")
        self.checkBetAmount(betAmount)

        #TODO - check for valid pairs

        self.bets.append(Bet(betNumbers, "split", 17, betAmount))


    # function to make a street Bet
    def makeStreet(self, betNumbers: [], betAmount:int) -> None:
        self.checkValidBetArgs(betNumbers, 3, "straight")
        self.checkBetAmount(betAmount)
        
        #TODO - check for valid triples

        self.bets.append(Bet(betNumbers, "street", 11, betAmount))


    # function to make a corner Bet
    def makeCorner(self, selectionVal: int, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.checkSelectionValue(selectionVal, config.VALID_CORNER_VALS)
            
        #TODO - check for valid groups of four
        betVals = []
        for i in range(2):
            betVals.append(selectionVal+i)
            betVals.append(selectionVal+3+i)

        self.bets.append(Bet([str(i) for i in betVals], "corner", 8, betAmount))


    # function to make five number Bet
    def makeFiveNumber(self, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.bets.append(Bet(["0", "00", "1", "2", "3"], "five-number", 6, betAmount))


    # function to make line bet given bottom left value of the coverage values
    def makeLine(self, selectionVal: int, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.checkSelectionValue(selectionVal, config.VALID_LINE_VALS)

        betVals = []
        for i in range(3):
            betVals.append(selectionVal+i)
            betVals.append(selectionVal+3+i)
        
        self.bets.append(Bet([str(i) for i in betVals], "line", 5, betAmount))

    
    # function to make dozen Bet
    def makeDozen(self, selectionVal:int, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.checkSelectionValue(selectionVal, config.VALID_ROWCOL_VALS)
       
        if selectionVal == 1:
            self.bets.append(Bet([str(i) for i in range(1, 13)], "dozen", 2, betAmount))
        
        elif selectionVal == 2:
            self.bets.append(Bet([str(i) for i in range(13, 25)], "dozen", 2, betAmount))

        elif selectionVal == 3:
            self.bets.append(Bet([str(i) for i in range(25, 37)], "dozen", 2, betAmount))


    # function to make row Bet
    def makeRow(self, selectionVal:int, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.checkSelectionValue(selectionVal, config.VALID_ROWCOL_VALS)
        
        if selectionVal == 1:
            self.bets.append(Bet([str(i) for i in range(1, 35, 3)], "row", 2, betAmount))
        
        elif selectionVal == 2:
            self.bets.append(Bet([str(i) for i in range(2, 36, 3)], "row", 2, betAmount))

        elif selectionVal == 3:
            self.bets.append(Bet([str(i) for i in range(3, 37, 3)], "row", 2, betAmount))


    # function to make even-odd Bet
    def makeEvenOdd(self, even:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount, ["1", "2", "3"])

        if even:
            self.bets.append(Bet([str(i) for i in range(2, 37, 2)], "even", 1, betAmount))
        else:
            self.bets.append(Bet([str(i) for i in range(1, 37, 2)], "odd", 1, betAmount))


    # function to make red-black Bet
    def makeRedBlack(self, red:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount)

        if red:
            self.bets.append(Bet([i for i in config.ROULETTE_OUTCOMES.keys() if config.ROULETTE_OUTCOMES.get(i) == "red"], "red", 1, betAmount))
        else:
            self.bets.append(Bet([i for i in config.ROULETTE_OUTCOMES.keys() if config.ROULETTE_OUTCOMES.get(i) == "black"], "black", 1, betAmount))


    # function to make high-low Bet
    def makeHighLow(self, high:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount)

        if high:
            self.bets.append(Bet([str(i) for i in range(19, 37)], "high", 1, betAmount))
        else:
            self.bets.append(Bet([str(i) for i in range(1, 19)], "low", 1, betAmount))




#TODO - remove test code


# code for testing
'''
bub = BetManager()
bub.makeRedBlack(False, 30)
bub.makeHighLow(False, 40)
bub.makeLine(10, 50)
bub.makeCorner(31, 100)
bub.makeCorner(2, 150)

print(bub)

print(bub.getBetManagerPayout("00"))
print(bub.getBetManagerPayout("2"))
'''