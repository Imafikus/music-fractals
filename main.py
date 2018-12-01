import cv2
import numpy as np
from math import sqrt

def calculate_starting_points(img, side_size):
    """
    Calculates first 3 points for the triangle
    based on the img width and height and side_size.
    Size size is the length of the triangle.

    Whole functions is the represents the 
    calculation of evensided triangle points
    given its orthocenter and side length

    Return List[List[int]] where List[int] are representing
    calculated points
    """

    #? in the future, this should move the C point coordinates
    #? according to some given parameter
    height, width, channels = img.shape
    print(height, width, channels)

    t_x, t_y = int(height/2), int(width/2)
    print(t_x, t_y)

    b = side_size*sqrt(3) / 2

    a_x = int(t_x - side_size / 2)
    a_y = int(t_y + side_size * sqrt(3) / 6)

    b_x = int(t_x + side_size / 2)
    b_y = a_y

    c_x = int(t_x)
    c_y = int(t_y - side_size*sqrt(3) / 3)

    return [ [a_x, a_y], [b_x, b_y], [c_x, c_y] ]  

def calculate_sierpinski_coordinates(triangle, img):
    """
    Calculate next three points following the rule
    for generating sierpinski triangle
    """

    a_x, a_y = triangle[0]
    b_x, b_y = triangle[1]
    c_x, c_y = triangle[2]

    print(a_x, a_y)
    print(b_x, b_y)
    print(c_x, c_y)

    ab_x, ab_y = int((a_x + b_x) / 2), int((a_y + b_y) / 2) 
    ac_x, ac_y = int((a_x + c_x) / 2), int((a_y + c_y) / 2) 
    bc_x, bc_y = int((b_x + c_x) / 2), int((b_y + c_y) / 2)

    
    tr1_points = np.array([ [a_x, a_y], [ab_x, ab_y], [ac_x, ac_y] ], np.int32)  
    tr2_points = np.array([ [ab_x, ab_y], [b_x, b_y], [bc_x, bc_y] ], np.int32)  
    tr3_points = np.array([ [ac_x, ac_y], [bc_x, bc_y], [c_x, c_y] ], np.int32)  


    cv2.polylines(img,[tr1_points],True,(0,128,255), 2)
    cv2.polylines(img,[tr2_points],True,(0,0,255), 2)
    cv2.polylines(img,[tr3_points],True,(255,0,255), 2)


def main():
    img = cv2.imread("lena.jpg")
    
    #line_thickness = 2
    #cv2.line(img, (20, 20), (60, 20), (0, 255, 0), line_thickness)
    
    side_size = 400
    triangle_pts = calculate_starting_points(img, side_size)
    calculate_sierpinski_coordinates(triangle_pts, img)
    
    #pts = np.array(triangle_pts, np.int32)

    #pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
    #cv2.polylines(img,[pts],True,(0,255,255), 3)
    
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()