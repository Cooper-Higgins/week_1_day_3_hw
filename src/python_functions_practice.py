def return_10():
    return 10

def add(number1, number2):
    return number1 + number2 

def subtract(number1, number2):
    return number1 - number2 

def multiply(number1, number2):
    return number1 * number2 

def divide(number1, number2):
    return number1 / number2

def length_of_string(test_string):
    return len(test_string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(number):
    months = {1 : "January", 
          2 : "February", 
          3 : "March", 
          4 : "April", 
          5 : "May", 
          6 : "June", 
          7 : "July", 
          8 : "August",
          9 : "September",
          10 : "October",
          11 : "November",
          12 : "December",
        }

    return months[number]

def number_to_short_month_name(number):
    months = {1 : "Jan", 
          2 : "Feb", 
          3 : "Mar", 
          4 : "Apr", 
          5 : "May", 
          6 : "Jun", 
          7 : "Jul", 
          8 : "Aug",
          9 : "Sep",
          10 : "Oct",
          11 : "Nov",
          12 : "Dec",
        }
    
    return months[number]

def volume_of_cube(side_length):
    cube_volume = side_length ** 3
    return cube_volume

def string_reversed(test_string): 
    reverse_string = test_string [::-1]
    return reverse_string

def farenheit_conversion(temp):
    celsius = (temp - 32) * (5.0 / 9.0)
    return celsius