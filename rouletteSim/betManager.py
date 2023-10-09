from bet import Bet
import config
import exceptions

class BetManager:

    def __init__(self, bets=[]):
        self.bets = bets


    def __str__(self):
        outString = ""
        for x in self.bets:
            outString += str(x) + "\n"
        
        return outString
    
    def checkValidBetArgs(betNumbers: [], numBetNums: int, tag: str) -> None:
        if betNumbers not in config.ROULETTE_OUTCOMES.keys() or len(betNumbers) != numBetNums:
            raise exceptions.InvalidBetNumbers("f{betNumbers} is invalid for a {tag} bet")
        
    
    def checkBetAmount(betAmount: int) -> None:
        if betAmount < 1:
            raise exceptions.InvalidBetAmount("f{betAmount} is in invalud bet amount.")
        
    

    # function to create a single Bet
    def makeSingle(self, betNumbers: [], betAmount) -> None:
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
    def makeStreet(self, betNumbers: [], betAmount) -> None:
        self.checkValidBetArgs(betNumbers, 3, "straight")
        self.checkBetAmount(betAmount)
        
        #TODO - check for valid triples

        self.bets.append(Bet(betNumbers, "street", 11, betAmount))


    # function to make a corner Bet
    def makeCorner(self, betNumbers: [], betAmount) -> None:
        self.checkValidBetArgs(betNumbers, 4, "corner")
        self.checkBetAmount(betAmount)
            
        #TODO - check for valid groups of four

        self.bets.append(Bet(betNumbers, "corner", 11, betAmount))

    # function to make five number Bet
    def fiveNumber(self, betAmount) -> None:
        self.checkBetAmount(betAmount)
        self.bets.append(Bet(["0", "00", "1", "2", "3"], "five-number", 6, betAmount))

