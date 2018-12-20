import cv2
import numpy as np
import time

from math import sqrt, log10, log

from random import randint, choice

from sound_processing import get_sound, get_sound_duration, get_samp_freq, plot_soundwave

from os.path import join

def calc_distortion_factor2(signal):
    """
    Calculate pseudo-random distortion factor
    based on the signal amplitude
    """
    dist = {}

    dist["a_x"] = 0
    dist["a_y"] = 0
    
    dist["b_x"] = 0
    dist["b_y"] = 0
    
    dist["c_x"] = int(signal[0])
    dist["c_y"] = int(signal[1])

    return dist

def calc_distortion_factor3(signal):
    """
    Calculate pseudo-random distortion factor
    based on the signal amplitude
    """
    dist = {}

    dist["a_x"] = int(signal[0])
    dist["a_y"] = int(signal[1])
    
    dist["b_x"] = int(signal[0])
    dist["b_y"] = int(signal[1])
    
    dist["c_x"] = int(signal[0])
    dist["c_y"] = int(signal[1])

    return dist

def calc_distortion_factor1(signal, test=False):
    """
    Calculate pseudo-random distortion factor
    based on the signal amplitude
    """
    dist = {}

    if  test:

        dist["a_x"] = 0
        dist["a_y"] = 0
        
        dist["b_x"] = 0
        dist["b_y"] = 0
        
        dist["c_x"] = 0
        dist["c_y"] = 0

    else:
        dist["a_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.005
        dist["a_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.005
        
        dist["b_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.005
        dist["b_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.005
        
        dist["c_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.005
        dist["c_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.005


    return dist

def calc_distortion_factor3(signal, test=False):
    """
    Calculate pseudo-random distortion factor
    based on the signal amplitude
    """
    dist = {}

    if  test:

        dist["a_x"] = 0
        dist["a_y"] = 0
        
        dist["b_x"] = 0
        dist["b_y"] = 0
        
        dist["c_x"] = 0
        dist["c_y"] = 0

    else:
        dist["a_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.015
        dist["a_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.015
        
        dist["b_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.015
        dist["b_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.015
        
        dist["c_x"] = int(signal[0])**2 * choice([-1, 1]) * 0.015
        dist["c_y"] = int(signal[1])**2 * choice([-1, 1]) * 0.015


    return dist


def calc_distortion_factor2(signal, test=False):
    """
    Calculate pseudo-random distortion factor
    based on the signal amplitude
    """
    dist = {}

    if  test:

        dist["a_x"] = 0
        dist["a_y"] = 0
        
        dist["b_x"] = 0
        dist["b_y"] = 0
        
        dist["c_x"] = 0
        dist["c_y"] = 0

    else:
    
        prepared_signal = abs(int(signal[0])), abs(int(signal[1]) ) 
    
        dist["a_x"] = (int(prepared_signal[0])+10 ) * choice([-1, 1]) * 0.4 
        dist["a_y"] = (int(prepared_signal[1])+10 ) * choice([-1, 1]) * 0.4
        
        dist["b_x"] = (int(prepared_signal[0])+10 ) * choice([-1, 1]) * 0.4
        dist["b_y"] = (int(prepared_signal[1])+10 ) * choice([-1, 1]) * 0.4
        
        dist["c_x"] = (int(prepared_signal[0])+10 ) * choice([-1, 1]) * 0.4
        dist["c_y"] = (int(prepared_signal[1])+10 ) * choice([-1, 1]) * 0.4


    return dist


def calculate_starting_points(img, side_size, x_offset, y_offset, distortion):
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

    t_x, t_y = int((height + x_offset)/2), int(width/2 + y_offset)

    b = side_size*sqrt(3) / 2

    a_x = int(t_x - side_size / 2) + distortion["a_x"]
    a_y = int(t_y + side_size * sqrt(3) / 6) + distortion["a_y"]

    b_x = int(t_x + side_size / 2) + distortion["b_x"]
    b_y = a_y + distortion["b_x"]

    c_x = int(t_x) + distortion["c_x"]
    c_y = int(t_y - side_size*sqrt(3) / 3) + distortion["c_y"]

    return [ [a_x, a_y], [b_x, b_y], [c_x, c_y] ]  

def draw_sierpinski_layer(triangle, img, level, color):
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

    cv2.polylines(img,[tr1_points],True, color, LINE_WIDTH)
    cv2.polylines(img,[tr2_points],True, color, LINE_WIDTH)
    cv2.polylines(img,[tr3_points],True, color, LINE_WIDTH)

    tr1 = [ [a_x, a_y], [ab_x, ab_y], [ac_x, ac_y] ]
    tr2 = [ [ab_x, ab_y], [b_x, b_y], [bc_x, bc_y] ]
    tr3 = [ [ac_x, ac_y], [bc_x, bc_y], [c_x, c_y] ]

    level = level-1

    draw_sierpinski_layer(tr1, img, level, color)
    draw_sierpinski_layer(tr2, img, level, color)
    draw_sierpinski_layer(tr3, img, level, color)

def show_image(img):
    """
    Display image given by img
    """
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def generate_image_set(low_pass, normal, high_pass, step):
    """
    Generate image set based on the sampled sound
    and distortion factor
    """
        
    exec_time = {}
    exec_time["distortion_factor"] = 0
    exec_time["image_copy"] = 0
    exec_time["drawing_triangles"] = 0
    exec_time["write_img"] = 0

    print("sound length: ", len(normal))
    sound_length = len(normal)
    i = 0
    img_index = 0

    while i < sound_length:
        
        #?calc distrortion factor
        start = time.time()
        low_distortion = calc_distortion_factor1(low_pass[i])
        normal_distortion = calc_distortion_factor2(normal[i])
        high_distortion = calc_distortion_factor3(high_pass[i])
        end = time.time()

        exec_time["distortion_factor"] += (end-start)

        #?make background image
        start = time.time()
        img = np.zeros((1024, 1280, 3), np.uint8)
        end = time.time()
        exec_time["image_copy"] += (end-start)
        
        start = time.time()
        
        #?first triangle
        triangle_pts = calculate_starting_points(img, TRIANGLE_SIDE_SIZE, -540, -400, low_distortion)
        draw_sierpinski_layer(triangle_pts, img, RECURSION_DEPTH, (255, 255, 255) )

        #?second triangle
        triangle_pts = calculate_starting_points(img, TRIANGLE_SIDE_SIZE, 200, -100, normal_distortion)
        draw_sierpinski_layer(triangle_pts, img, RECURSION_DEPTH, (0, 204, 0) )
                
        #?third triangle
        triangle_pts = calculate_starting_points(img, TRIANGLE_SIDE_SIZE, 940, 200, high_distortion)
        draw_sierpinski_layer(triangle_pts, img, RECURSION_DEPTH, (0, 0, 204) )
        end = time.time()
        exec_time["drawing_triangles"] += (end-start)
        

        start = time.time()
        res_path1 = join(*["pictures", "img" + str(img_index).zfill(7) + "res_smaller.png"])        
        
        cv2.imwrite(res_path1, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

        i += step
        img_index += 1

        end = time.time()
        exec_time["write_img"] += (end-start)
    
    print("EXEC TIME: ", exec_time)

#? --PARAMETERS--

#? Line width of a triangle, given in pixels
LINE_WIDTH = 1

#? Length of the triangle side given in pixels, starting triangle is evensided
TRIANGLE_SIDE_SIZE = 300

#? How deep should recursion go in draw_sierpinski_layer function
RECURSION_DEPTH = 5

#? Path to folder where generated images are saved
GENERATED_IMG_PATH = "pictures"

#? define fps rate for the video
#? NOTE: You must put same framerate here and in the ffmpeg script
FPS_RATE = 24

def main():

    low_pass_path = "animals/animals_lowpass.wav"
    low_pass = get_sound(low_pass_path)

    normal_path = "animals/animals.wav"
    normal = get_sound(normal_path)

    high_pass_path = "animals/animals_highpass.wav"    
    high_pass = get_sound(high_pass_path)

    samp_freq = get_samp_freq(normal_path)
    
    #? step defines how many fps our video is going to have
    step = int(samp_freq / FPS_RATE)
    
    generate_image_set(low_pass, normal, high_pass, step)
        
if __name__ == "__main__":
    main()

