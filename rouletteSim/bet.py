class Bet:

    def __init__(self, betNumbers=[], betType: str="",  payout: int=0, betAmount: int=0):
        self.betNumbers = betNumbers
        self.betType = betType
        self.payout = payout
        self.betAmount = betAmount

    def __str__(self):
        return f"bet numbers: {self.betNumbers}, payout: {self.payout}:1, bet amount: ${self.betAmount}"


    # Get payout of Bet given the outcome of the roulette wheel
    def getPayout(self, rouletteOutcome: str) -> int:
        payoutValue = self.payout*self.betAmount
        return payoutValue + self.betAmount if rouletteOutcome in self.betNumbers else -self.betAmount


    # Check if a Bet covers a specific outcome
    def coversValue(self, rouletteValue: str)-> bool:
        return True if rouletteValue in self.betNumbers else False

    # Getters
    def getBetNumbers(self):
        return self.betNumbers

    def getBetType(self) -> str:
        return self.betType

    def getPayout(self) -> int:
        return self.payout

    def getBetAmount(self) -> int:
        return self.betAmount
    
    # Setters
    def setBetAmount(self, betAmount):
        self.betAmount = betAmount\

    