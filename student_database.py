"""
Activity 08 - File 1: Student Database
Difficulty: Beginner
Focus: Basic dictionary operations (create, access, modify)
Estimated Time: 8-10 minutes

Complete the TODO comments below to create a simple student database system.
"""

def create_student_record():
    """
    Create and return a dictionary representing a student record.
    
    TODO: Create a dictionary with the following keys and sample values:
    - "name": "Alex Johnson"
    - "student_id": "12345"
    - "major": "Computer Science"
    - "year": 2
    - "gpa": 3.7
    """
    # Your code here
    student = {}
    
    return student

def display_student_info(student):
    """
    Display student information in a formatted way.
    
    TODO: Print the student information using the following format:
    "Student: [name], ID: [student_id], Major: [major], Year: [year], GPA: [gpa]"
    """
    # Your code here
    pass

def update_student_gpa(student, new_gpa):
    """
    Update the student's GPA.
    
    TODO: Update the "gpa" key in the student dictionary with the new_gpa value
    """
    # Your code here
    pass

def add_student_courses(student, courses_list):
    """
    Add a new key "courses" to the student dictionary with a list of courses.
    
    TODO: Add a "courses" key to the student dictionary with the courses_list as the value
    """
    # Your code here
    pass

def get_student_info(student, key):
    """
    Safely get information from the student dictionary.
    
    TODO: Use the .get() method to return the value for the given key.
    If the key doesn't exist, return "Information not available"
    """
    # Your code here
    return None

# Test your functions (don't modify this part)
if __name__ == "__main__":
    print("=== Student Database System ===")
    
    # Test creating a student record
    print("1. Creating student record...")
    student = create_student_record()
    print(f"Student record created: {student}")
    
    # Test displaying student info
    print("\n2. Displaying student information...")
    display_student_info(student)
    
    # Test updating GPA
    print("\n3. Updating GPA...")
    update_student_gpa(student, 3.9)
    print(f"Updated GPA: {student.get('gpa')}")
    
    # Test adding courses
    print("\n4. Adding courses...")
    courses = ["CS100", "MATH201", "PHYS101"]
    add_student_courses(student, courses)
    print(f"Courses added: {student.get('courses')}")
    
    # Test safe information retrieval
    print("\n5. Testing safe information retrieval...")
    print(f"Student name: {get_student_info(student, 'name')}")
    print(f"Student email: {get_student_info(student, 'email')}")
    
    print("\n=== All tests completed! ===")