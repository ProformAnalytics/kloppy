from dataclasses import dataclass


@dataclass
class Dimension(object):
    min: float
    max: float

    def to_base(self, value: float) -> float:
        return (value - self.min) / (self.max - self.min)

    def from_base(self, value: float) -> float:
        return value * (self.max - self.min) + self.min


@dataclass
class PitchDimensions(object):
    x_dim: Dimension
    y_dim: Dimension
    x_per_meter: float = None
    y_per_meter: float = None


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Line(object):
    p1: Point
    p2: Point


@dataclass
class Rectangle(object):
    p1: Point
    p2: Point

