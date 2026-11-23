class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, amount: float = 0.8) -> None:
        self.set_height(round(self.get_height() + amount, 2))

    def age(self, days: int = 1) -> None:
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25)
    print(f"\nHeight updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_height(-5)
    rose.set_age(-10)
    print("\nCurrent state: ", end="")
    rose.show()
