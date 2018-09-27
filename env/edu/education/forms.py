from django import forms 
 
#creating our forms



from .models import *
class courseform(forms.ModelForm):
    class Meta:
        model= course
        fields= ["department","name","ctype",]

class semesterform(forms.ModelForm):
    class Meta:
        model= semester
        fields= ["semname","coursename","departmentname",]



class materialform(forms.ModelForm):
    class Meta:
        model = material
        fields = ('desc', 'file','department','course','semester', )


class subjectform(forms.ModelForm):
    class Meta:
        model= subject
        fields= ["departmentname","subjectname","coursename","semester",]



class subjectform2(forms.ModelForm):
    class Meta:
        model= subject
        fields= ["departmentname","coursename","semester",]

class feeform(forms.ModelForm):
    class Meta:
        model= fee
        fields= ["student","fee",]


class studform(forms.ModelForm):
    class Meta:
        model= student
        fields= ["username","password",]

class feedbackform(forms.ModelForm):
    class Meta:
        model =feedback
        fields=["feedback"]

class parentform(forms.ModelForm):
    class Meta:
        model= student
        fields= ["parentname","gender","std_name","deptname","coursename","emailid","semester","joindate","admno", "address" ,"contactno", ]


class markform1(forms.ModelForm):
    class Meta:
        model= marks
        fields= ["semester","studentname",]

class markform(forms.ModelForm):
    class Meta:
        model= marks
        fields= ["semester","studentname","coursename","departmentname","examname","avmarks","remarks", ]

class attendanceform(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","semester","studentname","coursename","subjectname1","subjectname2","subjectname3", "subjectname4" ,"subjectname5","Subjectname6","Subjectname7","attsub1","attsub2","attsub3","attsub4","attsub5","attsub6","attsub7"]

class attendanceform2(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","semester","coursename",]


class attendanceform3(forms.ModelForm):
    class Meta:
        model= attendance
        fields= ["department","coursename",]


class departmentform(forms.ModelForm):
    class Meta:
        model= department
        fields= ["departmentname",]


