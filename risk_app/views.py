from django.shortcuts import render
from django.http import HttpResponse
from risk_app.models import Riskfactorsprofile
from plotly.offline import plot
import plotly.graph_objects as go

def index(request):
    # 뷰 로직
    return render(request, 'risk_app/index.html')

def your_view(request):
    # 각 컬럼별 고유한 값들을 조회
    facility_large_values = Riskfactorsprofile.objects.values_list('Facility_classification_large', flat=True).distinct()
    facility_medium_values = Riskfactorsprofile.objects.values_list('Facility_classification_medium', flat=True).distinct()
    facility_small_values = Riskfactorsprofile.objects.values_list('Facility_classification_small', flat=True).distinct()
    
    context = {
        'facility_large_values': facility_large_values,
        'facility_medium_values': facility_medium_values,
        'facility_small_values': facility_small_values,
    }
    return render(request, 'risk_app/index.html', context)

def my_view(request):
    return render(request, 'risk_app/index.html')


# Create your views here.

