
PRECISION = -6

def equal(expected_result, submission_result, msg):
    """
    Return true if submission_result is equal to expected_result, false otherwise.
    If not equal, print error message.
    """
    if isinstance(expected_result, int):
        # check for correct type
        if not isinstance(submission_result, int):
            print(msg)
            return False
        
        # check value
        if expected_result != submission_result:
            print(msg)
            return False
        
        
    elif isinstance(expected_result, float):
        # check for the correct type
        if not isinstance(submission_result, float):
            print(msg)
            return False
        
        # check value
        if abs(expected_result - submission_result) > 10**(PRECISION):
            print(msg)
            return False
        
    elif isinstance(expected_result, tuple):
        # check for correct type
        if not isinstance(submission_result, tuple):
            print(msg)
            return False

        # check that the lengths of the tuples are equal
        if len(submission_result) != len(expected_result):
            print(msg)
            return False
        
        for exp_res_item, sub_res_item in zip(expected_result, submission_result):
            if not equal(exp_res_item, sub_res_item, msg):
                return False
    else:
        print("Gradescope error, contact course head TA.")
        return False
        
    return True
                    

def test_01():
    """
    (None) -> bool
    
    Run convert_rgb_to_gs test, return true if test passes, false otherwise
    """
    from lab7 import convert_rgb_to_gs
    # RGB to gray
    test_input = ((3,67,90), (249, 255, 0), (49, 150, 128), (0,0,0),
                  (255,255,255), (1,2,3), (100,200,150))
    
    msg = "\n\nInput: convert_rgb_to_gs(" + str(test_input) + ")\n"
    
    expected_output = (50, 225, 117, 0, 255, 2, 164)
    submission_output = convert_rgb_to_gs(test_input)
        
    
    msg += "Expected output: " + str(expected_output) + "\n"
    msg += "Your output: " + str(submission_output) + "\n"
    return equal(expected_output, submission_output, msg)
    
def test_02():
    """
    (None) -> bool
    
    Run dot_product test, return true if test passes, false otherwise
    """
    from lab7 import dot_product
    # dot_product
    x1 = (-1.0,2.0,-3.0,4.0,-5.0)
    x2 = (1.0,0.0,1.0,0.0,1.0)
    
    msg = "\n\nInput: dot_product(" + str((x1,x2)) + ")\n"
    
    expected_output = -9.0
    submission_output = dot_product(x1,x2)
        
    
    msg += "Expected output: " + str(expected_output) + "\n"
    msg += "Your output: " + str(submission_output) + "\n"
    return equal(expected_output, submission_output, msg)
        
def test_03():
    """
    (None) -> bool
    
    Run extract_2d_img_segment test, return true if test passes, false otherwise
    """
    from lab7 import extract_2D_img_segment
    # extract segment
    
    
    grayscale_input_pixels =  (4,87,233,245,227,209,190,2,59,235,246,229,219,200,
                               17,99,230,220,211,210,201,46,58,196,165,201,179,
                               150,82,63,41,169,190,188,145,99,55,54,55,74,23,
                               12,45,55,56,45,155,145,156)
    centre_pixel = (4,2)
    N = 3
    height = 7
    width = 7
    
    msg = ("Input: extract_2d_img_segment(" + str(grayscale_input_pixels) + "," +
           str(width) + "," + str(height) + "," + str(centre_pixel) + "," + str(N) 
           + ")\n")
    
    submission_output = extract_2D_img_segment(grayscale_input_pixels, width, height, centre_pixel, N)
    
    expected_output = (246, 229, 219, 220, 211, 210, 165, 201, 179)
    
    
    msg += "Expected output: " + str(expected_output) + "\n"
    msg += "Your output: " + str(submission_output) + "\n"
    return equal(expected_output, submission_output, msg)

    
def test_04():
    """
    (None) -> bool
    
    Run kernel_filter test, return true if test passes, false otherwise
    """
    from lab7 import kernel_filter
    # extract segment
    grayscale_input_pixels =  (4,87,233,245,227,209,190,2,59,235,246,229,219,200,
                               17,99,230,220,211,210,201,46,58,196,165,201,179,
                               150,82,63,41,169,190,188,145,99,55,54,55,74,23,
                               12,45,55,56,45,155,145,156)
    kernel = ((-1, -2, -1),
              (0, 0, 0),
              (1, 2, 1))
    height = 7
    width = 7
        
    expected_output = (0, 0, 0, 0, 0, 0, 0, 0, 34, -19, -69, -56, -3, 0, 0, 3,
                       -160, -229, -177, -158, 0, 0, -196, -465, -312, -115, 
                       -121, 0, 0, -95, -397, -489, -520, -577, 0, 0, -38, 
                       -102, -268, -237, -110, 0, 0, 0, 0, 0, 0, 0, 0)
    
    msg = ("Input: kernel_filter(" + str(kernel) + "," + str(grayscale_input_pixels) + "," +
           str(width) + "," + str(height) + ")\n")
    
    submission_output = kernel_filter(kernel, grayscale_input_pixels, width, height)
        
    msg += "Expected output: " + str(expected_output) + "\n"
    msg += "Your output: " + str(submission_output) + "\n"
    return equal(expected_output, submission_output, msg)
    
def test_05():
    """
    (None) -> bool
    
    Run non_maxima_suppression test, return true if test passes, false otherwise
    """
    from lab7 import non_maxima_suppression
    input_tuple = ((5,6),(15,6),(17,5))
    min_dist = 10
    
    msg = "\n\nInput: non_maxima_suppression(" + str(input_tuple) + "," + str(min_dist) + ")\n"
    
    expected_output = ((5,6),(15,6))
    submission_output = non_maxima_suppression(input_tuple, min_dist)
    
    msg += "Expected output: " + str(expected_output) + "\n"
    msg += "Your output: " + str(submission_output) + "\n"
    return equal(expected_output, submission_output, msg)


def run_tests():
    """
    Run all Gradescope test functions
    """
    if test_01():
        print("test 1 passed")
    else:
        print("test 1 failed")
        
    if test_02():
        print("test 2 passed")
    else:
        print("test 2 failed")
        
    if test_03():
        print("test 3 passed")
    else:
        print("test 3 failed")
        
    if test_04():
        print("test 4 passed")
    else:
        print("test 4 failed")
        
    if test_05():
        print("test 5 passed")
    else:
        print("test 5 failed")


if __name__ == '__main__':
    run_tests()
