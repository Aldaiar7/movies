from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from movies.users.api.views.user_register import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register')
]



urlpatterns += [
    path('api/', include('config.api_router'))
]