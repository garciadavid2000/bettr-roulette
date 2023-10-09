

class Bet:
    betVals = []
    tag = ""
    payout = 0
    betAmount = 0

    def init(self, bv, t,  p, ba):
        self.betVals = bv
        self.tag = t
        self.payout = p
        self.betAmount = ba

    def str(self):
        return f"bet vals: {self.betVals}, payout: {self.payout}, bet amount: {self.betAmount}"

    def getPayout(self, rv):
        payoutValue = self.payout*self.betAmount
        return payoutValue + self.betAmount if rv in self.betVals else -self.betAmount
