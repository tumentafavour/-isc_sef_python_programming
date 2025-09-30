"""
Module: student_grades

This module defines a dictionary of students with their numeric scores
and provides a function to calculate corresponding letter grades
based on a standard grading scale.

Grading scale:
    90 and above   -> A
    80 - 89        -> B
    70 - 79        -> C
    60 - 69        -> D
    Below 60       -> F
"""

# Dictionary containing student names and their corresponding scores
students = {
    "Chida": 70,
    "Olamide": 85,
    "Aisha": 90,
    "David": 65,
    "Esi": 88,
    "Paul": 60,
}


def calculate_grades(student_marks):
    """
    Calculate letter grades for each student based on numeric scores.

    Args:
        student_marks (dict): A dictionary with student names as keys and
                              scores as values.

    Returns:
        dict: A dictionary with student names as keys and letter grades as values.
    """
    grades = {}

    for name, score in student_marks.items():
        # Determine the grade based on the score
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    return grades


if __name__ == "__main__":
    # Calculate and print the grades for the students
    final_grades = calculate_grades(students)
    print(final_grades)
