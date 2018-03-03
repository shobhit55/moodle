Database Model:

	Users:
		1.Professor(username=prof_i, password = pass_prof_i)
		2.Student(username=student_i, password = pass_stud_i)
		3.Admin(username=admin, password=admin)

	Course: course_code, course_name, user(people registered in that course)

	Message: message_body, course(which course's message), user(users who see this message)

Access Control: There is a single login window for all users.
		A function login_success in views.py of accounts app, checks which type of user is 		this and takes user to desired page.
		There is a logout button on each page which logs user out.