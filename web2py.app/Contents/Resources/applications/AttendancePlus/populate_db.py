## Populate DB Script

## clear database
for table in db.tables():
	try:
		db(db[table].id>0).delete()
		print "Cleared",table
	except Exception, e:
		print "Couldn't clear",table

## create 5 students
db.users.insert(
	first_name="Abhishek",
	last_name="Kumar",
	email="abhishek.iitd16@gmail.com",
	username="cs5110272",
	entry_no="2011CS50272",
	type_=0,
	password="1",
)

db.users.insert(
	first_name="Sharad",
	last_name="Maheshwari",
	email="cs5110295@cse.iitd.ac.in",
	username="cs5110295",
	entry_no="2011CS50295",
	type_=0,
	password="1",
)

db.users.insert(
	first_name="Rachit",
	last_name="Arora",
	email="rachitarora@gmail.com",
	username="cs5140292",
	entry_no="2014CS50292",
	type_=0,
	password="1",
)

db.users.insert(
	first_name="Mayank",
	last_name="Gupta",
	email="gptmayank51@gmail.com",
	username="cs1110283",
	entry_no="2011CS50283",
	type_=0,
	password="1",
)

db.users.insert(
	first_name="Vivek",
	last_name="Kumar",
	email="vivekkumar@gmail.com",
	username="mt5110627",
	entry_no="2011MT50627",
	type_=0,
	password="1",
)






db.users.insert(
	first_name="Shubham",
	last_name="Jindal",
	email="cs5110300@cse.iitd.ac.in",
	username="cs5110300",
	entry_no="2011CS50300",
	type_=0,
	password="1",
)

# 4 professors
db.users.insert(
	first_name="Suresh",
	last_name="Gupta",
	email="scgupta@cse.moodle.in",
	username="scgupta",
	entry_no="scgupta",
	type_=1,
	password="1",
)

db.users.insert(
	first_name="Mausam",
	last_name="Mausam",
	email="mausam@cse.iitd.ac.in",
	username="mausam",
	entry_no="mausam",
	type_=1,
	password="1",
)

db.users.insert(
	first_name="Subodh",
	last_name="Kumar",
	email="subodh@cse.iitd.ac.in",
	username="subodh",
	entry_no="subodh",
	type_=1,
	password="1",
)

db.users.insert(
	first_name="M",
	last_name="Balakrishanana",
	email="mbala@cse.iitd.ac.in",
	username="mbala",
	entry_no="mbala",
	type_=1,
	password="1",
)


## create 9 courses
db.courses.insert(
	name="Software Engineering",
	code="csl740",
	description="Introduction to the concepts of Software Design and Engineering.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Parallel Programming",
	code="csl730",
	description="Introduction to concurrent systems and programming style.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Artificial Intelligence",
	code="csl333",
	description="Introduction to Artificial Intelligence.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Natural Language Processing",
	code="csl772",
	description="Introduction to Natural Language Processing.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Computer Graphics",
	code="csl781",
	description="Computer Graphics.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Design Practices in Computer Science",
	code="csp301",
	description="Design Practices in Computer Science.",
	credits=3,
	l_t_p="1-0-4"
)

db.courses.insert(
	name="Advanced Computer Graphics",
	code="csl859",
	description="Graduate course on Advanced Computer Graphics",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Data Structures",
	code="csl201",
	description="Introduction to Data Structures.",
	credits=4,
	l_t_p="3-0-2"
)

db.courses.insert(
	name="Cloud Computing and Virtualisation",
	code="csl732",
	description="Introduction to Cloud Computing and Virtualisation.",
	credits=4,
	l_t_p="3-0-2"
)


db.courses.insert(
	name="Embedded System Design Project",
	code="cop315",
	description="Introduction to embeded programming.",
	credits=4,
	l_t_p="0-0-8"
)


db.classrooms.insert(room="SIT Sem Hall", capacity=60)

db.semesters.insert(year_=2015, semester=1)

db.slots.insert(name="Free", days="_______")
db.registered_courses.insert(
	course = 10,
	classroom = 1,
	prof_id = 8,
	semester = 1,
	slot = 1
)

db.student_registrations.insert(student_id=1,registered_course=1)
db.student_registrations.insert(student_id=2,registered_course=1)
db.student_registrations.insert(student_id=3,registered_course=1)
db.student_registrations.insert(student_id=4,registered_course=1)
db.student_registrations.insert(student_id=5,registered_course=1)
db.student_registrations.insert(student_id=6,registered_course=1)
