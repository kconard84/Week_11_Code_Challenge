# CIS 105 - Dictionaries and Data Structures: Quiz and Code Challenge

## Make This Repo Yours

1. Click the **Fork** button at the top right of this page. This creates your own copy of the repository under your GitHub account.
2. In your fork, click on `README.md`, then click the pencil icon to edit it.
3. Fill in your information below and answer every quiz question in this file, right where it says **Your answer:**.
4. Commit your changes (the green **Commit changes** button at the bottom of the edit page).
5. Complete the code challenge in the file `gradebook_challenge.py` in this same repository. You can edit it in the browser or download it and work in your usual editor, then upload the finished file.
6. When everything is done, copy the web address (URL) of your forked repository and submit that link on Moodle.

Name: Keegan Conard
Section: CIS 105
Date: 11/11/26

---

## Part 1: Quiz (50 points, 5 points each)

Answer each question in your own words or with the exact output, as asked. Write your answer on the line under each question.

**1.** A dictionary stores data as key-value pairs. Write one line of Python that creates a dictionary named `student` with the keys `"name"` and `"major"` and values of your choosing.

Your answer: student = {"name": "Jennifer", "major": "Finance"}

**2.** What is the output of this code?

```python
grades = {"quiz1": 85, "quiz2": 92, "quiz3": 78}
print(grades["quiz2"])
```

Your answer: 92

**3.** What is the difference between `grades["quiz4"]` and `grades.get("quiz4")` when the key `"quiz4"` does not exist in the dictionary?

Your answer: grades["quiz4"] will return an error message when it is run in the terminal but "grades.get("quiz4") will print "None" instead of an error.

**4.** Write the line of code that adds a new key `"quiz4"` with the value 88 to the `grades` dictionary above. Then write the line that changes `"quiz1"` to 90.

Your answer: grades = {"quiz1": 85, "quiz2": 92, "quiz3": 78, "quiz4": 88}
grades["quiz1"] = 90
print(grades)

**5.** What do the dictionary methods `.keys()`, `.values()`, and `.items()` each return?

Your answer: keys() returns a list of the dictionary's keys, values() returns all of the values in the dictionary and items() returns a view object.

**6.** In one or two sentences each, explain the main difference between a list, a tuple, and a set. When would you choose each one?

Your answer: A list is a collection of ordered, mutable elements that can hold a variety of data types. It is mostly used if you need to add, remove, or insert elements into a program often. A tuple is an ordered, immutable collection of elements that is mostly used when data should not be modified after creation. And a set is an unordered collection of unique elements that is best used to remove duplicates automatically. 

**7.** True or false, and explain why: in Python, the expression `"quiz1" in grades` checks whether `"quiz1"` is one of the values in the dictionary.

Your answer: False. It checks whether "quiz1" is a key in the dictionary and not a value

**8.** What is the output of this code?

```python
student = {"name": "Alex", "courses": {"current": "CIS 105", "credits": 3}}
print(student["courses"]["current"])
```

Your answer: CIS 105

**9.** Name two different ways to remove the key `"quiz3"` from the `grades` dictionary. What is one difference between them?

Your answer: Two ways to remove the key are by using pop() or del, and they are different because pop() returns the removed value while del simply deletes the key.

**10.** What does `len(grades)` return for the dictionary in Question 2, and what exactly is it counting?

Your answer: It returns "3" because there are 3 key pairs in the dictionary.

---

## Part 2: Code Challenge (50 points)

Open `gradebook_challenge.py` in this repository. You will build a small grade book program that stores student names as dictionary keys and each student's list of test scores as the value.

The file contains starter code with five functions to complete where you see `# TODO`:

1. `add_student(book, name)` - adds a new student with an empty score list. If the student is already in the grade book, print a message saying so and change nothing.
2. `add_grade(book, name, grade)` - adds a score to a student's list. If the student is not in the grade book yet, add the student first, then the score.
3. `student_average(book, name)` - returns the average of a student's scores. Use `.get()` so the function returns `None` instead of crashing if the student is not found.
4. `top_student(book)` - returns the name of the student with the highest average score.
5. `print_report(book)` - prints every student, their scores, and their average, one student per line, using a loop over `.items()`.

The bottom of the file has test code that is already written for you. Do not change the test code. When your functions are correct, running the file produces exactly this output:

```
Alex: [90, 85, 95] Average: 90.0
Jordan: [70, 80] Average: 75.0
Taylor: [100, 95, 90, 85] Average: 92.5
Top student: Taylor
```

### Rules

- Work only inside the five TODO functions. Do not change the test code at the bottom of the file.
- Use a dictionary as the main data structure. Solutions that store the grade book as separate variables will not receive credit.
- Your code must run with no errors from start to finish.

### How You Are Graded

- Quiz answers complete and correct: 50 points
- Each challenge function working correctly: 8 points each (40 points)
- Code runs cleanly and matches the expected output: 10 points

### Submitting

Submit the URL of your forked repository on Moodle. Make sure your repository is public, or I cannot see it to grade it.
