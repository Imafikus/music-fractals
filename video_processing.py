import cv2
import numpy as np
from os import listdir         
from os.path import isfile, join    
# Create a VideoCapture object

def write_to_video():

    #cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    #if (cap.isOpened() == False): 
    #  print("Unable to read camera feed")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    #frame_width = int(cap.get(3))
    #frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (256, 307))
    print("out file:", out)

    mypath = "pictures"

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print("ONLY FILES: ", onlyfiles)


    for file in onlyfiles:
      
          frame = cv2.imread(join(mypath, file))
          print("Frame shape", frame.shape)

          # Write the frame into the file 'output.avi'
          out.write(frame)

          # Display the resulting frame    
          cv2.imshow('frame',frame)
          cv2.waitKey(0)

    # When everything done, release the video capture and video write objects
    #cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    write_to_video()