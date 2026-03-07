#####################################################
# APS106 Winter 2024 - Lab 6 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Molecular Formula to Dictionary Converter #
######################################################

def molecule_formula(compound_formula: str):
    """
    (str) -> dictionary

    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    Parameters
    ----------
    compound_formula : str
        A string representing a chemical compound formula. The formula
        is a combination of element symbols and numbers. The element
        symbols are a single uppercase letter, followed by zero or more
        lowercase letters. The numbers are integers.
    
    Returns
    -------
    dictionary
        A dictionary with the elements as keys and the number of atoms of
        that element as values.

    Examples
    --------
    >>> molecule_formula("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}

    >>> molecule_formula("C1H4")
    {'C': 1, 'H': 4}
    """
    elements_dictionary = {}
    element = ''
    number = ''
    added_number = 0
    current_number = 0
    for i in range(len(compound_formula)):

        # is an element
        if compound_formula[i].isalpha():
            number = ''
            element += compound_formula[i]
            
            current_number = 0

        # is a number
        elif compound_formula[i].isnumeric(): 
            # get current element number
            current_number = elements_dictionary.get(element, 0)
            
            # add the number up to get the new number
            number += compound_formula[i]
            
            # add current number with new number, if next char is not a number
            if (i == len(compound_formula) - 1) or (compound_formula[i+1].isalpha()):
                current_number += int(number)

            # create a new dictionary containing current element
            new_dict = {element: current_number}
            elements_dictionary.update(new_dict)

            # clear element only if next char is not a number, or is the last char
            if (i == len(compound_formula) - 1) or (compound_formula[i+1].isalpha()):
                element = ''

    return elements_dictionary


######################################################
# PART 2 - Chemical Expression to Element Dictionary #
######################################################
    
def expression_formula(expr_coeffs, expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    Calculate the total number of atoms of each element in a chemical expression.
    
    Parameters
    ----------
    expr_coeffs : tuple
        A tuple containing integers that represent the coefficients for molecules
        within the expression. The order of the coefficients correspond to the order
        of molecule dictionaries.
    expr_molecs : tuple
        A tuple containing dictionaries that define the molecules within the expression.
        The molecule dictionaries have the form {'atomic symbol' : number of atoms}.
        The order of the coefficients correspond to the order of molecule dictionaries.
    
    Returns
    -------
    dictionary
        A dictionary containing all elements within the expression as keys and the
        corresponding number of atoms for each element within the expression as values.

    Examples
    --------
    
    >>> # expression: 2NaCl + H2 + 5NaF
    >>> expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    total_dictionary = {}
    for coeff_index in range (0,len(expr_coeffs)): # loop over all indices
        current_element_count = 0
        for element in expr_molecs[coeff_index]:
            # get the current element number and add the new number
            current_element_count = total_dictionary.get(element, 0)
            current_element_count += expr_molecs[coeff_index].get(element) * expr_coeffs[coeff_index]

            # create a new dict to hold the number of the current element
            new_dict = {element: current_element_count}

            # update the total dict
            total_dictionary.update(new_dict)

    return total_dictionary

########################################################
# PART 3 - Identify Unbalanced Atoms in a Chemical Eqn #
########################################################

def identify_unbalanced_atoms(reactant_atoms: dict, product_atoms:dict):
    """
    (Dict,Dict) -> Set
    
    Identify the elements that are not balanced between two dictionaries 
    that represent two sides of a chemical equation.
    
    Parameters
    ----------
    reactant_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the reactant side of a chemical equation.
    product_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the product side of a chemical equation.

    Returns
    -------
    Set
        A set containing all the elements that are not balanced between
        the two dictionaries.

    
    Examples
    --------
    >>> identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """

    if reactant_atoms == product_atoms: # same dict
        return set()
    
    # not same elements in products and reactants
    #if listr != listp:    
    #    list_long = listr + listp     # everything listed
    #    list_copy = list(list_long)   # copy the list to loop through; we will only modify list_long

    #    for element in list_copy:
    #        if (element in listr) and (element in listp): # in both, remove
    #            list_long.remove(element)
        
        
    # same elements in both    
    
    # not same dict
    list_long = []
    
    # get all the elements in a set
    list_elementsr = list(reactant_atoms)
    list_elementsp = list(product_atoms)
    list_all = list_elementsp + list_elementsr
    set_all = set(list_all)

    for element in set_all:
        coeffr = reactant_atoms.get(element, 0)
        coeffp = product_atoms.get(element, 0)
        if coeffr != coeffp:
            list_long.append(element)

    return set(list_long)


###############################################
# PART 4 - Check Chemical Equation Balance    #
###############################################

def check_eqn_balance(reactants, products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    Parameters
    ----------
    reactants : tuple
        A two-element nested tuple containing the coefficients for molecules 
        in the reactant expression and the molecules themselves. 
    products : tuple
        A two-element nested tuple containing the coefficients for molecules
        in the product expression and the molecules themselves.

    Returns
    -------
    Set
        A set containing any elements that are unbalanced in the equation.
    
    Examples
    --------
    >>> # balanced equation: C3H8 + 5O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()

    >>> # unbalanced equation: C3H8 + 2O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    """
    # part 1
    list_number_atoms_p = []
    list_number_atoms_r = []

    for formula in products[1]:
        dict_number_atoms_p_new = molecule_formula(formula)
        list_number_atoms_p.append(dict_number_atoms_p_new)

    for formula in reactants[1]:
        dict_number_atoms_r_new = molecule_formula(formula)
        list_number_atoms_r.append(dict_number_atoms_r_new)

    tuple_number_atoms_p = tuple(list_number_atoms_p)
    tuple_number_atoms_r = tuple(list_number_atoms_r)

    tuple_ready2p = products[0], tuple_number_atoms_p
    tuple_ready2r = reactants[0], tuple_number_atoms_r

    # part 2
    expp = expression_formula(products[0], tuple_number_atoms_p)
    expr = expression_formula(reactants[0], tuple_number_atoms_r)

    # part 3
    return identify_unbalanced_atoms(expp, expr)

