"""
Activity 08 - File 3: Grade Calculator
Difficulty: Advanced
Focus: Nested dictionaries and complex operations
Estimated Time: 12-15 minutes

Complete the TODO comments below to create a grade analysis system.
"""

def create_class_gradebook():
    """
    Create and return a nested dictionary representing a class gradebook.
    
    TODO: Create a dictionary with student names as keys, and each value 
    being another dictionary with subjects and grades:
    
    {
        "Emma": {"math": 95, "science": 87, "english": 92},
        "Liam": {"math": 78, "science": 94, "english": 88},
        "Sophia": {"math": 91, "science": 89, "english": 95}
    }
    """
    # Your code here
    gradebook = {}
    
    return gradebook

def add_new_student(gradebook, student_name, grades_dict):
    """
    Add a new student to the gradebook.
    
    TODO: Add the student_name as a key with grades_dict as the value
    """
    # Your code here
    pass

def calculate_student_average(gradebook, student_name):
    """
    Calculate the average grade for a specific student.
    
    TODO: Get the student's grades dictionary and calculate the average
    Return the average as a float, or None if student doesn't exist
    """
    # Your code here
    return None

def calculate_subject_average(gradebook, subject):
    """
    Calculate the average grade for a specific subject across all students.
    
    TODO: Loop through all students and collect grades for the given subject
    Calculate and return the average for that subject
    """
    # Your code here
    return None

def find_top_student_in_subject(gradebook, subject):
    """
    Find the student with the highest grade in a specific subject.
    
    TODO: Loop through all students and find who has the highest grade in the subject
    Return a tuple: (student_name, grade)
    """
    # Your code here
    return None, None

def get_students_above_average(gradebook, subject, threshold):
    """
    Find students who scored above the threshold in a subject.
    
    TODO: Return a list of student names who scored above the threshold in the subject
    """
    # Your code here
    return []

def add_subject_to_all_students(gradebook, subject, grades_list):
    """
    Add a new subject with grades to all students.
    
    TODO: Add the new subject to each student's grade dictionary
    grades_list should have the same number of grades as there are students
    """
    # Your code here
    pass

def generate_report_card(gradebook, student_name):
    """
    Generate a detailed report card for a student.
    
    TODO: Create a dictionary with:
    - "student": student_name
    - "grades": their grades dictionary
    - "average": their overall average
    - "total_subjects": number of subjects they're taking
    """
    # Your code here
    report = {}
    
    return report

def find_class_statistics(gradebook):
    """
    Calculate overall class statistics.
    
    TODO: Return a dictionary with:
    - "total_students": number of students
    - "subjects": list of all subjects
    - "class_average": overall average of all grades
    - "highest_average": highest student average
    - "lowest_average": lowest student average
    """
    # Your code here
    stats = {}
    
    return stats

# Test your functions (don't modify this part)
if __name__ == "__main__":
    print("=== Grade Calculator System ===")
    
    # Test creating gradebook
    print("1. Creating class gradebook...")
    gradebook = create_class_gradebook()
    print(f"Initial gradebook: {gradebook}")
    
    # Test adding new student
    print("\n2. Adding new student...")
    add_new_student(gradebook, "Noah", {"math": 85, "science": 92, "english": 79})
    print(f"Gradebook with new student: {gradebook}")
    
    # Test calculating student average
    print("\n3. Calculating student averages...")
    for student in gradebook.keys():
        avg = calculate_student_average(gradebook, student)
        print(f"{student}'s average: {avg:.2f}")
    
    # Test calculating subject averages
    print("\n4. Calculating subject averages...")
    subjects = ["math", "science", "english"]
    for subject in subjects:
        avg = calculate_subject_average(gradebook, subject)
        print(f"{subject.title()} class average: {avg:.2f}")
    
    # Test finding top student in each subject
    print("\n5. Finding top students in each subject...")
    for subject in subjects:
        student, grade = find_top_student_in_subject(gradebook, subject)
        print(f"Top student in {subject}: {student} with {grade}")
    
    # Test finding students above threshold
    print("\n6. Finding students above 90 in math...")
    high_performers = get_students_above_average(gradebook, "math", 90)
    print(f"Students above 90 in math: {high_performers}")
    
    # Test adding new subject
    print("\n7. Adding history grades...")
    history_grades = [88, 93, 86, 90]  # for Emma, Liam, Sophia, Noah
    add_subject_to_all_students(gradebook, "history", history_grades)
    print(f"Gradebook with history: {gradebook}")
    
    # Test generating report card
    print("\n8. Generating report card for Emma...")
    report = generate_report_card(gradebook, "Emma")
    print(f"Emma's report card: {report}")
    
    # Test class statistics
    print("\n9. Generating class statistics...")
    stats = find_class_statistics(gradebook)
    print(f"Class statistics: {stats}")
    
    print("\n=== All tests completed! ===")