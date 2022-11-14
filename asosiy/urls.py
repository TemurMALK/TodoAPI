from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from todo.views import *

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('planlar/', PlanlarAPIView.as_view()),
    # path('get_token/', TokenObtainPairView.as_view()),
    # path('token_yangila/', TokenRefreshView.as_view()),
    path('plan/<int:pk>/', PlanAPIView.as_view()),
    path('get_token/', obtain_auth_token, name='api_token_auth'),
    # path('get_token/', obtain_auth_token,),

]
