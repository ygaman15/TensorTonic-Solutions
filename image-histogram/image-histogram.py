def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    ans = [0] * 256
    for row in image:
        for pixel in row:
            ans[pixel]+=1

    return ans