import imageio


def generate_gif(duration):
    """
    Generates a gif from images.
    """

    images = []

    #!!!FIXME, cannot be fixed value
    for i in range(0, 176300):
        if i % 100 == 0:
            #!FIXME cannot have path like this
            filename = "pictures/img" + str(i) + ".png"
            images.append(imageio.imread(filename))
    
    output_file = 'kurcina.gif'
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    pass