import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time
from session5 import squared_power_list
from session5 import polygon_area
from session5 import temp_converter
from session5 import speed_converter

README_CONTENT_CHECK_FOR = [
    'time_it(fn, *args, repetitions= 1, **kwargs)',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_time_it_print():
    """Test time_it with print function"""
    avg_time = session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5)
    assert avg_time, "time_it can't time print function"

def test_time_it_squared_power_list():
    """Test time_it with squared_power function"""
    avg_time = session5.time_it(squared_power_list, 2, start=0, end=5, repetitions=5)
    assert avg_time, "time_it can't time squared_power_list function"

def test_time_it_polygon_area():
    """Test time_it with polygon_area function"""
    avg_time = session5.time_it(polygon_area, 15, sides=3, repetitions=10)
    assert avg_time, "time_it can't time polygon_area function"

def test_time_it_temp_converter():
    """Test time_it with temp_converter function"""
    avg_time = session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100)
    assert avg_time, "time_it can't time temp_converter function"

def test_time_it_speed_converter():
    """Test time_it with speed_converter function"""
    avg_time = session5.time_it(speed_converter, 100, dist='km', time='min', repetitions=200)
    assert avg_time, "time_it can't time speed_converter function"
