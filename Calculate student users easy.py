def calculate_student_users(total_users, staff_users):
    non_teaching_staff_users = staff_users // 3
    student_users = total_users - (staff_users + non_teaching_staff_users)
    return student_users

total_users = int(input("Total Users: "))
staff_users = int(input("Staff Users: "))

student_users = calculate_student_users(total_users, staff_users)
print(f"Student Users: {student_users}")
