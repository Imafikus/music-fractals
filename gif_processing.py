import imageio
from os import listdir
from os.path import isfile, join

def generate_gif(duration):
    """
    Generates a gif from images.    
    """
    mypath = "pictures"

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print("ONLY FILES: ", onlyfiles)
    #return
    images = []

    #!!!FIXME, cannot be fixed value
    for img in onlyfiles:
        #if i % 100 == 0:
        #!FIXME cannot have path like this
        filename = "pictures/" + img# + ".png"
        images.append(imageio.imread(filename))
    
    output_file = 'test.gif'
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    pass