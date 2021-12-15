courses = [ "CS112" , "EE121" , "MT102" , "PH103" , "ME102" , "HM102" , "CS112L" , "EE121L" ]
grades  = [ 3.67 , 2.67 , 1.00 , 3.33 , 2.33 , 3.67 , 3.67 , 2.00 ]

coursegrades = {courses[i]:grades[i] for i in range(len(courses))}

search = input("ENTER COURSE CODE FOR GRADEPOINT SEARCH :\n")

print(f"Gradepoint = {coursegrades[search]} ")