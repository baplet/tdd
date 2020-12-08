class Scorer:

    def __init__(self):
        self.score = 0

    def getScore(self):
        return self.score
    
    def do_shoot(self, shoot):
        self.score = self.score + shoot