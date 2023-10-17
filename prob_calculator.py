import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        num_balls = min(num_balls_to_draw, len(self.contents))
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_success = 0

    for _ in range(num_experiments):
        hat_copy = Hat()
        drawn_balls = hat_copy.draw(num_balls_drawn)
        ball_count = {}
        for ball in drawn_balls:
            ball_count[ball] = ball_count.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if color not in ball_count or ball_count[color] < count:
                success = False
                break

        if success:
            count_success += 1

    probability = count_success / num_experiments
    return probability
