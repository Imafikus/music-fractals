if [[ $# -eq 1 ]] ; then

    echo "create pictures dir..."
    echo
    mkdir pictures

    echo "generating image set...";
    echo
    python main.py;

    echo "copying .wav file to folder";
    echo
    cp animals/$1.wav pictures/$1.wav;

    echo "generating video";
    echo
    ffmpeg -framerate 24 -i pictures/img%07dres_smaller.png  -i  pictures/$1.wav  -acodec copy  sucessful_samples/$1.avi;

    echo "cleaning up..."
    echo
    rm -rf pictures

    echo "Video generated sucessfully, playing it...";
    mpv sucessful_samples/$1.avi
else
    echo "usage: ./test.sh name_of_the_wav_file";
    exit 1
fi