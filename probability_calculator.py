import copy
import random

class Hat:
    def __init__(self, **hat):
        self.contents = []
        [[self.contents.append(color) for _ in range(0, num)] for color, num in hat.items()]

    def draw(self, num):
        out = copy.copy(self.contents) if num > len(self.contents) else []
        if out == self.contents:
            self.contents = []
            return out

        for _ in range(0, num):
            ball = random.choice(self.contents)
            out.append(ball)
            self.contents.remove(ball)

        return out

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    times = 0

    for _ in range(0, num_experiments):
        newsort = copy.deepcopy(hat)
        sort = newsort.draw(num_balls_drawn)

        match = {color:0 for color in sort}
        for ball in sort:
            if ball in match:
                match[ball] += 1
            else:
                pass
        is_true = []
        for z in expected_balls:
            if z in match:
                is_true.append(match[z] >= expected_balls[z])
            else:
                pass

        if len(is_true) == len(expected_balls.items()) and all(is_true):
            times += 1
        else:
            pass
                              
    return round(times / num_experiments, 3)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)