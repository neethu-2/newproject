from django import forms
from .models import User
from. models import img
gender = (
	('Male', 'Male'),
	('Female','Female'),
	('Transgender','Transgender')
	)
maritialstatus = (
	('Married', 'Married'),
	('Unmarried','Unmarried')
	)
edu= [
    ('Sslc', 'Sslc'),('Plus2', 'Plus2'),('Degree', 'Degree'),('Pg', 'Pg'),('Others', 'Others')
    ]
# district = (
#     ('kasaragod','Kasaragod'),
#     ('kannur','Kannur'),
#     ('kozhikkode','Kozhikkode'),
#     ('vayanad','Vayanad'),
#     ('malappuram','Malappuram'),
#     ('thrissure','Thrissure'),
#     ('idukki','Idukki'),
#     ('palakkad','Palakkad'),
#     ('ernakulam','Ernakulam'),
#     ('alappuzha','Alappuzha'),
#     ('pathanamthitta','Pathanamthitta'),
#     ('kottayam','Kottayam'),
#     ('kollam','Kollam'),
#     ('thiruvananthapuram','Thiruvananthapuram'),
#     )


class UserRegForm(forms.ModelForm):

    Password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=gender))
    Educationalqualification=forms.MultipleChoiceField(choices=edu,widget=forms.CheckboxSelectMultiple(attrs={'class':'qual'}))
    Maritialstatus=forms.CharField(label='Maritialstatus',widget=forms.RadioSelect(choices=maritialstatus))
    # District=forms.CharField(label='District',widget=forms.RadioSelect(choices=district))
    class Meta():
        model = User
        fields = ('Name','Address','Gender','Maritialstatus','Educationalqualification','Languageknown','District','Email','Password','Confirmpassword','Photo')

class UserLoginForm(forms.ModelForm):
    Password= forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('Email', 'Password')
class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('Name','Address','Gender','Maritialstatus','Educationalqualification','Languageknown','District','Email','Photo')


class PasswordChangeForm(forms.ModelForm):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)
    Newpassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)

    class Meta():
        model = User
        fields = ('Oldpassword','Newpassword','Confirmpassword')




class ImageForm(forms.ModelForm):

    class Meta():
        model= img
        fields=('Name','Price','Location','Colour','Photo')

class ImageshowForm(forms.ModelForm):
    class Meta():
        model=img
        fields=('Photo',)

class AboutForm(forms.ModelForm):
    class Meta():
        model=img 
        fields=('Name','Price','Location','Colour','Photo')      
 
         