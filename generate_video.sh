# echo "create pictures dir..."
# mkdir pictures
# echo "generating image set...";
# python main.py;
# echo "copying .wav file to folder";
# cp animals/animals.wav pictures/animals.wav;
echo "generating video";
echo

ffmpeg -framerate 24 -i pictures/img%07dres_smaller.png  -i  pictures/animals.wav  -acodec copy  sucessful_samples/animals.avi;

echo "cleaning up..."
echo

rm -rf pictures

echo "Video generated sucessfully, playing it...";
mpv sucessful_samples/animals.avi
