import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls_drawn):
        balls_drawn = []
        if num_balls_drawn > len(self.contents):
            return self.contents
        for _ in range(num_balls_drawn):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**Counter(hat.contents))
        balls_drawn = hat_copy.draw(num_balls_drawn)
        if all(balls_drawn.count(color) >= count for color, count in expected_balls.items()):
            count += 1
    return count / num_experiments
