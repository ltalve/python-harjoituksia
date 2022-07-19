def course_grading():
  if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_information = input("Course information: ")
  else:
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_data = "exam_points2.csv"
    course_information = "course2.txt"
  
  names = {}
  exercises = {}
  exam_points = {}
  course_info = ()

  def clean_list(list: list):
    result =[]
    for item in list:
      result.append(int(item.strip()))
    return result
  
  def calculate_points(excercises_done, exam_points):
    # print("exercises done:", excercises_done, "exam points:", exam_points)
    if excercises_done >= 0 and excercises_done < 10/100*40:
      overall_points = 0 + exam_points 
    if excercises_done >= 10/100*40 and excercises_done < 20/100*40:
      overall_points = 1 + exam_points
    if excercises_done >= 20/100*40 and excercises_done < 30/100*40:
      overall_points = 2 + exam_points
    if excercises_done >= 30/100*40 and excercises_done < 40/100*40:
      overall_points = 3 + exam_points
    if excercises_done >= 40/100*40 and excercises_done < 50/100*40:
      overall_points = 4 + exam_points
    if excercises_done >= 50/100*40 and excercises_done < 60/100*40:
      overall_points = 5 + exam_points
    if excercises_done >= 60/100*40 and excercises_done < 70/100*40:
      overall_points = 6 + exam_points
    if excercises_done >= 70/100*40 and excercises_done < 80/100*40:
      overall_points = 7 + exam_points
    if excercises_done >= 80/100*40 and excercises_done < 90/100*40:
      overall_points = 8 + exam_points
    if excercises_done >= 90/100*40:
      overall_points = 9 + exam_points
    if excercises_done == 40:
      overall_points = 10 + exam_points
    exercise_points = overall_points - exam_points
    # print("overall points:", excercises_done, ",", exam_points, "=>", overall_points)
    return calculate_grade(overall_points, exercise_points)

  def calculate_grade(overall_points, exercise_points):
    grade = 0
    if overall_points > 14 and overall_points <= 17:
      grade = 1
    elif overall_points > 17 and overall_points <= 20:
      grade = 2
    elif overall_points > 20 and overall_points <= 23:
      grade = 3
    elif overall_points > 23 and overall_points <= 27:
      grade = 4
    elif overall_points > 27:
      grade = 5
    # print("overall points:", overall_points, "exercise points:", exercise_points, "grade:", grade)
    return grade, exercise_points, overall_points

  # read names from file
  with open(student_info) as new_file:
    for line in new_file:
      parts = line.split(";")
      id = parts[0]
      if id == "id":
        continue
      names[id] = f"{parts[1]} {parts[2].strip()}"

  # read exercises from file
  with open(exercise_data) as new_file:
    for line in new_file:
      parts = line.split(";")
      id = parts[0]
      if id == "id":
        continue
      cleaned_list = clean_list(parts[1:])
      exercises[id] = cleaned_list

  # read final exam result from file 
  with open(exam_data) as new_file:
    for line in new_file:
      parts = line.split(";")
      id = parts[0]
      if id == "id":
        continue
      cleaned_list = clean_list(parts[1:])
      exam_points[id] = sum(cleaned_list)

  # read course information from file
  with open(course_information) as new_file:
    course_name = ""
    course_credits = 0
    for line in new_file:
      if "name" in line:
        course_name = line[6:].strip()
      if "credits" in line:
        course_credits = line[14:].strip()
    course_info = course_name, course_credits
      

  def print_results_to_console(names: dict, exercises: dict, exam_points: dict, course_info: tuple):
    first_line = f"{course_info[0]}, {course_info[1]} credits"
    print(first_line)
    print(len(first_line) * "=")
    print(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
    for id, name in names.items():
      if id in exercises:
        points_from_exercises = sum(exercises[id])
        exec_nbr = sum(exercises[id])
        exec_pts = calculate_points(points_from_exercises, exam_points[id])[1]
        exm_pts = exam_points[id]
        tot_pts = calculate_points(points_from_exercises, exam_points[id])[2]
        grade = calculate_points(points_from_exercises, exam_points[id])[0]
        print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")
  
  print_results_to_console(names, exercises, exam_points, course_info)


  # Printing statistics to file ->

  def print_results_to_file(names: dict, exercises: dict, exam_points: dict, course_info: tuple):
    with open("results.txt", "w") as new_file:
      with open("results.csv", "w") as second_file:
        first_line = f"{course_info[0]}, {course_info[1]} credits \n"
        new_file.write(first_line)
        new_file.write((len(first_line) - 2) * "=" + "\n")
        new_file.write(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade \n")
        for id, name in names.items():
          if id in exercises:
            points_from_exercises = sum(exercises[id])
            exec_nbr = sum(exercises[id])
            exec_pts = calculate_points(points_from_exercises, exam_points[id])[1]
            exm_pts = exam_points[id]
            tot_pts = calculate_points(points_from_exercises, exam_points[id])[2]
            grade = calculate_points(points_from_exercises, exam_points[id])[0]
            new_file.write(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}\n")
            second_file.write(f"{id};{name};{grade}\n")
  
  print_results_to_file(names, exercises, exam_points, course_info)


course_grading()
