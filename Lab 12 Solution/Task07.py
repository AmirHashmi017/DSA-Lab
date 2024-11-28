<<<<<<< HEAD
class HanoiTower:
    def __init__(self):
        self.base_case = 1

    def display_move(self, from_peg, to_peg):
        print(f"{from_peg} -> {to_peg}")

    def solve(self, discs, from_peg, to_peg, temp_peg):
        if discs == self.base_case:
            self.display_move(from_peg, to_peg)
        else:
            self.solve(discs - 1, from_peg, temp_peg, to_peg)
            self.display_move(from_peg, to_peg)
            self.solve(discs - 1, temp_peg, to_peg, from_peg)

if __name__ == "__main__":
    hanoi = HanoiTower()
    hanoi.solve(3, 'A', 'B', 'C')
=======
class HanoiTower:
    def __init__(self):
        self.base_case = 1

    def display_move(self, from_peg, to_peg):
        print(f"{from_peg} -> {to_peg}")

    def solve(self, discs, from_peg, to_peg, temp_peg):
        if discs == self.base_case:
            self.display_move(from_peg, to_peg)
        else:
            self.solve(discs - 1, from_peg, temp_peg, to_peg)
            self.display_move(from_peg, to_peg)
            self.solve(discs - 1, temp_peg, to_peg, from_peg)

if __name__ == "__main__":
    hanoi = HanoiTower()
    hanoi.solve(3, 'A', 'B', 'C')
>>>>>>> d07c946dcb53b95415258cd54771b79c5a9b122e
