"""
 *     author:  _Shinomiyaa_
 *     created: 14.04.2026 07:10:01
"""
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    histogram = [0] * 256 
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram
    