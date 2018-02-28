from PIL import Image
from distortions import blur, brightness, composite, contrast, line, resolution, rotation
from elastic_transform import elastic_transform
import numpy as np

def blur_helper(fingerprint):
    coordinates = (np.random.uniform(0, fingerprint.width) - 25, np.random.uniform(0, fingerprint.width) - 25)
    coordinates += (np.random.uniform(coordinates[0] + 25, fingerprint.width) + 25,
                    np.random.uniform(coordinates[1] + 25, fingerprint.height) + 25)

    return blur(coordinates, np.random.uniform(0, 3), fingerprint)

def brightness_helper(fingerprint):
    coordinates = (np.random.uniform(0, fingerprint.width) - 25, np.random.uniform(0, fingerprint.width) - 25)
    coordinates += (np.random.uniform(coordinates[0] + 25, fingerprint.width) + 25,
                    np.random.uniform(coordinates[1] + 25, fingerprint.height) + 25)

    return brightness(coordinates, np.random.uniform(1, 4), fingerprint)

def contrast_helper(fingerprint):
    coordinates = (np.random.uniform(0, fingerprint.width) - 25, np.random.uniform(0, fingerprint.width) - 25)
    coordinates += (np.random.uniform(coordinates[0] + 25, fingerprint.width) + 25,
                    np.random.uniform(coordinates[1] + 25, fingerprint.height) + 25)

    return contrast(coordinates, np.random.uniform(1, 5), fingerprint)

def elastic_transform_helper(fingerprint, random_state):
    return elastic_transform(fingerprint,
                             2 * max(fingerprint.size), 0.08 * max(fingerprint.size),
                             random_state)

def generate(backgrounds, fingerprint):
    helper = (blur_helper, brightness_helper, contrast_helper, resolution_helper, rotation_helper)
    fingerprint_ = line_helper(fingerprint)

    for i in np.random.permutation(len(helper)):
        fingerprint_ = helper[i](fingerprint_)

    random_state = np.random.RandomState()
    seed = np.random.randint(0, 1000000)

    random_state.seed(seed)

    fingerprint_ = elastic_transform_helper(fingerprint_, random_state)
    fingerprint_ = composite(Image.open(backgrounds[np.random.randint(0, len(backgrounds))]), fingerprint_)

    random_state.seed(seed)

    return elastic_transform_helper(fingerprint, random_state), fingerprint_

def line_helper(fingerprint):
    fingerprint_ = fingerprint

    for i in range(np.random.randint(0, 21)):
        coordinates = (np.random.uniform(0, fingerprint.width), np.random.uniform(0, fingerprint.width))
        coordinates += (np.random.uniform(coordinates[0], fingerprint.width),
                        np.random.uniform(coordinates[1], fingerprint.height))
        fingerprint_ = line(coordinates, np.random.uniform(0, 6), fingerprint_)

    return fingerprint_

def resolution_helper(fingerprint):
    coordinates = (np.random.uniform(0, fingerprint.width) - 25, np.random.uniform(0, fingerprint.width) - 25)
    coordinates += (np.random.uniform(coordinates[0] + 25, fingerprint.width) + 25,
                    np.random.uniform(coordinates[1] + 25, fingerprint.height) + 25)

    return resolution(coordinates, np.random.uniform(1, 4), fingerprint)

def rotation_helper(fingerprint):
    coordinates = (np.random.uniform(0, fingerprint.width) - 25, np.random.uniform(0, fingerprint.width) - 25)
    coordinates += (np.random.uniform(coordinates[0] + 25, fingerprint.width) + 25,
                    np.random.uniform(coordinates[1] + 25, fingerprint.height) + 25)

    return rotation(coordinates, np.random.uniform(-10, 10), fingerprint)