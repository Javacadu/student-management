"""
TODO:
figure out how to create CSV to take from both studetns and assignemts, CSV saves all assignments and student data
Finish management system
make students inherit management system
make assignemnts and students associate with gradebook class
"""

class Management_System:
    
    def __init__(self, instructor, course):
        self.students = {}
        self.instructor = instructor
        self.course = course
        
    def add_student(self, name, student_ID, email):
        self.students[student_ID] = {"name": name, "ID": student_ID, "Email": email}
    
    def getCourseInfo(self):
        return {
            'Course': self.course,
            'Instructor': self.instructor,
            'Students': self.students,
        }

class Student(Management_System):
    def __init__():
        pass
    
    def getStudentInfo(self, student_ID):
        return self.students.get(student_ID)
    

class Assignment:
    def __init__(self, title, points, category, due):
        self.title = title
        self.points = points
        self.category = category
        self.due = due
        self.update_CSV()
        
    def update_CSV(self):
        pass        


cs22b = Management_System("AC", "CS 22B Python for Data Analytics")
cs22b.add_student("Jacob A", "001", "jatanacio@sjsu.edu")

print(cs22b.getCourseInfo())

studentInfo = Student(cs22b)



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