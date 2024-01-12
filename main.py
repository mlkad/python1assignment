import cmath
from math import sqrt
from math import cos, sin, tan

# Problem 1
a = float(input())
P = 4 * a
S = a ** 2
print(P)
print(S)

# Problem 2
a = float(input())
b = float(input())
P = 2 * (a + b)
S = a * b
print(P)
print(S)

# Problem 3
a = float(input())
b = float(input())
c = float(input())
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(V)
print(S)

# Problem 4
a = float(input())
b = float(input())
geometric_mean = (a * b) ** 0.5
print(geometric_mean)

# Problem 5
a = float(input())
b = float(input())
c = (a**2 + b**2)**0.5
P = a + b + c
print(c)
print(P)

# Problem 6
A = float(input())
B = float(input())
C = float(input())
A, B, C = B, C, A
print(A, B, C)

# Problem 7
A = float(input())
B = float(input())
C = float(input())
A, B, C = C, A, B
print(A, B, C)

# Problem 8
x = float(input())
y = 3 * x**2 - 6 * x + 7
print(y)

# Problem 9
x = float(input())
y = 4 * (x - 3)**2 + 7 * (x - 2) + 2
print(y)

# Problem 10
name = input("Enter your name:")
print("Hello, " + name)

# Problem 11
number = input()
sum_digits = sum(int(digit) for digit in number)
print(sum_digits)

# Problem 12
seconds = int(input())
days = seconds // (24 * 3600)
hours = (seconds % (24 * 3600)) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print("DD:" + days, "HH:" + hours, "MM:" + minutes, "SS:" + seconds)

# Problem 13
K = int(input())
day_of_week = (K - 1) % 7
print(day_of_week)

# Problem 14
a = float(input())
b = float(input())
c = float(input())
sorted_values = sorted([a, b, c])
print(sorted_values)

# Problem 15
a = float(input())
b = float(input())
c = float(input())
d = float(input())
sum_abcd = a + b + c + d
diff_abcd = a - b - c - d
prod_abcd = a * b * c * d
print(sum_abcd)
print(diff_abcd)
print(prod_abcd)

# Problem 16
def calculate_expression(x, y):
    numerator = abs(x) + abs(y)
    denominator = 1 + abs(x * y)

    result = numerator / denominator
    return result


x = float(input())
y = float(input())

result = calculate_expression(x, y)
print(result)


# Problem 17
edge_length = float(input())
volume = edge_length**3
surface_area = 6 * (edge_length**2)
print(volume)
print(surface_area)

# Problem 18
num1 = float(input())
num2 = float(input())
arithmetic_mean = (num1 + num2) / 2
geometric_mean = (num1 * num2)**0.5
print(arithmetic_mean)
print(geometric_mean)

# Problem 19
x = float(input())
y = float(input())
z = float(input())

top = math.sqrt(abs(x - 1)) - abs(y)**(1/3)
bottom = 1 + (x**2/2) + (y**2/4)
a = top / bottom

b = x * (math.atan(z) + (math.exp(-(x + 3))))

print(a)
print(b)

# Problem 20
x = float(input())
y = float(input())
z = float(input())

top = 3 + math.exp(y - 1)
bottom = 1 + x**2 * abs(y - math.tan(z))
a = top / bottom

b = 1 + abs(y - x) + (((y - x)**2)/2) + ((abs(y - x)**3)/3)

print(a)
print(b)

# Problem 21
x = float(input())
y = float(input())
z = float(input())

top = (1 + y) * ((x + y) / (x**2 + 4))
bottom = math.exp(-x - 2) + (1/(x**2 + 4))
a = top / bottom

top_2 = 1 + math.cos(y - 2)
bottom_2 = (x**4/2) + math.sin(z) ** 2
b = top_1 / bottom_2

print(a)
print(b)

# Problem 22
x = float(input())
y = float(input())
z = float(input())

bottom = y**2 + abs((x**2)/(y + (x**3/3)))
a = y + (x/bottom)

b = 1 + math.tan(z/2)**2

print(a)
print(b)

# Problem 23
x = float(input())
y = float(input())
z = float(input())

top = 2 * math.cos(x - (math.pi/6))
bottom = (1/2) + math.sin(y)**2
a = top / bottom

bottom_1 = 3 + (z**2/5)
b = 1 + (z**2/bottom_1)

print(a)
print(b)

# Problem 24
x = float(input())
y = float(input())
z = float(input())

top = 1 + math.sin(x + y)**2
bottom = 2 + (abs((x - 2 * x) / (1 + (x**2 * y**2))))
a = (top / bottom) + x

b = math.cos(math.atan(1/z))**2

print(a)
print(b)

# Problem 25
x = float(input())
y = float(input())
z = float(input())

a = math.log(abs(y-math.sqrt(abs(x)) * (x - y/(z + x**2/4))))

b = x - (x**2/(2*3)) + (x**5/(2*3*4*5))

print(a)
print(b)

# Problem 32
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(dist)

# Problem 33
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

dist1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
dist2 = math.sqrt((x3-x2)**2 + (y3-y1)**2)
dist3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
P = dist1 + dist2 + dist3
print(P)


