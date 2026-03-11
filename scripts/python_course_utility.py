"""
Python file containing functions to be used in the "Python basics for
geoscience and geotechnics" by the Norwegian Geotechnical Institute

@author: Sjur Beyer, sjur.beyer@ngi.no
"""


import time


def custom_mean(input_list: list) -> float:
    """
    Computes the mean using pure python functions
    """
    return sum(input_list) / len(input_list)


def custom_median(input_list: list) -> float:
    """
    Computes the median of a list of numerical values using only
    pure Python functions.

    The median is the middle value in a sorted list.
    If the list has an even number of elements, the median is the average
    of the two middle elements.

    Parameters
    ----------
    input_list : list
        list containing numerical values.

    Returns
    -------
    median : float
        The median of the input list, returned as a float.

    Notes
    -----
    - The input list must contain only numerical values
    - The function does not handle empty lists

    """

    input_sorted = sorted(input_list)

    if len(input_list) % 2 == 0:
        upper_val = input_sorted[len(input_sorted)//2]
        lower_val = input_sorted[len(input_sorted)//2-1]
        median = (upper_val + lower_val)/2
    else:
        median = input_sorted[len(input_sorted)//2-1]
    return median


def custom_variance(input_list: list) -> float:
    """
    Computes the variance of a list of numerical values using pure Python functions.

    The variance is a measure of how far the elements of the list are spread out from the mean. 
    It is calculated as the average of the squared differences between each element and the mean.

    Parameters
    ----------
    input_list : list
        A list of numerical values (int or float). The list must be non-empty.

    Returns
    -------
    variance : float
        The variance of the input list, returned as a float.

    Notes
    -----
    - The input list must contain only numerical values.
    - The function does not handle empty lists or non-numeric inputs.
    - This implementation uses a helper function `custom_mean()` to compute the mean.
    """
    # Use the mean function to compute the mean
    mean = custom_mean(input_list)
    
    # Instantiate a temporary list
    variance_temp = []

    # Append the squared differences to the list
    for c_i in input_list:
        variance_temp.append((c_i-mean)**2)

    # Computing variance as the mean of the squared differences
    # Here we could also use the custom_mean() function if we want
    variance = 1/len(input_list) * sum(variance_temp)

    return variance


def custom_std(input_list: list) -> float:
    """
    

    Parameters
    ----------
    input_list : list
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    variance = custom_variance(input_list)
    return variance**(1/2)


def profile_function(func):  # No type hints
    """
    A decorator used for timing functions

    """
    def wrapper(*args, **kwargs):
        start_time = time.time()        # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()          # Record end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        # Choose the appropriate unit
        if elapsed_time < 1e-9:
            time_unit = "ps"  # picoseconds
            nice_time = elapsed_time*1e12
        elif elapsed_time < 1e-6:
            time_unit = "ns"
            nice_time = elapsed_time * 1e9
        elif elapsed_time < 1e-3:
            time_unit = "µs"
            nice_time = elapsed_time * 1e6
        elif elapsed_time < 1:
            time_unit = "ms"
            nice_time = elapsed_time * 1e3
        else:
            time_unit = "s"
            nice_time = elapsed_time
        print(f"Function '{func.__name__}' took {nice_time:.2f} {time_unit}\n")
        return result                   # Return the original function's result
    return wrapper