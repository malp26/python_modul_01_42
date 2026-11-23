class Plant:

    name: str
    height: float
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, "
              f"{self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80.0
    sunflower.age_days = 45
    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15.0
    cactus.age_days = 120
    for plant in (rose, sunflower, cactus):
        plant.show()
