from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.

class PrimaryDepartment(models.Model):
	primary_department_id = models.AutoField(primary_key=True)
	department_name = models.CharField(max_length=128)

	def __str__(self):
		return self.department_name

class SecondaryDepartment(models.Model):
	secondary_department_id = models.AutoField(primary_key=True)
	department_name = models.CharField(max_length=128)

	def __str__(self):
		return self.department_name

class ProgrammingLanguage(models.Model):
	programming_language_id = models.AutoField(primary_key=True)
	language_name = models.CharField(max_length=64)

	def __str__(self):
		return self.language_name

class UserInfo(models.Model):
    user = models.ForeignKey(auth_models.User)
    primary_department = models.ForeignKey(PrimaryDepartment, on_delete=models.CASCADE)
    secondary_department = models.ForeignKey(SecondaryDepartment, on_delete=models.CASCADE)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    photo = models.FileField(upload_to="./upload/users/photo") # photo file path
    
    def __str__(self):
        return self.user_id.username
