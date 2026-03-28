###############################
# APS106 Winter 2024 - LAB 9  #
# Wind Turbine Placement OOP  #
###############################

import csv

class Point:
    """
    A point in a two-dimensional coordinate plane
    """

    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"

############################
# Part 1 - Circle Class
############################
class Circle:
    """
    A circle in a two-dimensional coordinate plane
    """

    def __init__(self, centre_x: int, centre_y: int, radius):
        """
        Create a circle defined by its centre coordinate and radius
        """
        self.centre = Point(centre_x, centre_y)
        self.radius = radius

    def __str__(self):
        """
        Generate a string representation of a circle
        """
        return ("Circle with centre coordinate " + 
                str(self.centre) + " and radius " + str(self.radius))

    def move(self, horizontal_translation: int, vertical_translation: int) -> None:
        """
        (Circle, int, int) -> None

        Alters the location of a circle by translating the coordinate
        of its centre coordinate.
        """
        self.centre.x += horizontal_translation
        self.centre.y += vertical_translation

    def overlap(self, circB: 'Circle') -> bool:
        """
        (Circle, Circle) -> bool
        
        Checks whether two circles overlap, return true if they overlap, false otherwise
        """

        # compute the distance between the centres
        d = ((self.centre.x - circB.centre.x) ** 2 + (self.centre.y - circB.centre.y) ** 2) ** (1/2)
        return d < (self.radius + circB.radius)

##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """

    def __init__(self, id_number, placement_centre_x, placement_centre_y, placement_radius):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Circle(placement_centre_x,placement_centre_y, placement_radius)

        self.overlapping_turbines = []

    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

    def move(self, horizontal_translation: int, vertical_translation: int) -> None:
        """
        (WindTurbine, int, int) -> None

        Alters the location of a wind turbine by translating the coordinate
        of its centre coordinate. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.

        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        self.placement.move(horizontal_translation, vertical_translation)
        self.overlapping_turbines = []
        
    def overlap(self, turbineB: 'WindTurbine') -> bool:
        """
        (WindTurbine, WindTurbine) -> bool

        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        return self.placement.overlap(turbineB.placement)

    def validate_placement(self, turbines: list['WindTurbine']):
        """
        (WindTurbine, list of WindTurbines) -> None

        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        for other_turbine in turbines:
            if self.overlap(other_turbine) and self.id_number != other_turbine.id_number:
                self.overlapping_turbines.append(other_turbine)

##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename: str) -> list[WindTurbine]:
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """
    # create an empty turbine list
    turbine_list = []

    # open the file
    turbine_file = open(turbine_filename, 'r')
    lines_with_header = turbine_file.readlines()
    lines_wo_header = lines_with_header[1:]
    for line in lines_wo_header:
        split_line_list = line.split(',')
        id = split_line_list[0]
        x = split_line_list[1]
        y = split_line_list[2]
        r = split_line_list[3]
        new_turbine_obj = WindTurbine(int(id), int(x), int(y), int(r))
        turbine_list.append(new_turbine_obj)

    turbine_file.close()

    return turbine_list

##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines: list[WindTurbine]) -> int:
    """
    (list of WindTurbines) -> int

    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.

    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    number_of_invalid = 0
    for turbine in turbines:
        turbine.validate_placement(turbines)
        if len(turbine.overlapping_turbines) > 0:
            number_of_invalid += 1

    return number_of_invalid