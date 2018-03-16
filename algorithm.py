
class Algorithm:

    def __init__(self):
        pass

    def calculate(self, world):
        for model in world.models:
            model.move(world.ground_line)
        pass
