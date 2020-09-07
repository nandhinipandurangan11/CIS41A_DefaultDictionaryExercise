# CIS 41A: Default Dictionary Exercise: Nandhini Pandurangan
# Using the Dictionary Exercise, replace the dictionary with a Default Dictionary.

import csv
import collections


# Student class contains 2 strings: the first and last name of the student
class Student:

    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # defines how print() is used on Student objects
    def __str__(self):
        return self.first_name + " " + self.last_name

    # overloading the less than < operator to allow for comparison between student last names
    def __lt__(self, right):
        return self.last_name < right.last_name


class Course:

    # constructor
    def __init__(self):

        # declaring a default dictionary with default value "Student not found"
        # the reason for lambda is because the default value must be declared
        # with something that is callable
        self.default_dict = collections.defaultdict(lambda: "Student not found")

    # reader() reads the csv file
    def reader(self, csvfile):

        k = 1  # each student is assigned a number which will be used as the key for the dictionary

        for line in csv.reader(open(csvfile)):  # iterating through file contents
            st = Student(line[0], line[1])  # calls the Student constructor using the elements of line
            self.default_dict[k] = st  # storing the student object in the dictionary of students
            k += 1  # incrementing key value by 1

    # output_list() outputs the list of students in the course
    def output_list(self):
        print()
        print("---  List of students in this course:  ---")
        for i in range(1, len(self.default_dict.values()) + 1):
            print(self.default_dict[i])


# main() creates a Course object
def main():
    c = Course()
    c.reader("Students.txt")  # passing a csv file to reader()
    c.output_list()


# calling main()
main()
