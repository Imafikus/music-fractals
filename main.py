import cv2
import numpy as np
from math import sqrt

from random import randint

# --PARAMETERS--

#? line width of a triangle, given in pixels
LINE_WIDTH = 1

#? length of the triangle side given in pixels, starting triangle is evensided
TRIANGLE_SIDE_SIZE = 600

RECURSION_DEPTH = 6
IMG_SRC = "black.jpg"


def calculate_starting_points(img, side_size):
    """
    Calculates first 3 points for the triangle
    based on the img width and height and side_size.
    Size size is the length of one side of the triangle.

    Functions represents the 
    calculation of evensided triangle points
    given its orthocenter and side length

    Return List[List[int]] where List[int] are representing
    calculated points
    """

    #? in the future, this should move the C point coordinates
    #? according to some given parameter
    height, width, channels = img.shape
    #print(height, width, channels)

    random_factor = randint(-100, 100)
    #!calculate_scaling_factor()

    t_x, t_y = int((height+100)/2), int(width/2)
    #print(t_x, t_y)

    b = side_size*sqrt(3) / 2

    a_x = int(t_x - side_size / 2)# + randint(-200, 200)
    a_y = int(t_y + side_size * sqrt(3) / 6)# + randint(-200, 200)

    b_x = int(t_x + side_size / 2)# + randint(-200, 200)
    b_y = a_y 

    c_x = int(t_x) + random_factor
    c_y = int(t_y - side_size*sqrt(3) / 3) + random_factor #+ 700

    return [ [a_x, a_y], [b_x, b_y], [c_x, c_y] ]  

def draw_sierpinski_layer(triangle, img, level):
    """
    Calculate next three points following the rule
    for generating sierpinski triangle and draw them on an image

    """

    if level == 0:
        return

    a_x, a_y = triangle[0]
    b_x, b_y = triangle[1]
    c_x, c_y = triangle[2]

    ab_x, ab_y = int((a_x + b_x) / 2), int((a_y + b_y) / 2) 
    ac_x, ac_y = int((a_x + c_x) / 2), int((a_y + c_y) / 2) 
    bc_x, bc_y = int((b_x + c_x) / 2), int((b_y + c_y) / 2)
    
    tr1 = [ [a_x, a_y], [ab_x, ab_y], [ac_x, ac_y] ]
    tr2 = [ [ab_x, ab_y], [b_x, b_y], [bc_x, bc_y] ]
    tr3 = [ [ac_x, ac_y], [bc_x, bc_y], [c_x, c_y] ]

    tr1_points = np.array(tr1, np.int32)  
    tr2_points = np.array(tr2, np.int32)  
    tr3_points = np.array(tr3, np.int32)  

    cv2.polylines(img,[tr1_points],True,(255, 0, 85), LINE_WIDTH)
    cv2.polylines(img,[tr2_points],True,(255, 0, 85), LINE_WIDTH)
    cv2.polylines(img,[tr3_points],True,(255, 0, 85), LINE_WIDTH)

    tr1 = [ [a_x, a_y], [ab_x, ab_y], [ac_x, ac_y] ]
    tr2 = [ [ab_x, ab_y], [b_x, b_y], [bc_x, bc_y] ]
    tr3 = [ [ac_x, ac_y], [bc_x, bc_y], [c_x, c_y] ]

    level = level-1

    draw_sierpinski_layer(tr1, img, level)
    draw_sierpinski_layer(tr2, img, level)
    draw_sierpinski_layer(tr3, img, level)

def main():
    img = cv2.imread(IMG_SRC)
        
    side_size = 600

    for i in range(0, 10):
        #print(randint(-100, 100))
        img = cv2.imread(IMG_SRC)
        triangle_pts = calculate_starting_points(img, side_size)
        draw_sierpinski_layer(triangle_pts, img, RECURSION_DEPTH)
        path = "pictures/img" + str(i) + ".png"
        cv2.imwrite(path, img)
    
    #cv2.imshow("image", img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    main()