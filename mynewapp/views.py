from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserRegForm,UserLoginForm,UserUpdateForm,PasswordChangeForm,ImageForm,ImageshowForm,AboutForm
from . models import User
from . models import img
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def image(request):
    if request.method =='POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Name']
            price =form.cleaned_data['Price']
            location =form.cleaned_data['Location']
            colour = form.cleaned_data['Colour']
            photo = form.cleaned_data['Photo']
            form.save()

            return redirect("/imageshow")
            return render(request,'image.html',{'form':form})
    else:
        form=ImageForm()
    return render(request,'image.html',{'form':form})

def imageshow(request):
    Img=img.objects.all()
    return render(request,'imageshow.html',{'Img':Img})



    



def user_reg(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Name']
            address = form.cleaned_data['Address']
            photo = form.cleaned_data['Photo']
            gender = form.cleaned_data['Gender']
            maritialstatus = form.cleaned_data['Maritialstatus']
            educationalqualification = form.cleaned_data['Educationalqualification']
            languageknown = form.cleaned_data['Languageknown']
            district = form.cleaned_data['District']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            confirmpassword = form.cleaned_data['Confirmpassword']
            
            ur = User.objects.filter(Email=email)

            # if ur:
            #     msg="User with same email is already exist!"
            #     args={'form':form,'error':msg}
            #     return render(request,'user_reg.html',args)

            if password!=confirmpassword:
                msg="Enter correct password! passwword mismatch"
                args={'form':form,'error':msg}
                return render(request,'user_reg.html',args)

            else:
                res=User(Name=name,Address=address,Gender=gender,Maritialstatus=maritialstatus,Educationalqualification=educationalqualification,Languageknown=languageknown,District=district,Email=email,
                            Password=password,Confirmpassword=confirmpassword,Photo=photo)
                res.save()
                return redirect('/user_reg')
    else:
        form=UserRegForm()
    return render(request,'user_reg.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            try:
                ur = User.objects.get(Email=email, Status=True)

                if not ur:
                    msg="Incorrect Email or password!"
                    args={'form':form,'error':msg}
                    return render(request,'user_login.html',args)

                elif password!=ur.Password:
                    msg="Incorrect Email or Password"
                    args={'form':form,'error':msg}
                    return render(request,'user_login.html',args)

                else:
                    request.session['email'] = email
                    request.session['sid'] = ur.id
                    return redirect('/user_home/%s' % ur.id)
            except:
                msg = "Incorrect Email or password!"
                args = {'form': form,'error': msg}
                return render(request, 'user_login.html',args)
    else:
        form=UserLoginForm()
    return render(request,'user_login.html',{'form':form})
# def edit(request,pk):
#     user=User.objects.get(id=pk)
#     form=UserEditForm(request.POST,instance=user)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request,'/edit.html',{'user':users})
def show(request, id):
    users=User.objects.get(id=id)
    form=UserUpdateForm(request.POST,instance=users)
    if form.is_valid():
        form.save()
        return redirect("/user_home")
    return render(request,'show.html',{'users':users})



def about(request,pk):
    Img=img.objects.get(id=pk)
    return render(request,'about.html',{'Img':Img})

def user_home(request,id):
    if request.session.has_key:
        email = request.session['email']
        uid = request.session['sid']
        user = User.objects.get(id=id)
        ur = User.objects.get(Email=email) 
        return render(request, 'user_home.html', {'ur':ur, 'user':user})


def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/")

def changepassword(request,id):
    uid=request.session['sid']
    user=User.objects.get(id=id)
    if request.method=='POST':
        form=PasswordChangeForm(request.POST)
        if form.is_valid():
            oldpassword = form.cleaned_data['Oldpassword']
            newpassword = form.cleaned_data['Newpassword']
            confirmpassword = form.cleaned_data['Confirmpassword']
            if oldpassword!=user.Password:
                msg="Enter correctpassword"
                return render(request,'changepassword.html',{'form':form,'error':msg,'user':user})
            elif newpassword!=confirmpassword:
                msg="Password does not match"
                return render(request,'changepassword.html',{'form':form,'error':msg,'user':user})
            else:
                user.Password =newpassword
                user.Confirmpassword = confirmpassword
                user.save()
                msg ="Password Change Successfully"
                return redirect('/user_home/%s'%id)
                return render(request,'changepassword.html',{'form':form,'error':msg,'user':user})
    else:
        form=PasswordChangeForm()
        return render(request,'changepassword.html',{'form':form,'user':user})
       


    

    
    

def logout(request):
    # logout(request)
    messages.info(request,'loggedout successfully')
    return redirect('/')



# def View_404(request):
#     Img=img.objects.all()
#     return redirect("/")
    