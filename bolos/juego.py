class Game:

    def __init__(self):
        self.rolls = []
        self.frame = Frame()

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        resultado = 0
        indice_roll = 0
        for frameIndice in range(10):
            if self.rolls[indice_roll] + self.rolls[indice_roll + 1] == 10:
                resultado += self.rolls[indice_roll] + self.rolls[indice_roll + 1] + self.rolls[indice_roll + 2]
            else:
                resultado += self.rolls[indice_roll] + self.rolls[indice_roll + 1]
            indice_roll += 2
        self.frame.is_pare(indice_roll)
        return resultado


class Frame:
    def add_roll(self, pins: int):
        pass

    def score(self) -> int:
        pass

    def is_pare(self, indice_roll) -> bool:
        pass

    def is_strake(self) -> bool:
        pass


class Roll:
    def __init__(self):
        self.frame = Frame()
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
