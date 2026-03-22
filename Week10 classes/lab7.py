#################################################
# APS106 - Winter 2025                          #
# LAB 7 - Image processing and corner detection #
#################################################

from operator import itemgetter

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################

def convert_rgb_to_gs(rgb_img):
    """
    (tuple) -> tuple
    
    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation: 
    `grayscale_intensity = 0.3 * R + 0.59 * G + 0.11 * B`
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.

    Parameters
    ----------
    rgb_img: tuple
        A nested tuple of RGB pixels. Each element of the tuple is a 3-element
        tuple representing the RGB components of a pixel. The RGB components
        are integers in the range [0, 255]. The red, green, and blue components
        are at indices 0, 1, and 2 respectively.

    Returns
    -------
    tuple
        A tuple of grayscale pixel intensities. Each element of the tuple is
        an integer in the range [0, 255].
    """
    gs_list = []
    # loop through all pixels
    for pixel in rgb_img:

        R, G, B = pixel
        gs = 0.3 * R + 0.59 * G + 0.11 * B
        gs_round = round(gs)
        gs_list.append(gs_round)

    return tuple(gs_list)
    


############################
# Part 2b - Dot Product    #
############################

def dot_product(x,y):
    """
    (tuple, tuple) -> float
    
    Perform a 1-dimensional dot product operation on the input vectors x
    and y. 

    Parameters
    ----------
    x: tuple
        A tuple of floating point numbers.
    y: tuple
        A tuple of floating point numbers.

    Returns
    -------
    float
        The dot product of the two input vectors.
    """
    product = 0

    for i in range(len(x)):
        product_i = x[i] * y[i]
        product = product + product_i

    return float(product)

######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_2D_img_segment(img, w, h, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.
    
    Parameters
    ----------
    img: tuple
        A one-dimensional tuple of grayscale pixel intensities representing
        an image. The image is stored in row-major order.
    w: int
        The width of the image.
    h: int
        The height of the image.
    centre_coordinate: tuple
        A two-element tuple containing the x- and y-coordinates of the centre
        of the 2D segment to extract.
    N: int
        The width and height of the 2D segment to extract. N must be an odd
        integer.
    
    Returns
    -------
    tuple
        A tuple of grayscale pixel intensities representing the NxN segment
        of the image.
    """
    # convert to 2-dimensional list
    column = []
    two_d = []
    for pixel in img:
        column.append(pixel)
        if len(column) == w:
            two_d.append(column)
            column = []

    # 
    extract = []
    
    number_of_pixel_to_explore = N // 2
    centrex, centrey = centre_coordinate
    for row_index in range(centrey - number_of_pixel_to_explore, centrey + number_of_pixel_to_explore + 1):
        for column_index in range(centrex - number_of_pixel_to_explore, centrex + number_of_pixel_to_explore + 1):
            extract.append(two_d[row_index][column_index])
        
    return tuple(extract)
    

######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(kernel, img, w, h):
    """
    (tuple, int, int, tuple) -> tuple
    
    Apply the kernel filter defined within the two-dimensional tuple kernel to 
    image defined by the pixels in img and its width and height.

    Parameters
    ----------
    kernel: tuple
        A two-dimensional tuple defining a NxN filter kernel. N must be an odd
        integer.
    img: tuple
        A one-dimensional tuple of grayscale pixel intensities representing
        an image. The image is stored in row-major order.
    w: int
        The width of the image.
    h: int
        The height of the image.

    Returns
    -------
    tuple
        A tuple of grayscale pixel intensities representing the filtered image.
    """
    # convert kernel to 1-dimensional
    # mail output: "kernel_1_d"
    kernel_1_d = []
    for row in kernel:
        for item in row:
            kernel_1_d.append(item)

    # convert img to 2-dimensional list
    # main output:  "two_d"
    column = []
    two_d = []
    for pixel in img:
        column.append(pixel)
        if len(column) == w:
            two_d.append(column)
            column = []

    # get every pixel's filtered result
    # main output: "explore_limit"
    filtered_list = []
    explore_limit = len(kernel) // 2

    # ???
    # main output: "filtered_list"
    for row_index in range(len(two_d)):
        for column_index in range(len(two_d[row_index])):

            # out of range: undefined window, index too small
            if (row_index - explore_limit < 0) or (column_index - explore_limit < 0):
                filtered = 0
            
            # out of range: undefined window, index too large
            elif (row_index + explore_limit >= len(two_d)) or ((column_index + explore_limit >= len(two_d))):
                filtered = 0

            else:
                extract = extract_2D_img_segment(img, w, h, (column_index, row_index), len(kernel))
                #print(extract, kernel_1_d)
                filtered = dot_product(extract, kernel_1_d)
            
            filtered_list.append(int(filtered))

    return tuple(filtered_list)    



###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (tuple, tuple) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Parameters
    ----------
    Ix: tuple
        A tuple of 9 integer elements representing the x-gradients of a 3x3
        window of pixels.
    Iy: tuple
        A tuple of 9 integer elements representing the y-gradients of a 3x3
        window of pixels.
    
    Returns
    -------
    float
        The Harris response of the pixel.
    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple
    
    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.

    Parameters
    ----------
    img: tuple
        A one-dimensional tuple of grayscale pixel intensities representing
        an image. The image is stored in row-major order.
    width: int
        The width of the image.
    height: int
        The height of the image.
    threshold: float
        The minimum corner strength required for a pixel to be considered a
        corner.
    
    Returns
    -------
    tuple
        A tuple of potential corner locations. Each element in the tuple is a
        two-element tuple containing an x- and y-coordinate.
    """
    
    # apply blurring average first
    blur_kernel = ((1/9, 1/9, 1/9),
                   (1/9, 1/9, 1/9),
                   (1/9, 1/9, 1/9))
    img = kernel_filter(img, width, height, blur_kernel)

    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1,-2,-1),
                              ( 0, 0, 0),
                              ( 1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    border_sz = 3
    corners = []
    for i_y in range(border_sz, height-border_sz):
        for i_x in range(border_sz, width-border_sz):
            Ix_window = extract_2D_img_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_2D_img_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)

            if corner_strength > threshold:
                corners.append([corner_strength,(i_x,i_y)])

    # sort
    corners.sort(key=itemgetter(0),reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple
    
    Filters any corners that are within a region with a stronger corner.
    Returns a list of corners that are at least min_distance away from
    any other stronger corner.

    Parameters
    ----------
    corners: tuple
        A tuple of two-element coordinate lists representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    min_distance: float
        The minimum distance between any two corners returned by this function.

    Returns
    -------
    tuple
        A tuple of two-element coordinate lists representing the corners that
        have been retained after non-maxima suppression.
    """
    min_dist_square = min_distance * min_distance
    # initialize with first item
    suppressed_list = [corners[0]]

    # loop through the oroginal corners list to find out if to add or not
    for unsupressed_corner in corners:
        # compare with every item already added in the supressed list
        for already_added_corner in suppressed_list:
            this_distance_square_list = []
            this_distance_square = ((unsupressed_corner[0] - already_added_corner[0]) ** 2 +
                                    (unsupressed_corner[1] - already_added_corner[1]) ** 2 )
            this_distance_square_list.append(this_distance_square)
        
        # get the min number of distance
        min_this_distance_square = min(this_distance_square_list)

        # min distance is larger than that set
        if min_this_distance_square >= min_dist_square:
            suppressed_list.append(unsupressed_corner)

    return tuple(suppressed_list)

    

