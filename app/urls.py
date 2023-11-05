
from django.urls import path, include
from .views import CarList, CreateCars

urlpatterns = [
    path('', CarList.as_view(), name='cars'),
    path('add-cars/', CreateCars.as_view(), name='add-cars'),
    path('captcha/', include('captcha.urls'))
]
