import noise
import numpy as np


#This creates a 2d array of noise with perlin noise, and turns it into an image.
def makeNoiseMap():
    #Example: https://stackoverflow.com/questions/36719997/threshold-in-2d-numpy-array
    shape = (1024,1024)
    scale = .5
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    seed = np.random.randint(0,100)

    world = np.zeros(shape)

    # make coordinate grid on [0,1]^2
    x_idx = np.linspace(0, 1, shape[0])
    y_idx = np.linspace(0, 1, shape[1])
    world_x, world_y = np.meshgrid(x_idx, y_idx)

    # apply perlin noise, instead of np.vectorize.
    world = np.vectorize(noise.pnoise2)(world_x/scale,
                            world_y/scale,
                            octaves=octaves,
                            persistence=persistence,
                            lacunarity=lacunarity,
                            repeatx=1024,
                            repeaty=1024,
                            base=seed)

    world = (world < 0) * 1
    img = np.floor((world ) * 255).astype(np.uint8) # <- Normalize world first

    image = img.astype('uint8')

    return image