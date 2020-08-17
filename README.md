# EPAI Session 5 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Functional Parameters". We have created 5 different functions. session5.py contains the code for these functions and test_session5.py file contains the various tests for these functions 

# Below are 5 key functions in session5.py file. 

### 1. time_it(fn, *args, repetitions= 1, **kwargs)
This function is used to call any function with its required parameters given number of times and it returns the average time to run that function given number of times. 
parameters-
fn -> mandatory positional parameter. function name to call a function.
*args -> to pass the positional arguments for called function.
repetitions -> default named parameter to repeat the function call.
**kwargs -> to be used to pass the named parameters for called function.
Return -> Average time take to call and run the given function.
### 2. squared_power_list(number,*args, start=0, end=5,**kwargs) 
This function returns a list of number raised to the power of numbers between start to end
parameters
numbers -> positional parameter to input number.
*args -> absorb all of the unwanted positional parameters. 
start = 0 -> optional/default keyword argument. This is starting number for the interval for powers.
end - 5 -> optional/default keyword argument. This is last number for the interval for powers. There should be no other keyword parameter passed and this can be used to verify and raise appropriate error.
**kwargs -> to be absorb all the unwanted named/keyword parameters for called function. There should be no other keyword parameter passed then the specified ones in function signature.
Return -> list of number raised to the power of numbers between start and end.
### 3. polygon_area(length, *args, sides = 3, **kwargs)
This function returns area for the polygons between sides from 3 to 6
parameters
length -> mandatory positional parameter to pass length of side
*args -> absorbs all other positional parameters. There should be no more positional parameter passed then the specified ones in function signature.
sides = 3 -> optional/default keyword argument. This is number of sides for the polygon.
**kwargs -> absorbs all other named/keyword parameters. There should be no other keyword parameter passed then the specified ones in function signature.
Return -> Area of polygon
### 4. temp_converter(temp, *args, temp_given_in = 'f', **kwargs)
This function converts the temprature from Franehite to Celsius or Celsiuc to Faranhite
parameters
temp -> mandatory positional parameter to pass the temprature value
*args -> absorbs all other positional parameters. There should be no more positional parameter passed then the specified ones in function signature.
temp_given_in = 3 -> optional/default keyword argument. This is unit of temprature.
**kwargs -> absorbs all other named/keyword parameters. There should be no other keyword parameter passed then the specified ones in function signature.
Return -> Temp is other unit
### 5. speed_converter(speed, *args, dist='km', time='min', **kwargs) 
This function converts the speed from KMPH to specified units by the user
parameters
speed -> mandatory positional parameter to pass the speed value
*args -> absorbs all other positional parameters. There should be no more positional parameter passed then the specified ones in function signature.
dist = 'km' -> optional/default keyword argument. This is unit of distance. possible values km/m/ft/yrd 
time = 'min' -> optional/default keyword argument. This is unit of temprature. possible values ms/s/min/hr/day
**kwargs -> absorbs all other named/keyword parameters. There should be no other keyword parameter passed then the specified ones in function signature.
Return -> speed in given unit 

# Below are test cases functions in test_session5.py file. Total 48 test cases. 

## 1. test_readme_exists : 
Test for readme exists

## 2. test_readme_contents : 
Test for readme contents are mor than 500 words

## 3. test_readme_proper_description : 
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting : 
Test for readme formatting

## 5. test_indentations : 
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters : 
Test for no function is with capitals in source code

## 7. test_time_it_print : 
Test time it by calling print multiple times and a non zero avg time for function calls is received 

## 8. test_time_it_squared_power_list : 
Test time it by calling squared_power_list multiple times and a non zero avg time for function calls is received 

## 9. test_time_it_polygon_area : 
Test time it by calling polygon_area multiple times and a non zero avg time for function calls is received 

## 10. test_time_it_temp_converter : 
Test time it by calling temp_converter multiple times and a non zero avg time for function calls is received 

## 11. test_time_it_speed_converter : 
Test time it by calling speed_converter multiple times and a non zero avg time for function calls is received 

