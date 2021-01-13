from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Lecture, Instructors

# Create your views here.


def index(request):
    if 'userid' in request.session:
        print('inside if')
        userid = request.session['userid']
        lecture = Lecture.objects.filter(instructor_id=userid)
        return render(request, 'lecture.html', {'lect_list': lecture, 'user': request.session['username']})
    else:
        print('inside else')
        return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def handleLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        try:
            user = Instructors.objects.get(email=email, password=password)
        except Instructors.DoesNotExist:
            user = None
        # print(user)

        # If password is right the 'user' would be not None.
        if user is not None:
            request.session['userid'] = user.id
            request.session['username'] = user.name
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')
    else:
        return HttpResponse("404 - Not Found")


def logout(request):
    del request.session['userid']
    del request.session['username']
    return redirect('/login')


# def lecture1(request):
#     lect_list = Lecture.objects.all()
#     context = {'lect': lect_list}
#     return render(request, 'lecture.html', context)


