def equal(expected_result, submission_result, msg):
    """
    Return true if submission_result is equal to expected_result, false otherwise.
    If not equal, print error message.
    """
    if expected_result==None:
        # check for correct type
        if submission_result!=None:
            print(msg)
            return False
    
    elif isinstance(expected_result,str):
        if not isinstance(submission_result,str):
            print(msg)
            return False
        
        if expected_result != submission_result:
            print(msg)
            return False
    
    elif isinstance(expected_result, bool):
        # check for correct type
        if not isinstance(submission_result, bool):
            print(msg)
            return False
        
        # check value
        if expected_result != submission_result:
            print(msg)
            return False
    
    elif isinstance(expected_result, int):
        # check for correct type
        if not isinstance(submission_result, int):
            print(msg)
            return False
        
        # check value
        if expected_result != submission_result:
            print(msg)
            return False
        
    elif isinstance(expected_result, list):
        # check for correct type
        if not isinstance(submission_result, list):
            print(msg)
            return False
        
        if len(expected_result)!=len(submission_result):
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
    
    Run Circle.move test, return true if test passes, false otherwise
    """
    from lab8 import Circle
    sub_c = Circle(3, 4, 8)
    
    pre_move_pt_id = id(sub_c.centre)

    sub_out = sub_c.move(33,-19)

    post_move_pt_id = id(sub_c.centre)
    
    # test that method returns None
    returns_none = equal(None, sub_out, "Your Circle.move method does not return None")

    # test that the coordinates of the circle are updated correctly
    correct_coordinates = equal('Circle with centre coordinate (36,-15) and radius 8', 
                                str(sub_c), 
                                "Circle.move method does not modify circle objects as expected")

    # test that no new Point object was created
    update_centre = equal(pre_move_pt_id, post_move_pt_id,
                          "Your Circle.move method creates a new Point object. It should update the existing Point")
 
    return returns_none and correct_coordinates and update_centre

def test_02():
    """
    (None) -> bool
    
    Run WindTurbine.move test, return true if test passes, false otherwise
    """
    from lab8 import WindTurbine
    sub_t = WindTurbine(14, 22, -7, 29)
    
    pre_move_circ_id = id(sub_t.placement)
    pre_move_pt_id = id(sub_t.placement.centre)
 
    sub_out = sub_t.move(33,-19)

    post_move_circ_id = id(sub_t.placement)
    post_move_pt_id = id(sub_t.placement.centre)

    # test that the method returns none
    returns_none = equal(None, sub_out, "Your WindTurbine.move method does not return None")

    # test that the coordinates of the circle are updated correctly
    correct_coordinates = equal('Wind Turbine ID: 14, Placement: Circle with centre coordinate (55,-26) and radius 29', 
                                str(sub_t), 
                                "WindTurbine.move method does not modify circle objects as expected")

    # test that no new Point object was created
    update_centre = equal(pre_move_pt_id, post_move_pt_id,
                          "Your WindTurbine.move method creates a new Point object. It should update the existing Point")

    # test that no new Circle object was created
    update_placement = equal(pre_move_circ_id, post_move_circ_id,
                             "Your WindTurbine.move method creates a new Circle object. It should update the existing Circle")
 

 
    return returns_none and correct_coordinates and update_centre and update_placement

        
def test_03():
    """
    (None) -> bool
    
    Run WindTurbine.overlap test, return true if test passes, false otherwise
    """
    from lab8 import load_turbine_placements
    sub_out = load_turbine_placements("turbines1.csv")

    # convert list of turbines to list of string representations
    sub_out_strs = []
    if isinstance(sub_out,list):
        for t in sub_out:
            sub_out_strs.append(str(t))    

    expected_out_strs = ['Wind Turbine ID: 1, Placement: Circle with centre coordinate (8,-9) and radius 8', 
                         'Wind Turbine ID: 52, Placement: Circle with centre coordinate (-9,71) and radius 5',
                         'Wind Turbine ID: 5, Placement: Circle with centre coordinate (0,0) and radius 1',
                         'Wind Turbine ID: 8, Placement: Circle with centre coordinate (7,99) and radius 2']

    return equal(expected_out_strs, sub_out_strs, "load_turbine_placements returns the incorrect result")

    
def test_04():
    """
    (None) -> bool
    
    Run WindTurbine.validate_placement test, return true if test passes, false otherwise
    """
    from lab8 import WindTurbine
    
    t1 = WindTurbine(1, 1, 2, 5)
    t2 = WindTurbine(2, 0, 2, 4)
    t3 = WindTurbine(3, 11, 12, 5)
    sub_ret = t2.validate_placement([t1, t2, t3])    
    
    t2_overlapping_strs = []
    for t in t2.overlapping_turbines:
        t2_overlapping_strs.append(str(t))
    
    return (equal(None, sub_ret, "Your method does not return None.") and 
            equal(['Wind Turbine ID: 1, Placement: Circle with centre coordinate (1,2) and radius 5'],
                   t2_overlapping_strs,
                   "Your WindTurbine.validate_placement method does not identify the correct overlapping turbines"))
    
def test_05():
    """
    (None) -> bool
    
    Run check_turbine_placements test, return true if test passes, false otherwise
    """
    from lab8 import check_turbine_placements, WindTurbine
    
    t1 = WindTurbine(1, 1, 2, 5)
    t2 = WindTurbine(2, 0, 2, 4)
    t3 = WindTurbine(3, 11, 12, 5)
    t4 = WindTurbine(4, -1, 4, 1)
    sub_out = check_turbine_placements([t1,t2,t3,t4])
    exp_out = 3
    return equal(exp_out, sub_out, "Your check_turbine_placement function does not return the correct number of overlapping turbines")


    
    
def run_tests():
    """
    Run all MarkUS test functions
    """
    if test_01():
        print("test 1 passed\n\n")
    else:
        print("test 1 failed, see error message above\n\n")
        
    if test_02():
        print("test 2 passed\n\n")
    else:
        print("test 2 failed, see error message above\n\n")
        
    if test_03():
        print("test 3 passed\n\n")
    else:
        print("test 3 failed, see error message above\n\n")
        
    if test_04():
        print("test 4 passed\n\n")
    else:
        print("test 4 failed, see error message above\n\n")
        
    if test_05():
        print("test 5 passed\n\n")
    else:
        print("test 5 failed, see error message above\n\n")
        

if __name__ == '__main__':
    run_tests()
