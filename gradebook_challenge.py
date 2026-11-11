# CIS 105 - Code Challenge: Grade Book
# Name: Keegan Conard
# Section: CIS 105
#
# Complete the five functions below where you see # TODO.
# Do not change the test code at the bottom of the file.
#
# The grade book is a dictionary:
#   keys   = student names (strings)
#   values = lists of test scores (numbers)
# Example: {"Alex": [90, 85, 95], "Jordan": [70, 80]}


def add_student(book, name):
    """Add a new student with an empty score list.
    If the student is already in the book, print a message and change nothing."""
    if name in book:
        print(f"Student '{name}' already exists in the grade book.")
    else:
        book[name] = []
    pass


def add_grade(book, name, grade):
    """Add a score to a student's list.
    If the student is not in the book yet, add the student first, then the score."""
    if name not in book:
        add_student(book, name)
    book[name].append(grade) 
    pass


def student_average(book, name):
    """Return the average of a student's scores.
    Use .get() so this returns None instead of crashing
    if the student is not in the book."""
    scores = book.get(name)
    if not scores:
        return None
    return sum(scores) / len(scores)
    pass


def top_student(book):
    """Return the name of the student with the highest average score."""
    best_name = None
    best_average = None

    for name in book:
        average = student_average(book, name)
        if average is not None and (best_average is None or average > best_average):
            best_name = name
            best_average = average

    return best_name
    pass


def print_report(book):
    """Print every student, their scores, and their average,
    one student per line. Loop over the dictionary with .items()."""
    for name, scores in book.items():
        average = student_average(book, name)
        average_text = "N/A" if average is None else f"{average:.1f}"
        print(f"{name}: {scores} Average: {average_text}")
    pass

# ---------------- TEST CODE - DO NOT CHANGE BELOW THIS LINE ----------------

gradebook = {}

add_student(gradebook, "Alex")
add_student(gradebook, "Jordan")
add_student(gradebook, "Taylor")

add_grade(gradebook, "Alex", 90)
add_grade(gradebook, "Alex", 85)
add_grade(gradebook, "Alex", 95)

add_grade(gradebook, "Jordan", 70)
add_grade(gradebook, "Jordan", 80)

add_grade(gradebook, "Taylor", 100)
add_grade(gradebook, "Taylor", 95)
add_grade(gradebook, "Taylor", 90)
add_grade(gradebook, "Taylor", 85)

print_report(gradebook)
print("Top student:", top_student(gradebook))

# Expected output:
# Alex: [90, 85, 95] Average: 90.0
# Jordan: [70, 80] Average: 75.0
# Taylor: [100, 95, 90, 85] Average: 92.5
# Top student: Taylor
