# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

@csrf_protect	
def addattendance(request):
	
	d= department.objects.all()
	c= course.objects.all()
	
	f= attendanceform(request.POST or None)
	if f.is_valid():
		
		dep=request.session.get('dep')
		coursee=f.cleaned_data['coursename']
		semester=f.cleaned_data['semester']
		
		
		subsss=subject.objects.all().filter(departmentname=dep, coursename=coursee)
		studname= f.cleaned_data['studentname']
		print studname
		if attendance.objects.all().filter(studentname=studname):
			atsub1=f.cleaned_data['attsub1']
			atsub2=f.cleaned_data['attsub2']
			atsub3=f.cleaned_data['attsub3']
			atsub4=f.cleaned_data['attsub4']
			atsub5=f.cleaned_data['attsub5']
			atsub6=f.cleaned_data['attsub6']
			atsub7=f.cleaned_data['attsub7']
			s=attendance.objects.all().filter(studentname=studname).update(attsub1=atsub1,attsub2=atsub2,attsub3=atsub3,attsub4=atsub4,attsub5=atsub5,attsub6=atsub6,attsub7=atsub7,)
			att=attendance.objects.all().filter(department=dep, coursename=coursee)
		    	return render(request,'addattendance2.html',{'dep':dep,'course':coursee,'semester':semester, 's':subsss, 'att':att})
			
		f.save()
		print dep,coursee
		att=attendance.objects.all().filter(department=dep, coursename=coursee)
		return render(request,'addattendance2.html',{'dep':dep,'course':coursee,'semester':semester, 's':subsss, 'att':att})
	forms= attendanceform2(request.POST or None)
	if forms.is_valid():
		
		request.session['dep']=forms.cleaned_data['department']
		request.session['coursee']=forms.cleaned_data['coursename']
		request.session['semester']=forms.cleaned_data['semester']
		dep=forms.cleaned_data['department']
		coursee=forms.cleaned_data['coursename']
		semester=forms.cleaned_data['semester']
		subs=subject.objects.all().filter(departmentname=dep, coursename=coursee)
		att=attendance.objects.all().filter(department=dep, coursename=coursee)
		print dep,coursee

		return render(request,'addattendance2.html',{'dep':dep,'course':coursee,'semester':semester, 's':subs,'att':att})
		
		
	return render(request,'addattendance.html',{'d':d,'c':c})

def addcourse(request):
	d= department.objects.all()
	
	forms= courseform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addcourse.html',{'d':d})
def addsemester(request):
	forms= semesterform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addsemester.html')
def addsubject(request):
	d= department.objects.all()
	c= course.objects.all()
	forms= subjectform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addsubject.html',{'c':c,'d':d})

def addparent(request):
	forms= parentfrom(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addparent.html')


def addmarks(request):
	forms= marksform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addmarks.html')

def adddepartment(request):
	forms= departmentform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'adddepartment.html')


def logindex(request):
	
	return render(request,'logindex.html')
def front(request):
	
	return render(request,'frontindex.html')
def login(request):
	forms= studform(request.POST or None)
	if forms.is_valid():
		s=forms.cleaned_data['username']
		pas=forms.cleaned_data['password']
		if s=="admin" and pas=="admin":
			return render(request,'index.html')

		if student.objects.all().filter(std_name=s,password=pas):
			print "ok"
		else:
			return render(request,'loginpagefront.html',{'d':"ww"})
	return render(request,'loginpagefront.html',{'d':""})

	
def afterlogin(request):
	forms= studform(request.POST or None)
	if forms.is_valid():
		s=forms.cleaned_data['username']
		print s
	return render(request,'frontindex.html')


def addpp(request):
	d=department.objects.all()
	c=course.objects.all()
	forms= parentform(request.POST or None)
	if forms.is_valid():
		forms.save()
	return render(request,'addparent.html',{'d':d, 'c':c})



def markss(request):
	f= markform(request.POST or None)
	if f.is_valid():
		sname=f.cleaned_data['studentname']
		exname=f.cleaned_data['examname']
		mark=f.cleaned_data['avmarks']
		rem=f.cleaned_data['remarks']
		r=f.cleaned_data['examname']
		request.session['exam']=r
		if marks.objects.all().filter(studentname=sname):
			marks.objects.all().filter(studentname=sname).update(examname=exname,avmarks=mark,remarks=rem)
		else:
			f.save()
		return render(request,'addmarks.html')

	forms= markform1(request.POST or None)
	if forms.is_valid():
		sname=forms.cleaned_data['studentname']
		sem=forms.cleaned_data['semester']
		
		s=student.objects.all().filter(admno=sname)
		e=request.session.get("exam","")
		if student.objects.all().filter(admno=sname):
			return render(request,'addmarks2.html',{'see':s,'e':e})
		else:
			return render(request,'addmarks.html',{'f':"no"})

	return render(request,'addmarks.html',{'f':""})



def viewdeps(request):

	d=department.objects.all()
	c=course.objects.all()
	s=subject.objects.all()
	sems=semester.objects.all()

	forms= attendanceform3(request.POST or None)

	if forms.is_valid():
		dep=forms.cleaned_data['department']
		coursee=forms.cleaned_data['coursename']
		
		s1=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester="S1")
		s2=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S2')
		s3=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S3')
		s4=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S4')
		s5=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S5')
		s6=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S6')
		s7=subject.objects.all().filter(departmentname=dep,coursename=coursee,semester='S7')
		print s1
		return render(request,'viewdepartments.html',{'d':dep,'c':coursee,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7})


	return render(request,'addattendance3.html',{'d':d,'c':c})


