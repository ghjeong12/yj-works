#CHANGE HERE!
NUM_OF_X = 2
NUM_OF_Y = 3
NUM_OF_LAYERS = 3
#

output_name = "result"+str(NUM_OF_X)+"_"+str(NUM_OF_Y)+"_"+str(NUM_OF_LAYERS) + ".txt"
output_file = open(output_name, 'w')

def init_move(output_file):
    output_file.write('T3 M06\r\n')
    output_file.write('M83 ;(0,0,0)\r\n')
    output_file.write('M43\r\n')
    output_file.write('G91\r\n')
    output_file.write('G01 Z 25.0 F3000\r\n')
    output_file.write('G01 X -65.0 Y 15.0 F3000\r\n')
    output_file.write('G01 Z -24.5 F1500\r\n')

def x_pos_move(output_file):
    output_file.write('M14\r\n')
    output_file.write('M15\r\n')
    output_file.write('G01 Z 2.0 F2000\r\n')
    output_file.write('G01 X 1.0 F2000\r\n')
    output_file.write('G01 Z -2.0 F2000\r\n')

def x_neg_move(output_file):
    output_file.write('M14\r\n')
    output_file.write('M15\r\n')
    output_file.write('G01 Z 2.0 F2000\r\n')
    output_file.write('G01 X -1.0 F2000\r\n')
    output_file.write('G01 Z -2.0 F2000\r\n')

def y_pos_move(output_file):
    output_file.write('M14\r\n')
    output_file.write('M15\r\n')
    output_file.write('G01 Z 2.0 F2000\r\n')
    output_file.write('G01 Y 1.0 F2000\r\n')
    output_file.write('G01 Z -2.0 F2000\r\n')

def y_neg_move(output_file):
    output_file.write('M14\r\n')
    output_file.write('M15\r\n')
    output_file.write('G01 Z 2.0 F2000\r\n')
    output_file.write('G01 Y -1.0 F2000\r\n')
    output_file.write('G01 Z -2.0 F2000\r\n')

def z_pos_move(output_file):
    output_file.write('M14\r\n')
    output_file.write('M15\r\n')
    output_file.write('G01 Z 2.0 F2000\r\n')
    output_file.write('G01 Z -1.0 F2000\r\n')

def layer_move_to_neg_y(output_file):
    for i in range(NUM_OF_Y):
        if((i % 2) == 0):
            for j in range(NUM_OF_X-1):
                x_pos_move(output_file)
        else:
            for j in range(NUM_OF_X-1):
                x_neg_move(output_file)

        if(i != NUM_OF_Y -1):
            y_neg_move(output_file)

# Reverse move for the upper function
# First direction in X-axis is determined as follows.
# NUM_OF_Y == even number -> to positive X
# NUM_OF_Y == odd number -> to negative Y
def layer_move_to_pos_y(output_file):
    for i in range(NUM_OF_Y):
        iterator = NUM_OF_Y - 2 - i # NUM_OF_Y -2 ... 0
        if((iterator % 2) == 0):
            for j in range(NUM_OF_X-1):
                x_pos_move(output_file)
        else:
            for j in range(NUM_OF_X-1):
                x_neg_move(output_file)

        if(i != NUM_OF_Y - 1):
            y_pos_move(output_file)

# Begin writing code
init_move(output_file)
for i in range(NUM_OF_LAYERS):
    if((i % 2) == 0):
        layer_move_to_neg_y(output_file)
    else:
        layer_move_to_pos_y(output_file)
    if(i != NUM_OF_LAYERS - 1):
        z_pos_move(output_file)
    else:  # Ending code
        output_file.write("G01 Z30.0 F2000\r\n")
        output_file.write("M30\r\n")


'''
def printZMove(output_file):
    output_file.write("M14\r\n")
    output_file.write("M15\r\n")
    output_file.write("G01 Z-3.0 F1000\r\n")
    output_file.write("G01 Z-1.0 F100\r\n")
    output_file.write("G01 Z1.0 F100\r\n")
    output_file.write("G01 Z3.0 F1000\r\n")

angle = 0
prev_x = 0.0;
prev_y = 0.0;
new_x = 0.0;
new_y = 0.0;
delta_x = 0.0;
delta_y = 0.0;

while angle < 360:
    if(angle==0):
        output_file.write("G01 Y-")
        output_file.write(str(int(RADIUS)))
        output_file.write(" F400\r\n")
        prev_x = math.cos(math.radians(angle))*RADIUS
        prev_y = math.sin(math.radians(angle))*RADIUS
        printZMove(output_file)
    else:
        new_x = math.cos(math.radians(angle)) * RADIUS
        new_y = math.sin(math.radians(angle)) * RADIUS

        delta_x = (new_y - prev_y) * -1;
        delta_y = (new_x - prev_x) * -1;
        if(delta_x < 0.01 and delta_x > -0.01):
            delta_x = 0.0
        if(delta_y < 0.01 and delta_y > -0.01):
            delta_y = 0;

        output_file.write("G01 X")
        output_file.write("{:.2f}".format(delta_x))
        output_file.write(" Y")
        output_file.write("{:.2f}".format(delta_y))
        output_file.write(" F400\r\n")
        printZMove(output_file)
        prev_x = new_x
        prev_y = new_y
    angle = angle+360/NUM_POINTS

output_file.write("G01 X")
output_file.write("{:.2f}".format(prev_y))
output_file.write(" Y")
output_file.write("{:.2f}".format(prev_x))
output_file.write(" F400\r\n")
'''
output_file.close()
