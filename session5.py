"""Assignment for session 5 based on functions, arguments and parameters concepts"""
import time

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    if repetitions < 0: # Repetition should be positive number
        raise ValueError(f"Value of repetitions can't be negative")

    start = time.perf_counter() # Start the timer
    for i in range(repetitions):
        # Call function
        fn(*args, **kwargs)
    end = time.perf_counter()  # End the timer

    # Calculate and return average time
    return (end-start)/repetitions if repetitions else 0

def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations
    if not isinstance(number, int):
        raise TypeError(f"Only integer type arguments are allowed")
    if (start or end) < 0:
        raise ValueError(f"Value of start or end can't be negative")
    if start > end:
        raise ValueError(f"Value of start should be less than end")
    if number > 10:
        raise ValueError(f"Value of number should be less than 10")
    if len([*args]):
        raise TypeError(f"squared_power_list function takes maximum 1 positional arguments, more provided")
    if len({**kwargs}):
        raise TypeError(f"squared_power_list function take maximum 2 keyword/named arguments, more provided")

    # Return the list of number to the power of numbers from start to end
    return [number**x for x in list(range(start,end))]

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if not isinstance(sides, int):
        raise TypeError(f"Side can be of integer type only")
    if not isinstance(length, (int,float)):
        raise TypeError(f"Length can be a real number. (int or float) type only")
    if not 2<sides<7 :
        raise ValueError(f"Number of sides must be between [3-6]")
    if length < 0 :
        raise ValueError(f"Length should be greater than 0")
    if len([*args]):
        raise TypeError(f"polygon_area function takes maximum 1 positional arguments, more provided")
    if len({**kwargs}):
        raise TypeError(f"polygon_area function take maximum 1 keyword/named arguments, more provided")

    # Return area
    if sides == 3: # Triangle
        return (length **2) * (3**(1/2))/4
    elif sides == 4: # Square
        return length**2
    elif sides == 5: # Pentagon
        return (1/4)*(length**2)*(5*(5 + 2*(5**(1/2))))**(1/2)
    else: # Hexagon
        return (length **2) *3* (3**(1/2))/2

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if not isinstance(temp, (int,float)):
        raise TypeError(f"Temprature can be a real number (int or float) type only")
    if not isinstance(temp_given_in, str):
        raise TypeError(f"Charcater string expected")
    if temp_given_in not in {'f', 'c','F','C'}:
        raise ValueError(f"Only 'f' or 'c' is allowed for fahrenheit or celsius respectively")
    if temp_given_in in {'c','C'} and temp < -273.15: # Celsius
        raise ValueError(f"Temprature can't go below -273.15 celsius = 0 Kelvin")
    elif temp_given_in in {'f','F'} and temp < -459.67: # Fahrenheit
        raise ValueError(f"Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    if len([*args]):
        raise TypeError(f"temp_converter function takes maximum 1 positional arguments, more provided")
    if len({**kwargs}):
        raise TypeError(f"temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in.lower() == 'f': # Convert to C
        return (temp - 32) * (5/9)
    else: # Convert to F
        return (temp * 9/5) + 32

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if not isinstance(speed, (int,float)):
        raise TypeError(f"Speed can be int or float type only")
    if not isinstance(dist, str):
        raise TypeError(f"Charcater string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError(f"Charcater string expected for time unit")
    if dist.upper() not in {'KM','M', 'FT', 'YRD'}:
        raise ValueError(f"Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if time.upper() not in {'MS','S', 'MIN', 'HR', 'DAY'}:
        raise ValueError(f"Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    if speed <0:
        raise ValueError(f"Speed can't be negative")
    if len([*args]):
        raise TypeError(f"temp_converter function takes maximum 1 positional arguments, more provided")
    if len({**kwargs}):
        raise TypeError(f"temp_converter function take maximum 2 keyword/named arguments, more provided")

    # Return the converted speed
    d_dist = {'KM':1,'M':1000,'FT':3280.84,'YRD':1093.61} # Dict for distance conversion
    d_time = {'DAY':0.0416667, 'HR':1, 'MIN':60, 'S':3600, 'MS':3600000}

    c_dis = d_dist.get(dist.upper()) # Conversion factor for distance
    c_time = d_time.get(time.upper()) # Conversion factor for time

    return round((speed * c_dis)/c_time) # Converted Speed
