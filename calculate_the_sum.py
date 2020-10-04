"""calculate_the_sum.py"""
import numpy

def read_numbers_from_file():
    file = open("file.txt")
    return list(file.read())


def calculate_the_sum_of_evens_in_a_list(list_of_numbers):
    return sum([n for n in list_of_numbers if not n % 2])


def write_list_of_numbers_to_file(list_of_numbers):
    file = open("output.txt", "w")
    list_of_numbers_as_string = ", ".join(", ".join(str(n) for n in list_of_numbers))
    average_as_string = "Avg:" + str(calculate_the_average_of_numbers_in_a_list(list_of_numbers))
    sum_of_evens_as_string = str(calculate_the_sum_of_evens_in_a_list(list_of_numbers))
    output_string = list_of_numbers_as_string + "\n" + average_as_string + "\n" + sum_of_evens_as_string
    file.write(output_string)


def calculate_the_average_of_numbers_in_a_list(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)


def calculate_the_product(list_of_numbers):
    return numpy.prod(list_of_numbers)

def print_number_to_standard_output(msg, number):
    print(f"{msg}:{number}")


def calculate_the_product_of_evens(list_of_numbers):
    return calculate_the_product([n for n in list_of_numbers if not n % 2])