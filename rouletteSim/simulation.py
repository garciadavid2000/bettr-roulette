from betManager import BetManager
import config
import random

class Simulation:
    
    def __init__(self, startingBet = BetManager()):
        self.bets = startingBet
    

    def __str__(self):
        return str(self.bets)

    def spinWheel(self):
        return random.choice(list(config.ROULETTE_OUTCOMES.keys()))

    def getNetPayout(self, rouletteOutcome: str) -> int:
        return self.bets.getBetManagerPayout(rouletteOutcome)
    




testBet = BetManager()
testBet.makeCorner(2, 300)
testBet.makeRedBlack(True, 20)
testBet.makeSingle("4", 5)

testBet.incrementBetVal("3", 15)

testSim = Simulation(testBet)
testSim2 = Simulation()


print("=============================")
print(testSim)
print("=============================")
print(testSim2)



print(testSim.getNetPayout("3"))
print(testSim2.getNetPayout("00"))

for i in range(10):
    print(testSim.getNetPayout(testSim.spinWheel()))
