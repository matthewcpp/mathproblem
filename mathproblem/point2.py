import math

class Point2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y

    def scale(self, k: float):
        self.x *= k
        self.y *= k

    def length(self) -> float:
        return math.sqrt(self.x ** 2.0 + self.y ** 2.0)

    def normalize(self):
        l = self.length()

        self.x /= l
        self.y /= l

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    @staticmethod
    def add(a: 'Point2', b: 'Point2') -> 'Point2':
        return Point2(a.x + b.x, a.y + b.y)

    @staticmethod
    def subtract(a: 'Point2', b: 'Point2') -> 'Point2':
        return Point2(a.x - b.x, a.y - b.y)

    @staticmethod
    def midpoint(a: 'Point2', b: 'Point2') -> 'Point2':
        p: 'Point2' = Point2.add(a, b)
        p.scale(0.5)

        return p

    @staticmethod
    def direction(a: 'Point2', b: 'Point2') -> 'Point2':
        d = Point2.subtract(b, a)
        d.normalize()

        return d

    @staticmethod
    def distance(a: 'Point2', b: 'Point2') -> float:
        d = Point2.subtract(b, a)

        return d.length()

    @staticmethod
    def distance_to_line(pt: 'Point2', line: 'Line2') ->float:
        d = Point2.distance(line.p1, line.p2)
        a = ((line.p2.y - line.p1.y) * pt.x) - ((line.p2.x - line.p1.x) * pt.y) + line.p2.x * line.p1.y - line.p2.y * line.p1.x

        return abs(a) / d

    @staticmethod
    def scale_by_constant(pt: 'Point2', k: float) -> 'Point2':
        return Point2(pt.x * k, pt.y * k)

    @staticmethod
    def divide_by_constant(pt: 'Point2', k: float) -> 'Point2':
        return Point2(pt.x / k, pt.y / k)

    @staticmethod
    def rotate(pt: 'Point2', theta_deg: float):
        cos_theta = math.cos(math.radians(theta_deg))
        sin_theta = math.sin(math.radians(theta_deg))

        return Point2(pt.x * cos_theta + pt.y * sin_theta, -pt.x * sin_theta + pt.y * cos_theta)

    @staticmethod
    def zero():
        return Point2(0, 0)


class Line2:
    def __init__(self, p1: Point2, p2: Point2):
        self.p1: Point2 = p1
        self.p2: Point2 = p2


class Rect:
    def __init__(self, min_pt: Point2, max_pt: Point2):
        self.min: Point2 = min_pt
        self.max: Point2 = max_pt

    def add_point(self, pt: Point2):
        if pt.x < self.min.x:
            self.min.x = pt.x
        if pt.y < self.min.y:
            self.min.y = pt.y

        if pt.x > self.max.x:
            self.max.x = pt.x
        if pt.y > self.max.y:
            self.max.y = pt.y

    def center(self):
        return Point2.midpoint(self.min, self.max)
