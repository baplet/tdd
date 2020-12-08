from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance(self, b: 'Point'):
        return 0