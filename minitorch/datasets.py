import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """
    Generate a simple 2D dataset split by a vertical line at x = 0.5.

    Each point is labeled 1 if x < 0.5, else 0.

    Args:
        N (int): Number of samples to generate.

    Returns:
        Graph: A graph object containing the points and binary labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """
    Generate a 2D dataset split by a diagonal line x + y = 0.5.

    Each point is labeled 1 if x + y < 0.5, else 0.

    Args:
        N (int): Number of samples to generate.

    Returns:
        Graph: A graph object containing the points and binary labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """
    Generate a 2D dataset with two vertical bands near the edges labeled as 1.

    Points are labeled 1 if x < 0.2 or x > 0.8, else 0.

    Args:
        N (int): Number of samples to generate.

    Returns:
        Graph: A graph object containing the points and binary labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """
    Generate a 2D XOR-style dataset with diagonal separation.

    Points are labeled 1 if they lie in opposite quadrants across x=0.5 and y=0.5, else 0.

    Args:
        N (int): Number of samples to generate.

    Returns:
        Graph: A graph object containing the points and binary labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if ((x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5)) else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """
    Generate a circular 2D dataset with an inner region labeled 0 and outer ring labeled 1.

    Points are labeled 1 if their distance from center (0.5, 0.5) is greater than sqrt(0.1), else 0.

    Args:
        N (int): Number of samples to generate.

    Returns:
        Graph: A graph object containing the points and binary labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = (x_1 - 0.5, x_2 - 0.5)
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """
    Generate a 2D spiral dataset with two interleaved spirals labeled 0 and 1.

    The spirals are generated using parametric equations and mapped into the unit square.

    Args:
        N (int): Number of samples to generate (evenly split between the two spirals).

    Returns:
        Graph: A graph object containing the spiral points and binary labels.
    """

    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
