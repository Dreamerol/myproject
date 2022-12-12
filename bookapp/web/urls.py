from django.urls import path, include

from bookapp.web.views import home, add_page, edit_page, delete_page, profile, create_profile, edit_profile, \
    delete_profile, page_details

urlpatterns = (

    path('', home, name='home'),
    path('add/', add_page, name='add page'),
    path('edit/<int:pk>', edit_page, name='edit page'),
    path('details/<int:pk>', page_details, name='page details'),
    path('delete/<int:pk>', delete_page, name='delete page'),

    path('profile/', include([
        path('', profile, name='profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)