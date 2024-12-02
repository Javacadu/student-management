# Student Management System

This project is a Python-based Student Management System with a graphical user interface (GUI) built using Tkinter. It allows users to manage students, assignments, grades, and project teams. Data is stored and updated in real-time in a CSV file for persistence.

---

## Features
- **Add/View Students**: Manage student details including name and email.
- **Add/View Assignments**: Track assignment title, points, category, and due date.
- **Create/View Project Teams**: Organize students into teams with project titles and members.
- **Grade Management**:
  - Assign grades to students for specific assignments.
  - Calculate and display final grades.
  - Export grades to a CSV file.
- **Persistent Data**: All information is stored in `gradebook.csv` for easy access and analysis.

---

## How to Run the Code

Use an IDE that can run pyhton code

### Step 1: Clone the Repository
- Open your terminal or command prompt and run the following commands:
```bash
git clone https://github.com/your-repo/student-management.git
cd student-management
```

## Step 2: Set up and activate a python envirironment

```bash
python -m venv .venv

#Windows
.venv\Scripts\activate

#MacOS
source .venv/bin/activate
```

## Step 3 Install Dependancies

pandas: For working with CSV files.
matplotlib: For visualizing grades with graphs.

## Step 4 Execute Code

- Run the interface.py file