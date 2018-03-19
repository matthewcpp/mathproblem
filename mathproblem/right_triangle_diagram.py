import sys

from typing import List
from enum import Enum

from .point2 import Point2, Line2, Rect
from .simple_svg import text, polyline, triangle


class RightAngleThetaVertex(Enum):
    VertexB = 1
    VertexC = 2


class RightAngleDiagram:
    """
            al
      a-----------b
       |  |     /
       | _     /
       |      /
     bl|     / cl
       |    /
       |   /
       |  /
       | /
       V c
    """
    def __init__(self, ab: float, ac: float, degrees: float = 0.0, theta_vertex: RightAngleThetaVertex = RightAngleThetaVertex.VertexB):
        self.a_label: str = None
        self.b_label: str = None
        self.c_label: str = None

        # generate triangle points
        self.pt_a = Point2(0, 0)
        self.pt_b = Point2(ab, 0)
        self.pt_c = Point2(0, ac)

        self.ab = ab
        self.ac = ac
        self.bc = Point2.distance(self.pt_b, self.pt_c)

        self.ab_text_pos = Point2.midpoint(self.pt_a, self.pt_b)
        self.ab_text_pos.y -= 15.0

        self.ac_text_pos = Point2.midpoint(self.pt_a, self.pt_c)
        self.ac_text_pos.x -= 15.0

        self.bc_text_pos = Point2.midpoint(self.pt_b, self.pt_c)
        d_vec = Point2.direction(self.ac_text_pos, self.bc_text_pos)
        d_vec.scale(20.0)
        self.bc_text_pos = Point2.add(self.bc_text_pos, d_vec)

        if theta_vertex == RightAngleThetaVertex.VertexB:
            theta_line = Line2(self.pt_b, self._centroid())
            line1 = Line2(self.pt_a, self.pt_b)
            line2 = Line2(self.pt_b, self.pt_c)
        else:
            theta_line = Line2(self.pt_c, self._centroid())
            line1 = Line2(self.pt_a, self.pt_c)
            line2 = Line2(self.pt_b, self.pt_c)

        self.theta_pos = RightAngleDiagram._calc_theta_pos(theta_line, line1, line2, 6.0)

        bracket_size = 15.0

        self.bracket: List[Point2] = [
            Point2(bracket_size, 0),
            Point2(bracket_size, bracket_size),
            Point2(0, bracket_size)
        ]

        if degrees != 0.0:
            self._rotate_triangle(degrees)

    def _rotate_triangle(self, degrees: float):
        centroid = self._centroid()
        centroid.negate()

        # move to origin and rotate
        self.translate(centroid)
        self.rotate(degrees)
        centroid.negate()
        self.translate(centroid)

    def translate(self, offset: Point2):
        self.pt_a = Point2.add(self.pt_a, offset)
        self.pt_b = Point2.add(self.pt_b, offset)
        self.pt_c = Point2.add(self.pt_c, offset)

        self.ab_text_pos = Point2.add(self.ab_text_pos, offset)
        self.ac_text_pos = Point2.add(self.ac_text_pos, offset)
        self.bc_text_pos = Point2.add(self.bc_text_pos, offset)
        self.theta_pos = Point2.add(self.theta_pos, offset)

        for i in range(len(self.bracket)):
            self.bracket[i] = Point2.add(self.bracket[i], offset)

    def rotate(self, degrees: float):
        self.pt_a = Point2.rotate(self.pt_a, degrees)
        self.pt_b = Point2.rotate(self.pt_b, degrees)
        self.pt_c = Point2.rotate(self.pt_c, degrees)

        self.ab_text_pos = Point2.rotate(self.ab_text_pos, degrees)
        self.ac_text_pos = Point2.rotate(self.ac_text_pos, degrees)
        self.bc_text_pos = Point2.rotate(self.bc_text_pos, degrees)

        self.theta_pos = Point2.rotate(self.theta_pos, degrees)

        for i in range(len(self.bracket)):
            self.bracket[i] = Point2.rotate(self.bracket[i], degrees)

    def bounding(self) -> Rect:
        bounding_box = Rect(Point2(sys.float_info.max, sys.float_info.max), Point2(sys.float_info.min, sys.float_info.min))

        bounding_box.add_point(self.pt_a)
        bounding_box.add_point(self.pt_b)
        bounding_box.add_point(self.pt_c)

        bounding_box.add_point(self.ab_text_pos)
        bounding_box.add_point(self.ac_text_pos)
        bounding_box.add_point(self.bc_text_pos)

        bounding_box.add_point(self.theta_pos)

        return bounding_box

    def reposition(self):
        bounding_box = self.bounding()

        padding = 15
        offset = Point2.subtract(Point2(padding, padding), bounding_box.min)
        self.translate(offset)


    @staticmethod
    def _calc_theta_pos(path: Line2, l1: Line2, l2: Line2, tolerance: float) -> Point2:
        step_count = 15
        path_dir = Point2.direction(path.p1, path.p2)
        step_size = Point2.distance(path.p1, path.p2) / step_count

        for i in range(30):
            test_point = Point2.add(path.p1, Point2.scale_by_constant(path_dir, i * step_size))

            if Point2.distance_to_line(test_point, l1) > tolerance and Point2.distance_to_line(test_point, l2) > tolerance:
                return test_point

        return path.p1

    def generate_diagram_svg(self) -> List[str]:
        diagram: List[str] = list()


        diagram.append(triangle(self.pt_a, self.pt_b, self.pt_c))
        diagram.append(polyline(self.bracket, 255, 0, 0))

        if self.a_label is not None:
            diagram.append(text(self.ab_text_pos, str(self.a_label)))
        if self.b_label is not None:
            diagram.append(text(self.ac_text_pos, str(self.b_label)))
        if self.c_label is not None:
            diagram.append(text(self.bc_text_pos, str(self.c_label)))

        diagram.append(text(self.theta_pos, "&theta;"))

        return diagram

    def _centroid(self):
        return Point2.divide_by_constant(Point2.add(Point2.add(self.pt_a, self.pt_b), self.pt_c), 3.0)
