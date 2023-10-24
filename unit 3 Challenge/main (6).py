
'''implement a function called sort_students that takes a list of students objects as input and sorts the
list based on their CGPA (cumulative Grade Point Average) in descending order. each student object
has the following attributes: name (string), roll_number (string), and cgpa (float. Test the function
with different input lists of student.'''


class Student:
    def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa

    @staticmethod
    def sort_students(student_list):
     sorted_students = sorted(student_list, key=lambda student:
          student.cgpa, reverse=True)
     return sorted_students
     

# Example usage:
students = [
    Student("hart", "A123", 7.0),
    Student("srikath", "A124", 8.9),
    Student("sayumya", "A125", 9.1),
    Student("manoj", "A126", 9.3),
]
sorted_students = Student.sort_students(students)

# Print the sorted students list
for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
 