## 12. test_time_it_no_args : 
Test time_it with no arguments 

## 13. test_time_it_incorrect_pos_args : 
Test time_it with non existing positional arguments

## 14. test_time_it_zero_rep : 
est time_it with zero repetation. Should return 0 avg time

## 15. test_squared_power_list_no_args : 
Test squared_power function for no mandatory positional arguments

## 16. test_squared_power_list_incorrect_pos_args : 
Test squared_power_list function for incorrect values for positional arguments

## 17. test_squared_power_list_incorrect_start__end : 
Test squared_power_list function for incorrect value to start keyword arguments

## 18. test_squared_power_list_start_gt_end : 
Test squared_power_list function for start value greater than end

## 19. test_squared_power_list_number_gt_10 : 
Test squared_power_list function for number value greater than 10

## 20. test_squared_power_list_unwanted_args : 
Test squared_power_list function for unwanted positional/keyword arguments

## 21. test_squared_power_list_output : 
Test squared_power_list function for output with multiple inputs

## 22. test_polygon_area : 
Test polygon_area function for no mandatory positional arguments

## 23. test_polygon_area_length : 
Test polygon_area function for incorrect values for positional argument length

## 24. test_polygon_area_sides : 
Test polygon_area function for incorrect value to sides keyword argument

## 25. test_polygon_area_sides_values : 
Test polygon_area function for permissible values for sides

## 26. test_polygon_area_length_values : 
Test polygon_area function for permissible values for sides

## 27. test_polygon_area_unwanted_args : 
Test polygon_area function for output with multiple inputs

## 28. test_polygon_area_output : 
Test for readme formatting

## 29. test_temp_converter : 
Test temp_converter function for no mandatory positional arguments

## 30. test_temp_converter_temp : 
Test temp_converter function for incorrect values for positional argument tem

## 31. test_temp_converter_temp_given_in : 
Test temp_converter function for incorrect value to temp_given_in keyword argument

## 32. test_temp_converter_temp_values_in_celsius : 
Test temp_converter function for permissible values for temprature in celsius

## 33. test_temp_converter_temp_values_in_fahrenheit : 
Test temp_converter function for permissible values for temprature in fahrenheit

## 34. test_temp_converter_unwanted_args : 
Test temp_converter function for unwanted positional/keyword arguments

## 35. test_temp_converter_output_in_fahrenheit : 
Test temp_converter function for output with multiple inputs in fahrenheit

## 36. test_temp_converter_output_in_celsius : 
Test temp_converter function for output with multiple inputs in celsius

## 37. test_speed_converter : 
Test speed_converter function for no mandatory positional arguments

## 38. test_speed_converter_speed : 
Test speed_converter function for incorrect values for positional argument temp

## 39. test_speed_converter_dist : 
Test speed_converter function for incorrect type of value for dist keyword argument

## 40. test_speed_converter_time : 
Test speed_converter function for incorrect type of value for time keyword argument

## 41. test_speed_converter_speed_allowed_values : 
Test speed_converter function for permissible value for speed argument

## 42. test_speed_converter_time_allowed_values : 
Test speed_converter function for permissible value for time keyword argument

## 43. test_speed_converter_dist_allowed_values : 
Test speed_converter function for permissible value for dist keyword argument

## 44. test_speed_converter_unwanted_args : 
Test speed_converter function for unwanted positional/keyword arguments

## 45. test_speed_converter_output_km_to : 
Test speed_converter function for output with multiple inputs from km/(x), x can be ms/s/min/hr/day

## 46. test_speed_converter_output_m_to : 
Test speed_converter function for output with multiple inputs from m/(x), x can be ms/s/min/hr/day

## 47. test_speed_converter_output_ft_to : 
Test speed_converter function for output with multiple inputs from ft/(x), x can be ms/s/min/hr/day

## 48. test_speed_converter_output_yrd_to : 
Test speed_converter function for output with multiple inputs from yrd/(x), x can be ms/s/min/hr/day