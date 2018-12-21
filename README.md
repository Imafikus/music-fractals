# music-fractals

## *Distorting fractals based on the sound amplitude.*


This program was made as a project for my Geometry class on faculty. Because the theme of the project was symmetry, and it had to be a video about 30 seconds long, I decided to make a program which will distort the given fractal based on the sound amplitude at the given moment.

Three triangles correspond with sound which has low pass filter (white), original sound (green), and sound with high pass filter (red).

Program generates images which are later merged into the video with sound.

## Dependencies

### Python

- [Python 3.x](https://www.python.org/)
- [SciPy](https://www.scipy.org/) - Used for signal processing
- [OpenCV](https://opencv.org/) - Used for image generation
- [NumPy](https://www.numpy.org/) - Used within SciPy and OpenCV packages
- [matplotlib](https://matplotlib.org/) (optional) - Used for plotting the sound wave 

### Other programs

- [Audacity](https://www.audacityteam.org/) - Used for audio editing
- [ffmpeg](https://ffmpeg.org/) - Used for video generation
- [mpg123](https://mpg123.de/) - Used for converting .mp3 files to .wav files

### Operating System

- [ArchLinux](https://www.archlinux.org/) with [Gnome](https://www.gnome.org/) desktop

### Songs used
- [Martin Garrix - Animals](https://www.youtube.com/watch?v=gCYcHz2k5x0)
- [Noisestorm - Heist](https://www.youtube.com/watch?v=YXYYCFaUUHQ)

## Quick program tour

### Main

It mainly has functionalities used for image generation, it has a number of parameters you can tweak to get different results. 

It's still in development mode, so in the near future, more parameters and less hardcoded values are going to come up

### Sound Processing

This module is used for sound manipulation, it's main purpose is to extract the normalized sound from the wav file to numpy array.

You can optionally plot the soundwave if you want.

## Using the program

Program is set to put all generated images into the 'pictures' folder. You can run the program from terminal by using the following command:

`python3 main.py`

Your program should generate n images per second of the sound file, where n is the number of frames you specified in the main file of the program.

After you've generated images, you should go to the *pictures* folder and run following command:

`ffmpeg -framerate your_framerate -i img%07dres_smaller.png  -i  your_sound.wav  -acodec copy  your_video.avi`

**NOTE 1:** framerate, sound and video file should be specified by you, and if you have tinkered with the generated images naming, you should update that also.

**NOTE 2:** exec_time will tell you the execution part of individual integral parts of the program. Writing images to disc takes about 90% of the time, so you will probably run you program slower/faster depending on your hard drive speed. 

## Converting from .mp3 to .wav

Files are converted by using the following command:

`mpg123 -w  name_for_new_wav_file.wav your_mp3_file.mp3`

NOTE: .wav and .mp3 file names should be specified by you.

## Automatization 

If you don't want to type commands by yourself, you can use *generate_video.sh* to do all operations needed to play the video.

**NOTE:** Paths to .wav file and to folder where the video will be saved **are predefined** inside the shell script, so if you want some other folders **you must change that manually**.  
Also, script generates and deletes *pictures* folder, so the compatibility with the current version of the program remains.

## Final Note

This program is still very much in the development phase, so it's possible that some features are going to be added / replaced / removed.

The latest stable version of the program will always be on master branch.