import math
import random


def approximate_pi():
    total_points = 0
    within_circle = 0

    for i in range(100001):
        x = random.random()
        y = random.random()
        total_points += 1
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance < 1:
            within_circle += 1
            if total_points % 1000 == 0:
                pi_estimate = 4 * within_circle / total_points
                if total_points == 100000:
                    return pi_estimate
                else:
                    yield pi_estimate


if __name__ == '__main__':
    estimates = [estimate for estimate in approximate_pi()]
    errors = [estimate - math.pi for estimate in estimates]
    print(estimates)
    print(errors)
