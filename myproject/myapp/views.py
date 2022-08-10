from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Alvin'
    # feature1.details = 'Hi my name is Alvin'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Carol'
    # feature2.details = 'Hi my name is Carol'
    
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Jack'
    # feature3.details = 'Hi my name is Jack'
    
    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Melvin'
    # feature4.details = 'Hi my name is Melvin'

    # features = [feature1, feature2, feature3, feature4]

    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not Match')
            return redirect('register')
    else:
        return render(request, 'register.html')