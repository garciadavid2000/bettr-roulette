class Bet:

    def __init__(self, betNumbers=[], betType: str="",  payout: int=0, betAmount: int=0):
        self.betVals = betNumbers
        self.betType = betType
        self.payout = payout
        self.betAmount = betAmount

    def __str__(self):
        return f"bet vals: {self.betVals}, payout: {self.payout}, bet amount: {self.betAmount}"

    def getPayout(self, rouletteOutcome: str) -> int:
        payoutValue = self.payout*self.betAmount
        return payoutValue + self.betAmount if rouletteOutcome in self.betVals else -self.betAmount
