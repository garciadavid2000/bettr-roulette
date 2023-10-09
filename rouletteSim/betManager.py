from bet import Bet


class BetManager:

    def __init__(self, bets=[]):
        self.bets = bets


    def __str__(self):
        outString = ""
        for x in self.bets:
            outString += str(x)
        
        return outString

