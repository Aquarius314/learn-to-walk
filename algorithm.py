
class Algorithm:

    def __init__(self):
        self.iterations = 0

    def calculate(self, world):
        self.iterations += 1
        dists = []
        for model in world.models:
            model.move(world.ground_line)
            dists.append(model.get_distance())
        if self.iterations%100 == 0:
            print("Best distance:", max(dists), " iters:", self.iterations)
        if self.iterations == 100000:
            return False
        else:
            return True
