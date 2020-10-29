from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from whatislove import views

urlpatterns = [
    path('films/', views.FilmList.as_view()),
    path('films/<int:pk>/', views.FilmDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

