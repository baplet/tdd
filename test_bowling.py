from bowling import Scorer

class Test:
    def setup_method(self):
        self.scorer = Scorer()
    
    def teardown_method(self):
        del self.scorer

    def test_getScore_null(self):
        assert self.scorer.getScore() == 0

    def test_getScore_shoot(self):
        shoot = 5
        self.scorer.do_shoot(shoot)

        assert self.scorer.getScore() == shoot