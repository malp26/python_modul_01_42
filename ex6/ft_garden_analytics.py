class Plant:

    class Statistics:

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_statistics(self) -> None:
        self._stats.display()

    def __init__(self, name: str, height: float, age: int) -> None:
        self._stats = self.Statistics()
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
        self._stats.record_grow()
        self.set_height(round(self.get_height() + amount, 2))

    def age(self, days: int = 1) -> None:
        self._stats.record_age()
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 color: str = "unknown") -> None:
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

    class Statistics(Plant.Statistics):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _stats: Statistics

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float = 0.0) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str = "unknown") -> None:
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


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int,
                 color: str = "unknown", seed_count: int = 42) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = seed_count
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = self._seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> "
              f"{Plant.is_older_than_year(days)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
