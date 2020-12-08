from bowling import Scorer

class Test:
    def setup_method(self):
        self.scorer = Scorer()
    
    def teardown_method(self):
        del self.scorer

    def test_getScore_null(self):
        assert self.scorer.getScore() == 0

    def test_getScore_1_shoot(self):
        shoot = 5
        self.scorer.do_shoot(shoot)

        assert self.scorer.getScore() == shoot
    
    def test_getScore_2_shoot(self):
        shoot1 = 5
        self.scorer.do_shoot(shoot1)

        shoot2 = 3
        self.scorer.do_shoot(shoot2)

        assert self.scorer.getScore() == shoot1 + shoot2