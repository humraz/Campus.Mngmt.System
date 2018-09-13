# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class course(models.Model):
	cid=models.AutoField(primary_key=True)
	department=models.CharField(max_length=30)
	name=models.CharField(max_length=30)
	ctype=models.CharField(max_length=30,default="type1")
	


class semester(models.Model):
	semname=models.CharField(max_length=30)
	coursename=models.CharField(max_length=30)
	departmentname=models.CharField(max_length=30)
	
class feedback(models.Model):
	
	feedback=models.CharField(max_length=30)
	date=models.DateField(default=datetime.date.today)





class subject(models.Model):
	departmentname=models.CharField(max_length=30)
	subjectname=models.CharField(max_length=30)
	coursename=models.CharField(max_length=30)
	semester=models.CharField(max_length=30)
	
class student(models.Model):
	parentname=models.CharField(max_length=30)
	gender=models.CharField(max_length=30)
	std_name=models.CharField(max_length=30)
	deptname=models.CharField(max_length=30)
	semester=models.CharField(max_length=30)
	joindate=models.CharField(max_length=30)
	admno=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	contactno=models.CharField(max_length=30)
	emailid=models.CharField(max_length=30)
	coursename=models.CharField(max_length=30,default="")
	username=models.CharField(max_length=30,default="user")
	password=models.CharField(max_length=30,default="pass")

class marks(models.Model):
	departmentname=models.CharField(max_length=30)
	coursename=models.CharField(max_length=30)
	semester=models.CharField(max_length=30)
	studentname=models.CharField(max_length=30)
	examname=models.CharField(max_length=30,default="NA")
	avmarks=models.CharField(max_length=30,default="NA")
	remarks=models.CharField(max_length=30,default="NA")

class attendance(models.Model):
	department=models.CharField(max_length=30)
	semester=models.CharField(max_length=30)
	studentname=models.CharField(max_length=30)
	status=models.CharField(max_length=30,default="")
	coursename=models.CharField(max_length=30)
	subjectname1=models.CharField(max_length=30,blank=True)
	subjectname2=models.CharField(max_length=30,blank=True)
	subjectname3=models.CharField(max_length=30,blank=True)
	subjectname4=models.CharField(max_length=30,blank=True)
	subjectname5=models.CharField(max_length=30,blank=True)
	Subjectname6=models.CharField(max_length=30,blank=True)
	Subjectname7=models.CharField(max_length=30,blank=True)
	attsub1=models.CharField(max_length=30,blank=True)
	attsub2=models.CharField(max_length=30,blank=True)
	attsub3=models.CharField(max_length=30,blank=True)
	attsub4=models.CharField(max_length=30,blank=True)
	attsub5=models.CharField(max_length=30,blank=True)
	attsub6=models.CharField(max_length=30,blank=True)
	attsub7=models.CharField(max_length=30,blank=True)
	avattendance=models.IntegerField(default=0)

class department(models.Model):
	departmentname=models.CharField(max_length=30)
	
