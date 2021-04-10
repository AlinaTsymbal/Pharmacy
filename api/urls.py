from django.urls import path

from api.views import RemediesView

urlpatterns = [
    path('remedies', RemediesView.as_view()),
]
