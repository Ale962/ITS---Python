# Optional Exercise 1

'''
1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.

'''

def StudentsDict() -> dict:

    students_dict : dict = {}

    while True:

        add_student = input("Want to add a new student? (Y or N)")

        if add_student.upper() == "Y":

            student_name = input("Write the student name: ")
            students_dict[student_name] = {}

            while True:

                add_subject = input("Want to add a vote? (Y or N): ")

                if add_subject.upper() == "Y":

                    subject = input("Write the subject here: ")
                    vote: float = float(input("Write the vote here"))
                    students_dict[student_name][subject] = vote

                else:
                    break
        
        else:
            break

    return students_dict


def StudentAverage(student: str, votes: list[float]) -> None:

    if len(votes) > 0:
        average = sum(votes) / len(votes)
    else:
        raise ValueError("Can not calculate the avarage because there aren't any votes")

    if average >= 60:
        print(f"The student {student} passed the exam with an average of {average}")
    else:
        print(f"The student {student} failed to pass the exam with an average of {average}")


def StudentAverageDict(dict: dict[str, dict[str, float]]):

    for s, d in dict.items():
        if len(d.keys()) >= 0:
            average_dict = sum(d.values()) / len(d.values())
        else:
            raise ValueError("Given number of subject insufficient to make an average, can't divide for 0!")

        if average_dict >= 60:
            print(f"The student {s} passed the exam with an average of {average_dict}")
        else:
            print(f"The student {s} failed to pass the exam with an average of {average_dict}")


def StudentAverageDict2(dict: dict[str, dict[str, float]]):

    for s, d in dict.items():
        StudentAverage(s, list(d.values()))

if __name__ == "__main__":
    StudentAverage("Alessio", [85, 67, 57.9, 78.5, 98.3])
    StudentAverage("Marco", [85])
    students_data = {
    "Rachele": {"Math": 80, "Science": 70, "History": 60},
    "Luca": {"Math": 50, "Science": 40},
    "Alessio": {"Math": 90, "Science": 95, "History": 100, "Art": 85}
    }

    print("\nUsing StudentAverageDict:")
    StudentAverageDict(students_data)

    print("\nUsing StudentAverageDict2:")
    StudentAverageDict2(students_data)