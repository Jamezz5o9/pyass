student_record = []


def gathering_student_info():

    keep_adding_info = "y"
    count = 0
    while keep_adding_info == "y":
        name = input("Please Enter your name: ")
        first_grade = int(input("Enter math score: "))
        second_grade = int(input("Enter your eng score: "))
        total = first_grade + second_grade
        avg = total / 2
        count += 1

        student_grades = {
            "name": name,
            "first_grade": first_grade,
            "second_grade": second_grade,
            "total": total,
            "avg": avg,
            "position": count
        }

        student_record.append(student_grades)

        keep_adding_info = input("Do you want to keep adding student grade?  y/n: ")


def output_grade():
    print("#################################################################")
    print("{}{:<10s}{:<10s}{:<10s}{:<10s}{:<10s}".format("Names", "Math", "Eng", "Total", "Average", "Position"))
    for i in range(len(student_record)):
        print(student_record[i]["name"], "\t", student_record[i]["first_grade"], "\t",
              student_record[i]["second_grade"], "\t",
              student_record[i]["total"], "\t", student_record[i]["avg"], "\t", student_record[i]["position"])


def sort_student_position():
    for i in range(len(student_record)):
        for j in range(i + 1, len(student_record)):
            if student_record[j]['avg'] > student_record[i]['avg']:
                student_record[i], student_record[j] = student_record[j], student_record[i]

        for i in range(len(student_record)):
            student_record[i]['position'] = i + 1


gathering_student_info()
sort_student_position()
output_grade()