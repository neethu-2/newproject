from django.db import models
# from django.core.validators import RegexValidator




gender = (
	('male', 'Male'),
	('female','Female'),
	('transgender','Transgender')
	)
maritialstatus = (
	('married', 'Married'),
	('unmarried','Unmarried')
	)
edu = (
	('sslc','Sslc'),
	('plus2','Plus2'),
	('degree','Degree'),
	('pg','Pg'),
	('others','Others'),
	)
	
languageknown = (
	('malayalam', 'Malayalam'),
	('english', 'English'),
	('hindi', 'Hindi')
	)

district = (
    ('kasaragod','Kasaragod'),
    ('kannur','Kannur'),
    ('kozhikkode','Kozhikkode'),
    ('vayanad','Vayanad'),
    ('malappuram','Malappuram'),
    ('thrissure','Thrissure'),
    ('idukki','Idukki'),
    ('palakkad','Palakkad'),
    ('ernakulam','Ernakulam'),
    ('alappuzha','Alappuzha'),
    ('pathanamthitta','Pathanamthitta'),
    ('kottayam','Kottayam'),
    ('kollam','Kollam'),
    ('thiruvananthapuram','Thiruvananthapuram'),
    )	


	
	

	
class User(models.Model):
	Name = models.CharField(max_length=100)
	Address = models.CharField(max_length=100)
	Gender = models.CharField(max_length=100,default='')
	Email = models.EmailField(unique=True)
	Maritialstatus = models.CharField(max_length=100,default='')
	Educationalqualification = models.CharField(max_length=100,default='')
	Languageknown = models.CharField(max_length=100,choices=languageknown)
	District = models.CharField(max_length=100,choices=district)
	Password = models.CharField(max_length=8)
	Confirmpassword = models.CharField(max_length=8)
	Photo = models.ImageField(upload_to='media/')
	Status = models.BooleanField(default=False)
	def __str__(self):
		return self.Name


class img(models.Model):
	Name = models.CharField(max_length=100)
	Price = models.CharField(max_length=100)
	Location = models.CharField(max_length=100)
	Colour = models.CharField(max_length=100)
	Photo = models.ImageField(upload_to='media/')

	def __str__(self):
		return self.Name



