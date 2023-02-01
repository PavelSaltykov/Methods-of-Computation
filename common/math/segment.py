from decimal import Decimal


class Segment:
    def __init__(self, left, right):
        left, right = Decimal(left), Decimal(right)
        if left >= right:
            raise ValueError("Right should be greater than left")
        self.left = left
        self.right = right

    def split(self, number_of_segments: int) -> list['Segment']:
        points = self.equidistant_points(number_of_segments)
        segments = [Segment(left, right) for left, right in zip(points[:-1], points[1:])]
        return segments

    def equidistant_points(self, number_of_segments: int) -> list[Decimal]:
        if number_of_segments < 1:
            raise ValueError("Number of segments should a be natural number")

        step = (self.right - self.left) / Decimal(number_of_segments)
        point = self.left
        points = [point]
        number_of_middle_points = number_of_segments - 1

        for _ in range(number_of_middle_points):
            point += step
            points.append(point)

        points.append(self.right)
        return points

    @property
    def length(self) -> Decimal:
        return self.right - self.left

    @property
    def center(self) -> Decimal:
        return (self.left + self.right) / 2

    def contains(self, point: Decimal) -> bool:
        return self.left <= point <= self.right

    def __str__(self) -> str:
        return f"[{self.left}, {self.right}]"

    def __iter__(self):
        return iter((self.left, self.right))
