class Scorer:

    def __init__(self):
        self.score = 0
        self.num_shoot = 0
        self.scoreList = []

    def getScore(self):
        return self.score
    
    def do_shoot(self, shoot):
        self.num_shoot = self.num_shoot + 1
        self.scoreList.append(shoot)
        self._evaluateScore(shoot)

    def _evaluateScore(self, shoot):
        if self.num_shoot == 1:
            self.evaluate_spare_bonus(shoot)
            if shoot == 10:
                self.num_shoot = 0
        elif self.num_shoot == 2:
            self.num_shoot = 0
            if self.previous_frame_was_strike():
                self.score = self.score + self.scoreList[-2] + shoot
        self.score = self.score + shoot

    def evaluate_spare_bonus(self, shoot):
        if self.previous_frame_was_spare():
            self.score = self.score + shoot

    def previous_frame_was_spare(self):
        return len(self.scoreList) > 2 and self.scoreList[-2] + self.scoreList[-3] == 10
    
    def previous_frame_was_strike(self):
        return len(self.scoreList) > 2 and self.scoreList[-3] == 10

    