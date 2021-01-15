
import math
for i in range(11):
    print(i)

for i in range(11):
    if i == 5:
        break
    print(i)

num = 0
while True:
    if num == 5:
        break
    print(num)
    num = num + 1


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


for i in range(1, 11):
    print("Current i = ", i)
    if i % 2 == 0:
        continue
    print("Prining in loop ", i)


for i in range(1, 11):

    if i % 2 == 0:
        print("Current i = ", i)
        continue
    print("Prining in loop ", i)


for i in range(1, 11):
    print("Current i = ", i)
    if i % 2 == 0:
        print("Current i = ", i)
        continue
    print("Prining in loop ", i)


num = 15
num ** 2
num = 7
num ** 23
num ** 2 + 100
num = num / 2
print("Hello")
math.sqrt(324)


def calculateArea(height, width):
    area = height * width
    print(area)


calculateArea(7, 67)


def areaSquare(length):
    result = length**2
    print("Area of square is ", result)


areaSquare(5)


def areaSquare(length):
    result = length**2
    return result


areaSquare(5)
squareResult = areaSquare(5)
print(squareResult)
x = calculateArea(5, 7)
print(x)


def doubleReturn(height, width):
    area = height * width
    perimiter = 2 * (height + width)
    return area, perimiter


doubleReturn(5, 7)
(35, 24)
y = doubleReturn(5, 7)
y
type(y)

areaRectangle, periRectangle = y
areaRectangle
periRectangle
area, peri = doubleReturn(5, 7)
area
peri


def double(number):
    return number * number


def double(number):
    return number * 2


double(5)
double(15)


def getArea(height, width):
    return height * width


getArea(5, 6)
