"""Example: Different Robot vendors use different conventions to describe TCP orientation."""

from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Frame

point = Point(0.0, 0.0, 63.0)
xaxis = Vector(0.68, 0.68, 0.27)
yaxis = Vector(-0.67, 0.73, -0.15)
F = Frame(point, xaxis, yaxis)

print(repr(F.quaternion))  # ABB
print(repr(F.euler_angles(static=False, axes='xyz')))  # Staubli
print(repr(F.euler_angles(static=False, axes='zyx')))  # KUKA
print(repr(F.axis_angle_vector))  # UR
