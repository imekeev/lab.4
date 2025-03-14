import math

degree = 15
radian = math.radians(degree)
print("Radian:", radian)

height = 5
base1 = 5
base2 = 6
trapezoid_area = ((base1 + base2) * height) / 2
print("Trapezoid area:", trapezoid_area)

num_sides = 4
side_length = 25
polygon_area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
print("Regular polygon area:", polygon_area)

base = 5
height_parallelogram = 6
parallelogram_area = base * height_parallelogram
print("Parallelogram area:", parallelogram_area)
