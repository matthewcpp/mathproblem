from typing import List
from .point2 import Point2

from io import StringIO


def triangle(a: Point2, b: Point2, c: Point2) -> str:
    return '<polygon points="{},{} {},{} {},{}" style="fill:none;stroke:black;" />\n'.format(
        a.x, a.y, b.x, b.y, c.x, c.y
    )


def polyline(points: List[Point2], color_r: int, color_g: int, color_b: int) -> str:
    point_list = StringIO()

    for point in points:
        point_list.write("{}, {} ".format(point.x, point.y))

    return '<polyline points="{}" style="fill:none;stroke:rgb({}, {}, {});" />\n'.format(
        point_list.getvalue(), color_r, color_g, color_b
    )


def text(pos: Point2, text: str) -> str:
    return '<text x="{}" y="{}" fill="black" font-size="12" text-anchor="middle" >{}</text>\n'.format(
        pos.x, pos.y, text
    )