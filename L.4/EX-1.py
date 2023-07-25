first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
student_id_number = input('Enter your student ID number:')

print('Your system login name is:', (first_name[0:3])+(last_name[0:3])+(student_id_number[-3:len(student_id_number)]))