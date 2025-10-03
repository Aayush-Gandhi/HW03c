"""
This module provides a function to classify triangles based on side lengths.
"""
from math import isclose, isfinite

def classify_triangle(a, b, c):
    """
    Classifies a triangle as Equilateral, Right, Isosceles, Scalene,
    or determines if it's not a valid triangle.
    """
    # ... (all of your existing function code is perfect) ...
    # ... (it goes here) ...
    return "Scalene"

def main():  # pragma: no cover
    """Get user input for triangle sides and print the classification."""
    try:
        side_a = float(input("Enter side a: "))
        side_b = float(input("Enter side b: "))
        side_c = float(input("Enter side c: "))
        print(f"Triangle type: {classify_triangle(side_a, side_b, side_c)}")
    except ValueError:
        print("Not a triangle")

if __name__ == "__main__":  # pragma: no cover
    main()
    