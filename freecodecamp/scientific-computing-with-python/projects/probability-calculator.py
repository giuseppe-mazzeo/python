import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, n_balls_draw):
        if n_balls_draw >= len(self.contents):
            draw = copy.deepcopy(self.contents)
            self.contents.clear()
            return draw

        draw = []
        for _ in range(n_balls_draw):
            ball = random.choice(self.contents)
            draw.append(ball)
            self.contents.remove(ball)
        return draw  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    n = num_experiments

    while n > 0:
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        dic_draw = {x: draw.count(x) for x in draw}
        
        if all(dic_draw.get(ball, 0) >= quant for ball, quant in expected_balls.items()):
            success += 1

        n -= 1

    return (success / num_experiments)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
