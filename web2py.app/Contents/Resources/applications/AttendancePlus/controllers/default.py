# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
	"""
	example action using the internationalization operator T and flash
	rendered by views/default/index.html or views/generic.html

	if you need a simple wiki simply replace the two lines below with:
	return auth.wiki()
	"""
	response.flash = T("Hello World")
	return dict(message=T('Welcome to web2py!'))


def user():
	"""
	exposes:
	http://..../[app]/default/user/login
	http://..../[app]/default/user/logout
	http://..../[app]/default/user/register
	http://..../[app]/default/user/profile
	http://..../[app]/default/user/retrieve_password
	http://..../[app]/default/user/change_password
	http://..../[app]/default/user/bulk_register
	use @auth.requires_login()
		@auth.requires_membership('group name')
		@auth.requires_permission('read','table name',record_id)
	to decorate functions that need access control
	also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
	"""
	return dict(form=auth())


@cache.action()
def download(): 
	return response.download(request,db)

@cache.action()
def link(): 
	return response.download(request,db,attachment=False)

def prints():
	return dict(prints=db(db.fingerprints.id>0).select())

def users():
	return dict(users=db(db.users.id>0).select())


def upload_print_json():
	if True or auth.is_logged_in():
		sub_form = FORM(
			INPUT(_name="sub_name", _type="text"),
			INPUT(_name="sub_file", _type="file")
			)
		if sub_form.accepts(request.vars, formname='sub_form') and sub_form.vars.sub_name.strip()!="":
			eno = sub_form.vars.sub_name.upper()
			student = student_by_entryno(eno)
			#open('log.txt','a').write(str(student)+'\n')
			if student!=None:
				sub = db.fingerprints.finger1.store(sub_form.vars.sub_file.file, sub_form.vars.sub_file.filename)
				db(db.fingerprints.user_id==student.id).delete()
				id = db.fingerprints.insert(finger1=sub, user_id=student.id )
				if id>0:
					session.flash = "Fingerprint upload Successful!"
					return dict(success=True, msg=session.flash)
				else:
					session.flash = "Fingerprint upload Failed!"
					return dict(success=False, msg=session.flash)
			else:
				session.flash = "User doesn't exist"
				return dict(success=False, msg=session.flash)
		else:
			session.flash = "Invalid formname or name cannot be empty!"
			return dict(success=False, msg=session.flash)
	else:
		session.flash = "Authentication failed!!"
		return dict(success=False, msg=session.flash)
		

def upload_print():
	if True or auth.is_logged_in():
		sub_form = FORM(
			INPUT(_name="sub_name", _type="text"),
			INPUT(_name="sub_file", _type="file")
			)
		if sub_form.accepts(request.vars, formname='sub_form') and sub_form.vars.sub_name.strip()!="":
			eno = sub_form.vars.sub_name.upper()
			student = student_by_entryno(eno)
			if student!=None:
				sub = db.fingerprints.finger1.store(sub_form.vars.sub_file.file, sub_form.vars.sub_file.filename)
				id = db.fingerprints.insert(finger1=sub, user_id=student.id )
				if id>0:
					session.flash = "Fingerprint upload Successful!"
			else:
				session.flash = "User doesn't exist"
	if request.env.http_referer:
		redirect(request.env.http_referer)
	else:
		redirect('/prints')

def delete_print():
	db(db.fingerprints.finger1==request.args[0]).delete()
	session.flash = "Resource deleted successfully!!"
	if request.env.http_referer:
		redirect(request.env.http_referer)
	else:
		redirect('/')

def attendance():
	if len(request.args)<1:
		raise HTTP(404, "course code not provided")
	class_code = str(request.args[0])
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
	if not request.vars['lecture_time']:
		c_lectures = db(db.lectures.course==registered_course).select()
		lectures = {}
		for lecture in c_lectures:  
			lectures[str(lecture.time_)] = (db(db.attendance.lecture==lecture.id).select(),lecture)
	else:
		c_lectures = db(db.lectures.course==registered_course)(db.lectures.time_==request.vars['lecture_time']).select()
		lectures = {}
		for lecture in c_lectures:  
			lectures[str(lecture.time_)] = (db(db.attendance.lecture==lecture.id).select(),lecture)
	return dict(lectures=lectures, lecture_time=request.vars['lecture_time'],registered_course=registered_course, registered_students = db(db.student_registrations.registered_course==registered_course.id).select())

def call():
	"""
	exposes services. for example:
	http://..../[app]/default/call/jsonrpc
	decorate with @services.jsonrpc the functions to expose
	supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
	"""
	return service()


