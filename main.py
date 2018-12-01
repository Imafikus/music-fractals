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

def calculate_sierpinski_coordinates()

def main():
    img = cv2.imread("lena.jpg")
    
    #line_thickness = 2
    #cv2.line(img, (20, 20), (60, 20), (0, 255, 0), line_thickness)
    
    side_size = 400
    triangle_pts = calculate_starting_points(img, side_size)
    
    pts = np.array(triangle_pts, np.int32)

    #pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(0,255,255), 3)
    
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()