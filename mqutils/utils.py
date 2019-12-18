import numpy as np

import logbook

import sys


logbook.StreamHandler(sys.stdout).push_application()
logger = logbook.Logger('logbook')


def find_intensity_at_half_radius_sersic(n=1,
                                         r_e=10,
                                         l_total=5e10):
    """
    Computes the vale of intensity at half light radius for Sersic profile.
    The total luminosity of the galaxy should be provided by the user.

    Parameters
    ----------
    n : int, optional
        Sersic index, currently only n=1 is acceptable.
    r_e : int, optional
        The half light radius of the Sersic profile.
    l_total : float, optional
        The total luminosity of the galaxy.

    Returns
    -------
    numpy.float64
        The intensity of the luminosity of the galaxy at half light radius.

    Raises
    ------
    ValueError
        This function accepts only n=1 currently and for other values raises
        ValueError.
    """
    if n != 1:
        raise ValueError('values other than n = 1 are not acceptable yet')
    l_e = (1.678 ** 2) * l_total / (2 * (r_e ** 2) * (np.exp(1.678)) * np.pi)
    return l_e


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
