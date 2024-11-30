import csv
import pandas as pd
import matplotlib.pyplot as plt

class Student:
    def __init__(self, student_id, name, email, total_points=100):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.total_points = total_points
        self.assignments = {}

    def add_assignment(self, assignment, score):
        self.assignments[assignment.title] = score

    def get_final_grade(self):
        if not self.assignments:
            return 0
        return (sum(self.assignments.values()) / self.total_points) * 100

    def get_letter_grade(self):
        final_grade = self.get_final_grade()
        if final_grade >= 90:
            return 'A'
        elif final_grade >= 80:
            return 'B'
        elif final_grade >= 70:
            return 'C'
        elif final_grade >= 60:
            return 'D'
        else:
            return 'F'


class Assignment:
    def __init__(self, title, points, category, due_date):
        self.title = title
        self.points = points
        self.category = category
        self.due_date = due_date


class Gradebook:
    def __init__(self):
        self.students = {}
        self.assignments = []

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def assign_grade(self, student_id, assignment, score):
        student = self.students.get(student_id)
        if student:
            student.add_assignment(assignment, score)
            self.save_to_csv()

    def save_to_csv(self):
        # Save all student grades and assignments to CSV
        data = []
        for student in self.students.values():
            row = [student.name, student.student_id, student.email]
            row.extend([student.assignments.get(assignment.title, 0) for assignment in self.assignments])
            row.append(student.get_final_grade())
            row.append(student.get_letter_grade())
            data.append(row)

        df = pd.DataFrame(data, columns=['Name', 'ID', 'Email'] + [a.title for a in self.assignments] + ['Final Grade', 'Letter Grade'])
        df.set_index('Name', inplace=True)
        df.to_csv("gradebook.csv")

    def plot_final_grades(self):
        final_grades = {student.name: student.get_final_grade() for student in self.students.values()}
        letter_grades = {student.name: student.get_letter_grade() for student in self.students.values()}

        graph = plt.bar(final_grades.keys(), final_grades.values(), color='blue')
        for x in graph:
            height = x.get_height()
            plt.text(x.get_x() + x.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10, color='black')

        plt.xlabel('Students')
        plt.ylabel('Final Grade')
        plt.title('Final Grades of Students')
        plt.show()


class ProjectTeams:
    def __init__(self, title, members=""):
        self.title = title
        self.members = members  # Now a single string to hold all members.

    def add_member(self, student_name):
        """Add a new member to the project as a string."""
        if self.members:
            self.members += ", " + student_name  # Append new member with a comma
        else:
            self.members = student_name  # First member, no comma needed

    def get_team_info(self):
        return {'Title': self.title, 'Members': self.members}

"""
Example
student1 = Student(1, 'Fatema', 300)
student2 = Student(2, 'Jacob', 300)

assignment1 = Assignment('Midetm 1', 100, 'Exams', '1/1/2024')
assignment2 = Assignment('Hands on 1', 100, 'HW', '1/2/2024')
assignment3 = Assignment('Project Proposal', 100, 'Project', '1/3/2024')

gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_student(student2)

gradebook.add_assignment(assignment1)
gradebook.add_assignment(assignment2)
gradebook.add_assignment(assignment3)

radebook.add_grades(student1, assignment1, 85)
gradebook.add_grades(student1, assignment2, 92)
gradebook.add_grades(student1, assignment3, 78)

gradebook.add_grades(student2, assignment1, 90)
gradebook.add_grades(student2, assignment2, 88)
gradebook.add_grades(student2, assignment3, 91)

gradebook.create_csv()

gradebook.plot_final_grades()
"""



'''
class Management_System:
    def __init__(self, students, instructor, course):
        self.students = {}
        self.instructor = instructor
        self.course = course
        
    def add_student(self, name, id_Number, email):
        self.students[studnet_ID] = [name, id_Number, email]
        


class Assignment:
    def __init__(self, title, points, category, due):
        """creates a new assignment , assignment category, 
        set points assignemnt is worth, due date
        
        TODO: add a value to show if a student has submitted the assignment, 
                not submitted, or submitted late"""
                
        self.title = title
        self.points = points
        self.category = category
        self.due_date = due

class Students(Management_System):
    
    def __init__(self, name, idNum, email):
        """student name, ID, overall course grade
            TODO: calculate overall grade        
        """
        self.name = name
        self.idNum = idNum
        self.grades = {}  # This will hold all scores
        self.email = email

    def update_scores(self, assignment, score):
        """Update scores will add/update assignment score
        
        Should this be a gradebook class instead or should we make a gradebook???"""
        
        self.grades[assignment.title] = {
            'Assignment': assignment.title,
            'Score': score,
            'Total Points': assignment.points,
            'Category': assignment.category,
            'Due Date': assignment.due_date
        }

    def get_score(self, assignment_title):
        """will display assignment info """
        
        return self.grades.get(assignment_title, "No recorded score")

    def get_student_info(self):
        """returns student name,id,email"""
        return {
            'Student': self.name,
            'ID': self.id_Number,
            'Email': self.email
        }

class Score:
    def __init__(self, student, assignment, score):
        """class that scores a student's assignment and 
        records it to the student object"""
        self.student = student
        self.assignment = assignment
        self.score = score
        self.record_score() #runs the function each time a new score is submitted

    def record_score(self):
        """records score to the student class"""
        self.student.update_scores(self.assignment, self.score)

class Project:
    def __init__(self, title, grade):
        """ detailed overview of who is in the team, 
        project name, lists all assignments related to the project,
        displays if students have submitted,
        displays project score
        """        
        self.title = title
        self.team = [] #list of strings containing the names of team members
        self.grade = grade
        #self.proj_report (not sure how to implement this... dont thin just sub)
    
    def grade_project():
        pass
    
    def get_project_info():
        return {
            'Title:',
            'Team Members:',
            'Grade:'
        }

student1 = Student("test", 12345, "test@sjsu.com")

assignment1 = Assignment("Math Test", 100, "Exam", "2023-11-01")
score1 = Score(student1, assignment1, 88)


print(student1.get_score("Math Test"))
print(student1.get_student_info())
score1 = Score(student1, assignment1, 90)
print(student1.get_score("Math Test"))'''