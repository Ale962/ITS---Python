# Lesson 4 Exercise 8.16

'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

import functions

from functions import car_information2

print(car_information2("Ferrari", "F488", 2020, "Italia"))

from functions import describe_city as dc

dc("Roma", "Italia")

import car_function as cf

from functions import *

display_message()

describe_city("Roma", "Italia")

print(car_information2("Ferrari", "F488", 2020, "Italia"))