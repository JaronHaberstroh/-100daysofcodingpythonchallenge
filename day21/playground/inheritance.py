class Animals():
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animals):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving through water")


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_of_eyes)
