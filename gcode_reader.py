import re
import math
from math import atan

txt = open('./Drawing/middle.nc', 'r').read().split('\n')
ngxy_reg = re.compile(r'G(?P<G>-?\d+(\.\d*)?) X(?P<X>-?\d+(\.\d*)?) Y(?P<Y>-?\d+(\.\d*)?)')

Yarr = []
Xarr = []
max_x = None
max_y = None
min_x = None
min_y = None

width = None
height = None
area = None
center_point = []
point_coordinate = []
poly_Num = None
center_point_coordinate = []

arr_angle_of_point1 = []
arr_angle_of_point = []

arr_angle_of_laser_of_point1 = []
arr_angle_of_laser_of_point = []

laser_height = 65

for i, data in enumerate(txt):
    ngxy = ngxy_reg.match(data)
    if ngxy:
        x = float("{X}".format(**ngxy.groupdict()))
        y = float("{Y}".format(**ngxy.groupdict()))
        g = "{G}".format(**ngxy.groupdict())
        Xarr.append(x)
        Yarr.append(y)
        point_coordinate.append(x)
        point_coordinate.append(y)

        max_x = max(Xarr)
        max_y = max(Yarr)
        min_x = min(Xarr)
        min_y = min(Yarr)

width = abs(max_x) + abs(min_x)
height = abs(max_y) + abs(min_y)
area = width * height
center_point = [(width / 2), (height / 2)]
center_point_coordinate = [((abs(max_x) - abs(min_x)) / 2), ((abs(max_y) - abs(min_y)) / 2)]

# print(center_point_coordinate)


poly_Num = int(len(point_coordinate) / 8)
h = 0
z = 1
f = 0
for i in range(len(point_coordinate)):
    h += 1
    center_of_rectangle_in_loop = []
    exec("center_of_rectangle_%s = [((point_coordinate[f] + point_coordinate[f+4]) / 2), ((point_coordinate[f+1] + point_coordinate[f+3]) / 2)]" % z)
    center_of_rectangle_in_loop = [((point_coordinate[f] + point_coordinate[f+4]) / 2), ((point_coordinate[f+1] + point_coordinate[f+3]) / 2)]
    adjacent = (center_of_rectangle_in_loop[0] - center_point_coordinate[0])     # adjacent
    opposite = (center_of_rectangle_in_loop[1] - center_point_coordinate[1])     # opposite
    hypotenuse = math.hypot(adjacent,opposite)

    exec("angle_of_laser_of_point_%s = 90 - (math.degrees(atan(hypotenuse / laser_height)))" % z)
    arr_angle_of_laser_of_point1.append(90 - (math.degrees(atan(hypotenuse / laser_height))))
    # arr_angle_of_point1.append(exec("angle_of_point_%s" % z))

    if adjacent == 0:
        if opposite < 0:
            exec("angle_of_point_%s = 270" % z)
            arr_angle_of_point1.append(270)
        else:
            exec("angle_of_point_%s = 90" % z)
            arr_angle_of_point1.append(90)
    elif adjacent < 0:
        if opposite < 0:
            exec("angle_of_point_%s = (math.degrees(atan(opposite / adjacent))) + 180" % z)
            arr_angle_of_point1.append((math.degrees(atan(opposite / adjacent))) + 180)
        elif opposite > 0:
            exec("angle_of_point_%s = abs((math.degrees(atan(opposite / adjacent)))) + 90" % z)
            arr_angle_of_point1.append(abs((math.degrees(atan(opposite / adjacent)))) + 90)
    else:
        exec("angle_of_point_%s = math.degrees(atan(opposite / adjacent))" % z)
        arr_angle_of_point1.append(math.degrees(atan(opposite / adjacent)))

    if h == 8:
        z += 1
        h = 0
        f += 8



k = 0
for i in range(poly_Num):
    arr_angle_of_point.append(arr_angle_of_point1[k])
    k += 8

m = 0
for i in range(poly_Num):
    arr_angle_of_laser_of_point.append(arr_angle_of_laser_of_point1[m])
    m += 8


# print(arr_angle_of_point)
# print(arr_angle_of_laser_of_point)



# print(center_point_coordinate)




# print("width: " + str(width))
# print("height: " + str(height))
# print("area: " + str(area))
# print("center point: (" + str(center_point[0]) + ", " + str(center_point[1]) + ")")

# print(point_coordinate)
