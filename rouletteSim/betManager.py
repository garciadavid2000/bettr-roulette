from bet import Bet
import config
import exceptions

class BetManager:

    def __init__(self, bets: [] = []):
        self.bets = bets


    def __str__(self):
        outString = ""
        for x in self.bets:
            outString += str(x) + "\n"
        
        return outString
    
    def checkValidBetArgs(self, betNumbers: [], numBetNums: int, tag: str) -> None:
        if betNumbers not in config.ROULETTE_OUTCOMES.keys() or len(betNumbers) != numBetNums:
            raise exceptions.InvalidBetNumbers("f{betNumbers} is invalid for a {tag} bet")
        
    
    def checkBetAmount(self, betAmount: int) -> None:
        if betAmount < 1:
            raise exceptions.InvalidBetAmount("f{betAmount} is in invalud bet amount.")
        
    

    # function to create a single Bet
    def makeSingle(self, betNumbers: [], betAmount:int) -> None:
        self.checkValidBetArgs(betNumbers, 1, "single")
        self.checkBetAmount(betAmount)
        self.bets.append(Bet(betNumbers, "single", 35, betAmount))


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
    def makeCorner(self, betNumbers: [], betAmount:int) -> None:
        self.checkValidBetArgs(betNumbers, 4, "corner")
        self.checkBetAmount(betAmount)
            
        #TODO - check for valid groups of four

        self.bets.append(Bet(betNumbers, "corner", 11, betAmount))

    # function to make five number Bet
    def fiveNumber(self, betAmount:int) -> None:
        self.checkBetAmount(betAmount)
        self.bets.append(Bet(["0", "00", "1", "2", "3"], "five-number", 6, betAmount))


    #TODO - make function for line Bet
    

    # function to make dozen Bet
    def dozen(self, dozenVal:int, betAmount:int) -> None:
        self.checkBetAmount(betAmount)

        #TODO - check valid dozenVal in [1,2,3]

        if dozenVal == 1:
            self.bets.append(Bet([str(i) for i in range(1, 13)], "dozen", 2, betAmount))
        
        elif dozenVal == 2:
            self.bets.append(Bet([str(i) for i in range(13, 25)], "dozen", 2, betAmount))

        elif dozenVal == 3:
            self.bets.append(Bet([str(i) for i in range(25, 37)], "dozen", 2, betAmount))


    # function to make even-odd Bet
    def evenOdd(self, even:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount)
        if even:
            self.bets.append(Bet([str(i) for i in range(2, 37, 2)], "even", 1, betAmount))
        
        else:
            self.bets.append(Bet([str(i) for i in range(1, 37, 2)], "odd", 1, betAmount))



    # function to make red-black Bet
    def redBlack(self, red:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount)
        if red:
            self.bets.append(Bet([i for i in config.ROULETTE_OUTCOMES.keys() if config.ROULETTE_OUTCOMES.get(i) == "red"], "red", 1, betAmount))
        
        else:
            self.bets.append(Bet([i for i in config.ROULETTE_OUTCOMES.keys() if config.ROULETTE_OUTCOMES.get(i) == "black"], "black", 1, betAmount))


    # function to make high-low Bet
    def highLow(self, high:bool, betAmount: int) -> None:
        self.checkBetAmount(betAmount)
        if high:
            self.bets.append(Bet([str(i) for i in range(19, 37)], "high", 1, betAmount))
        
        else:
            self.bets.append(Bet([str(i) for i in range(1, 19)], "low", 1, betAmount))





bub = BetManager()
bub.redBlack(False, 30)
print(bub)
