

class Animal:
    def __init__(self, name: str | None):
        self.name = name or ""
        self.distance = 0

    def move(self):
        print("moving")
        self.distance += 1

    def get_distance(self):
        return self.distance

    def get_name(self):
        return self.name
