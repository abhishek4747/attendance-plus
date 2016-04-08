def set_static_var(name, int_value, str_value):
	db.static_vars.insert(name=name, int_value=int_value, str_value=str_value)
	
def update_static_var(name, int_value, str_value):
	db(db.static_vars.name==name).update(int_value=int_value, str_value=str_value)

def get_static_var(name, default):
	v = db(db.static_vars.name==name).select().first()
	if v:
		return v.int_value, v.str_value
	else:
		return default, str(default)

int_value = 0
str_value = 1

def student_by_entryno(eno):
	student = db(db.users.entry_no==str(eno)).select()
	if (len(student)>0):
		return student.first()
	return None

def get_current_year():
	return get_static_var("current_year", 2015)[int_value]

def get_current_sem():
	return get_static_var("current_sem", 1)[int_value]


def get_current_semester():
	return db(db.semesters.year_==get_current_year())(db.semesters.semester==get_current_sem()).select().first()
	

def valid_class_code(class_code):
	class_code = str(class_code)
	return db(db.courses.code==class_code).count()==1

def current_valid_class_code(class_code):
	class_code = str(class_code)
	course = db(db.courses.code==class_code).select().first()
	if not course:
		return False
	curr_sem = get_current_semester()
	return db(db.registered_courses.course==course.id)(db.registered_courses.semester==curr_sem.id).count()==1
	
def timeHuman(date_time):
	"""
	converts a python datetime object to the 
	format "X days, Y hours ago"
	@param date_time: Python datetime object
	@return:
		fancy datetime:: string
	"""
	if not date_time:
		return ""
	import datetime
	current_datetime = datetime.datetime.now()
	delta = str(current_datetime - date_time)
	if delta.find(',') > 0:
		days, hours = delta.split(',')
		days = int(days.split()[0].strip())
		hours, minutes = hours.split(':')[0:2]
	else:
		hours, minutes = delta.split(':')[0:2]
		days = 0
	days, hours, minutes = int(days), int(hours), int(minutes)
	datelets =[]
	years, months, xdays = None, None, None
	plural = lambda x: 's' if x!=1 else ''
	if days >= 365:
		years = int(days/365)
		datelets.append('%d year%s' % (years, plural(years)))
		days = days%365
	if days >= 30 and days < 365:
		months = int(days/30)
		datelets.append('%d month%s' % (months, plural(months)))        
		days = days%30
	if not years and days > 0 and days < 30:
		xdays =days
		datelets.append('%d day%s' % (xdays, plural(xdays)))        
	if not (months or years) and hours != 0:
		datelets.append('%d hour%s' % (hours, plural(hours)))        
	if not (xdays or months or years):
		datelets.append('%d minute%s' % (minutes, plural(minutes)))        
	return ', '.join(datelets) + ' ago.'
