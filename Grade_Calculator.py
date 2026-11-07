
grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

while True:
    try:
        courses_num = int(input("How many courses: "))
        if courses_num <= 0:
            print("Enter a number greater than 0.")
            continue
        break
    
    except ValueError:
        print("That's not a valid entry")

count = 0
total_units = 0
total_points = 0

while count < courses_num:
    course_entry = input("Enter Course (s = restart, = = finish): ")
    
    if course_entry == 's':
        count = 0
        total_units = 0
        total_points = 0
        print ("Restart course entry")
        continue
    
    if course_entry == '=':
        break
        
    
    course_grade = input("Grade: ").upper()
    
    if course_grade not in ("A", "B", "C", "D", "E", "F"):
        print("Invalid grade, enter A to F")
        continue
    
    try:
        course_unit = int(input("Unit: "))
    except ValueError:
        print("Invalid Entry")
        continue

    if course_unit <= 0:
        print("Invalid Entry")
        continue
   
    
    count += 1
    total_units += course_unit
    total_points += grade_points[course_grade] * course_unit
    
print (f"you entered {count} entries")
print(f"Total units: {total_units}")

if total_units > 0:
    gpa = total_points / total_units
    print(f"GPA: {gpa:.2f}")
else:
    print("No courses entered")