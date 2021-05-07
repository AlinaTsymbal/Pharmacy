from django.urls import path

from api.views import RemediesView, Categories, RemedySets

urlpatterns = [
    path('categories', Categories.as_view()),
    path('remedies', RemediesView.as_view()),
    path('med-kits', RemedySets.as_view()),
]
