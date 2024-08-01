from django.urls import path

from users.views import ProfileView, LoginUserView, LogoutView, UpdateProfileView, UserCreateViews

app_name = 'user'




urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),

    path('register/', UserCreateViews.as_view(), name='register_page'),
    path('login/', LoginUserView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout'),


    # path('profile/', ProfileView.as_view(), name='profile'),



    path('update/', UpdateProfileView.as_view(), name='update')
]


