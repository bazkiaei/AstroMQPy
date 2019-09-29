import numpy as np

import logbook

import sys


logbook.StreamHandler(sys.stdout).push_application()
logger = logbook.Logger('logbook')


def pixel_distance(stars):
    """
    This function measures the distance between to objects. First, it was
    designed to measure the distance betweeen stars in an image in units of
    pixels

    Parameters
    ----------
    stars : np.array
        An array representing the positions of the stars.

    Returns
    -------
    np.array
        Array which contains the distances between stars.

    Notes
    -----
        Alternatively, you can use the following suggestion for calculating
        the Eucliudean Distance between the pairs of coordinates. Link:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
        Scipy.spatial.distance.cdist has an advantage of having a variety of
        distance metrics.
    """
    distances = np.zeros((stars.shape[0], stars.shape[0]))
    logger.info('Start')
    for i in range(stars.shape[0]):
        if i < stars.shape[0] - 1:
            dis1 = stars[i, 0] - stars[i + 1:, 0]
            dis2 = stars[i, 1] - stars[i + 1:, 1]
            dis = np.sqrt(dis1 ** 2 + dis2 ** 2)
            distances[i][i + 1:] = dis
    logger.info('The End!')
    return distances
