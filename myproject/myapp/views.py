from django.shortcuts import render
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