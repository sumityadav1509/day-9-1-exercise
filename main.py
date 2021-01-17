student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
  print(grade)
  student_grades=student_scores[grade]
  if student_grades>91 and student_grades<100:
    print("Outstanding")
  elif student_grades>81 and student_grades<90:
    print("Exceeds Expectation")
  elif student_grades>71 and student_grades<80:
    print("Acceptable")
  elif student_grades<70:
    print("Fail.")    

    

# 🚨 Don't change the code below 👇
print(student_grades)





