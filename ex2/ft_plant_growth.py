class Plant:

    name: str
    height: float
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, "
              f"{self.age_days} days old")

    def grow(self, amount: float = 0.8) -> None:
        self.height = round(self.height + amount, 2)

    def age(self, days: int = 1) -> None:
        self.age_days += days


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    print(f"Growth this week: {rose.height - initial_height:.1f}cm")
