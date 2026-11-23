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


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, amount: float = 2.1) -> None:
        previous_height = self.get_height()
        super().grow(amount)
        if self.get_height() > previous_height:
            self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        previous_age = self.get_age()
        super().age(days)
        if self.get_age() > previous_age:
            self.nutritional_value += days * 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
