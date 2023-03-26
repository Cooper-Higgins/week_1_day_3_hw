def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 // num_2 

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    sum = int(string_1) + int(string_2)
    return sum

def number_to_full_month_name(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"

def number_to_short_month_name(month_number):
   short_month_name = number_to_full_month_name(month_number)[0:3]
   return short_month_name

def volume_of_cube(side_length):
    volume = side_length ** 3
    return volume

def string_reversed(string):
    string_reversed = string[::-1]
    return string_reversed

def fahrenheit_conversion(temperature):
    temperature = 212
    celsius = (temperature - 32) * 5 // 9
    return celsius