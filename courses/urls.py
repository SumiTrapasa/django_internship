from django.urls import path
from .views import (
    # my_fbv,
    CourseListView,
    CourseView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDleteView
)

app_name = 'courses'
urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    # path('', MyListView.as_view(), name='courses-list'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', CourseView.as_view(tepmlates='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDleteView.as_view(), name='course-delete'),
    
]