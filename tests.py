from main import Management_System
import unittest

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = Management_System("Dr. Smith", "Computer Science")
        
    def test_AddStudent(self):
        # Add a student and check if they were added correctly
        self.system.add_student("Jacob Atanacio", "018087563", "jacob.atanacio@sjsu.edu")
        self.assertIn("018087563", self.system.students)
        self.assertEqual(self.system.students["018087563"]["name"], "Jacob Atanacio")
        self.assertEqual(self.system.students["018087563"]["Email"], "jacob.atanacio@sjsu.edu")

    def test_getCourseInfo(self):
        # Add a student, then check the course info
        self.system.add_student("Jacob Atanacio", "018087563", "jacob.atanacio@sjsu.edu")
        self.assertEqual(self.system.getCourseInfo(), {
            'Course': "Computer Science",
            'Instructor': "Dr. Smith",
            'Students': {
                "018087563": {
                    "name": "Jacob Atanacio", "ID": "018087563", "Email": "jacob.atanacio@sjsu.edu"
                }
            },
        })

if __name__ == "__main__":
    unittest.main()
