class Scorer:

    def __init__(self):
        self.score = 0
        self.scoreList = []

    def getScore(self):
        return self.score
    
    def do_shoot(self, shoot):
        self.scoreList.append(shoot)
        self._evaluateScore(shoot)

    def _evaluateScore(self, shoot):
        if len(self.scoreList) > 2:
            if self.scoreList[-2] + self.scoreList[-3] == 10:
                self.score = self.score + shoot
        self.score = self.score + shoot

    