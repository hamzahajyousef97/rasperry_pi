import ezdxf
import string
from subprocess import call

def GCode_header(parameters):
    value = {
        "R100": 3, "R101": 5, "R102": 6, "R103": 13, "R104": 0, "R105": 0, "R109": 0, "R112": 0,
        "R113": 100, "R114": 0, "R115": 100, "Tool": 2
    }
    value.update(parameters)

    gcode = string.Template("G-Code Start\n\n").substitute(value)
    # print(header.substitute(value))
    return gcode


# def GCode_conv_line(e, value):

#     value.update({"StartX": round(e.dxf.start[0], 2),
#                   "StartY": round(e.dxf.start[1], 2),
#                   "EndX": round(e.dxf.end[0], 2),
#                   "EndY": round(e.dxf.end[1], 2)})

#     gcode = string.Template(
#         'G00 X$StartX Y$StartY\n'
#         # 'G00 Q1=$Q1 M100 @717\n'
#         # 'H$H1\n'
#         # 'S1\n'
#         # 'M103 @714\n'
#         # 'H$H2\n'
#         'G01 X$EndX Y$EndY\n'
#         # 'M104 M105 S1 @717\n'
#         # 'G00 Q1=$Q2 M100 @717\n\n'
#         ).substitute(value)
#     # print(gcode)
#     return gcode


def GCode_conv_polyline(e, value):
    if e.closed:
        closed = True
    else:
        closed = False

    pts = e.get_points()  # Get every points in the polyline
    gcode = ""

    point_coordinate = []

    for i, pt in enumerate(pts):
        value.update({"X": round(pt[0], 2), "Y": round(pt[1], 2)})
        x = round(pt[0], 2)

        if i == 0:
            first_pt = ((round(pt[0], 2),round(pt[1], 2)))
            # print(first_pt)
            gcode = string.Template(
                '\nG00 X$X Y$Y\n'
                ).substitute(value)
        else:
            gcode += string.Template("G0" + str(i) + " X$X Y$Y \n").substitute(value)

    #Check if the polyline closed
    # if e.closed:
    #     value.update({"X": first_pt[0], "Y": first_pt[1]})
    #     gcode += string.Template("G01 X$X Y$Y \n").substitute(value)

    # End of polyline
    gcode += string.Template("End of polyline\n\n").substitute(value)
    # print(gcode)
    return gcode


def GCode_footer():
    gcode = ('End G-Code')
    return gcode


def main():
    input_filename = "./Drawing/360SXiiS.dxf"
    output_filename = "./Drawing/middle.nc"
    n_layer = 1
    machine_parameters = {"R112": 0, "R114": 700, "Tool": 3}
    value = {"Q1": 1.2, "H1": -200, "H2": -100, "Vel": 600, "Q2": 3}
    incr1 = 0.2
    incr2 = 0.2
    # Read DXF Objects and Generate GCode
    dwg = ezdxf.readfile(input_filename)
    modelspace = dwg.modelspace()

    # Append GCode header
    gcode = GCode_header(machine_parameters)

    # Multiple Layers
    for layer in range(0, n_layer):
        value.update({"Q1": round(value["Q1"]+incr1, 2), "Q2": round(value["Q2"]+incr2, 2)})
        gbody = "(Layer {})\n".format(layer+1)
        for e in modelspace:
            # if e.dxftype() == 'LINE':
            #     gbody += GCode_conv_line(e, value)

            if e.dxftype() == 'LWPOLYLINE':
                gbody += GCode_conv_polyline(e, value)
        gcode += gbody

    # Append GCode Footer
    gcode += GCode_footer()
    print(gcode)

    # Write to File
    with open(output_filename, 'w') as f:
        f.write(gcode)

if __name__ == "__main__":
    main()
    # call(["python", "gcode_reader.py"])