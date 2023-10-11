from betManager import BetManager

class Simulation:
    
    def __init__(self, startingBet: BetManager = BetManager()):
        self.bet = startingBet
    

    def __str__(self):
        return str(self.bet)

    def getNetPayout(self, rouletteOutcome: str) -> int:
        return self.bet.getBetManagerPayout(rouletteOutcome)
    




testBet = BetManager()
testBet.makeCorner(2, 300)
testBet.makeRedBlack(True, 20)
testBet.makeSingle("4", 5)

#testBet.incrementBetVal("3", 15)

testSim = Simulation(testBet)
testSim2 = Simulation()

print(testSim)
print(testSim2)



print(testSim.getNetPayout("3"))
print(testSim2.getNetPayout("00"))
