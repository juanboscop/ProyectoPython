print("\nwelcome to Bosco's grade sorter app\n")

grades = []
grade1 = int(input("first grade: "))
grade2 = int(input("Second Grade: "))
grade3 = int(input("Third grade: "))
grade4 = int(input("Fourth grade: "))
grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
print(f"\nYour grades are --> {grades}\n")
grades.sort()
grades.reverse()
print(f"\nYour grades from highest to lowest is --> {grades}\n")
print("\nthe lowest 2 grades will now be dropped\n")
grades.pop(2)
grades.pop(-1)
print(f"!Congrugulations your remaining grades are --> {grades[0:2]}")


