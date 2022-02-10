from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Department(models.Model):
    department_name = models.CharField(max_length=120, null=True)
    hod = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.department_name




#  student registration university table
class StudentRegistrationUni(models.Model):
    ACD_STATUS = (
        ('','Select Status'),
        ('running','Running '),
        ('discontinue','Discontinue'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=120, null=True, unique=True)
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.BigIntegerField(null=True,blank=True)
    fathername = models.CharField(max_length=120, blank=True, null=True)
    mothername = models.CharField(max_length=120, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    adminsion_year = models.CharField(max_length=50, null=True,blank=True)
    address = models.TextField(max_length=120, null=True,blank=True)
    academic_status = models.CharField(max_length=120, null=True, choices=ACD_STATUS,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,blank=True)
    religion = models.CharField(max_length=120, null=True,blank=True)
    nationality = models.CharField(max_length=120, null=True,blank=True)

    def __str__(self):
        return self.student_id
    class Meta:
        verbose_name = 'Student Registration (University)'
        verbose_name_plural = 'Student Registration (University)'


#  student registration collage table
class StudentRegistrationCollage(models.Model):
    ACD_STATUS = (
        ('','Select Status'),
        ('running','Running '),
        ('discontinue','Discontinue'),
    )

    GROUPS = (
        ('', 'Select Group'),
        ('science', 'Science'),
        ('commerce', 'Business Studies / Commerce'),
        ('arts', 'Humanities / Arts'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=120, null=True, unique=True)
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.BigIntegerField(null=True)
    fathername = models.CharField(max_length=120, blank=True, null=True)
    mothername = models.CharField(max_length=120, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    adminsion_year = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=120, null=True)
    academic_status = models.CharField(max_length=120, null=True, choices=ACD_STATUS)
    group = models.CharField(max_length=120, null=True, choices=GROUPS)
    religion = models.CharField(max_length=120, null=True)
    nationality = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.student_id
    class Meta:
        verbose_name = 'Student Registration (HSC)'
        verbose_name_plural = 'Student Registration (HSC)'

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    course_name = models.CharField(max_length=120, null=True)
    course_code = models.CharField(max_length=120, null=True)
    course_credit = models.FloatField(null=True)
    def __str__(self):
        return f'{self.course_code} {self.course_name} - {self.department.department_name}'

class Enroll(models.Model):
    student = models.ForeignKey(StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    enroll_year = models.IntegerField(blank=True, null=True)
    enroll_semester = models.IntegerField(blank=True, null=True)


class Result(models.Model):
    student = models.ForeignKey(StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    grade_point = models.FloatField(null=True)
    grade_letter = models.CharField(max_length=5, null=True)


class Financial(models.Model):
    student = models.ForeignKey(StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    payment_date = models.DateField(null=True,default=now)
    payment_amount = models.FloatField(null=True,default=0.0)
    money_receipt_no = models.CharField(max_length=120, null=True)
    def __str__(self):
        return f'Payment of #{self.student.student_id} - {self.year}year {self.semester}semester'

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    post_title = models.CharField(null = True, max_length= 150)
    post_content = models.TextField(null=True, max_length=500)
    file = models.FileField(upload_to="notice_file/",blank=True,null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Post: {self.post_title}"






