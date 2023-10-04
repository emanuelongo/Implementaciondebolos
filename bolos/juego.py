class Game:
    pines = []

    def __init__(self):
        pass

    def roll(self, pins: int):
        self.pines.append(pins)

    def score(self) -> int:
        return sum(self.pines)


class Frame:
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass

    def is_pare(self) -> bool:
        pass

    def is_strake(self) -> bool:
        pass


class Roll:
    def __init__(self):
        self.pins = 0


class NormalFrame(Frame):
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass


class TenthFrame(Frame):
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass
