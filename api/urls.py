from django.urls import path

from api.views import RemediesView, Categories

urlpatterns = [
    path('categories', Categories.as_view()),
    path('remedies', RemediesView.as_view()),
]
