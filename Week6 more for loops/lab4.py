def extract_name_from_email(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string containing the first and last names separated by a comma.

    Parameters
    ----------
    email : str
        A string with the format "first_name.last_name@domain.com" where
        first_name and last_name are strings of characters with no spaces

    Returns
    -------
    str
        A string with the format "Last_name,First_name" where
        the first and last names are capitalized and separated by a comma
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'Conda,Anna'
    """
    first_dot_last_list = email.split('@') # split the string from the '@' symbol
    first_dot_last = first_dot_last_list[0] # we only need the first part

    # split the string before @ using the dot
    first_last_list = first_dot_last.split('.') 
    first = first_last_list[0]
    last = first_last_list[1]

    # capitalize
    cap_first = first.capitalize()
    cap_last = last.capitalize()

    return cap_last + ',' + cap_first



def calculate_site_average(measurements, site):
    """
    (str, str) -> str
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the average of the site measurements to two decimal places.

    Parameters
    ----------
    measurements : str
        A string of comma separated site-measurement pairs where the site
        is a string and the measurement is a float.
    site : str
        A string representing the site for which the average is to be calculated.

    Returns
    -------
    str
        The average of the site measurements to two decimal places or "NULL"
        if there are no measurements for the specified site.
    
    >>> calculate_site_average("A, 4.23, B, 6.77, Control, 7.10, B, 6.55, Control, 7.82, Control, 6.89, A, 3.93", "Control")
    7.27
    """
    # remove all blank spaces
    measurements_no_space = measurements.translate({32: None})

    # split the measurements
    measure_list = measurements_no_space.split(',')

    # verify measurement string has even number of elements
    if len(measure_list) % 2 != 0:
        print('This is not a valid input.')
        return None

    # initialize loop
    site_occurence = 0
    site_ph_total = 0
    for i in range(0, len(measure_list)//2):
        if measure_list[2*i] == site:
            site_ph_total += float(measure_list[2*i + 1])
            # print('in loop:', i, site_ph_total)
            site_occurence += 1

    # no occurence / not available:
    if site_occurence == 0:
        return 'NULL'
    
    # divide total by occurences
    average = site_ph_total / site_occurence
    average_round = round(average, 2)
    average_str = str(average_round)

    return average_str



def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name and average of control
    site pH level measurements from string of technician measurements. 
    
    Parameters
    ----------
    measurement_info : str
        A string with the format "firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ..."
    site : str
        A string representing the site for which the average is to be calculated.
    
    Returns
    -------
    str
        A string with the format "date,Lastname,Firstname,site,average pH of specified site
 
    >>> generate_summary("michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90", "Chilis")
    '05/05/05,Scott,Michael,Chilis,4.05'
    """
    # remove all spaces
    measurement_info = measurement_info.translate({32: None})

    # split into 3 parts
    info_split = measurement_info.split(',', 2)
    email = info_split[0]
    date = info_split[1]
    measurement_comma = info_split[2]

    # name
    name_str = extract_name_from_email(email)
    # will have something like "Last,First"

    # get average in site
    average_str = calculate_site_average(measurement_comma, site)
    # will get something like "1.23"

    # combine all parts
    if average_str != None:
        output = date + ',' + name_str + ',' + site + ',' + average_str
        return output
    
    print('measurements not valid. Please check the input info')