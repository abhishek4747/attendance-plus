def index():
	return dict(msg="Hello world")

def test():
	return dict(success=True)

def getPrintsOfClass():
	if (len(request.args)==0):
		raise HTTP(404, "Course code not provided")
	class_code = str(request.args[0]).lower()
	if not current_valid_class_code(class_code):
		raise HTTP(201, "Invalide class code")
	if (len(request.args)>2):
		try:
			year = int(request.args[1])
			sem_num = int(request.args[2])
			sem = db(db.semesters.year_==year)(db.semesters.semester==sem_num).select().first()
		except:
			raise HTTP(202, "Invalid semester")
	else:
		sem = get_current_semester()
	course = db(db.courses.code==class_code).select().first()
	registered_course = db(db.registered_courses.course==course.id)(db.registered_courses.semester==sem.id).select().first()
	students = db(db.student_registrations.registered_course==registered_course.id).select()

	prints = {}
	for student in students:
		prints[db(db.users.id==student.id).select().first().entry_no] = db(db.fingerprints.user_id==student.id).select().first()
	return dict(prints=prints)


def markAttendanceOfStudents():
	if (len(request.args)==0):
		raise HTTP(404, "Course code not provided")
	class_code = str(request.args[0]).lower()
	if not current_valid_class_code(class_code):
		raise HTTP(201, "Invalide class code")
	if (len(request.args)>2):
		try:
			year = int(request.args[1])
			sem_num = int(request.args[2])
			sem = db(db.semesters.year_==year)(db.semesters.semester==sem_num).select().first()
		except:
			raise HTTP(202, "Invalid semester")
	else:
		sem = get_current_semester()
	course = db(db.courses.code==class_code).select().first()
	registered_course = db(db.registered_courses.course==course.id)(db.registered_courses.semester==sem.id).select().first()
	from datetime import datetime
	if request.vars['timestamp']:
		timestamp = datetime.strptime(str(request.vars['timestamp'])+" 08:00", '%d-%m-%Y %H:%M')
	else:
		timestamp = datetime.now()
	db(db.lectures.course==registered_course)(db.lectures.time_==timestamp).delete()
	lecture = db.lectures.insert(course=registered_course.id, time_=timestamp)
	if request.vars['students']:
		students = map(lambda x: x.strip().upper(), str(request.vars['students']).split(','))
		for student in students:
			stu = student_by_entryno(student.upper())
			if stu:
				db.attendance.insert(student_id= stu, lecture= lecture)
		return dict(success=True, msg="Attendance marked for %d students"% len(students))
	else:
		raise HTTP(404, "Students list not provided")
	
	
	

