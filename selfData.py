
class Point:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year



    def __str__(self) -> str:
        return f"({self.day}, {self.month}, {self.year})"


Point= Point(21, 42,2021)
print(str(Point))

