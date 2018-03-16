
class Algorithm:

    def __init__(self):
        pass

    def calculate(self, world):
        dists = []
        for model in world.models:
            model.move(world.ground_line)
            dists.append(model.get_distance())
        print("Best distance:", max(dists))
