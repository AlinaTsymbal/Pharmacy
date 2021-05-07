from django.urls import path

from api.views import RemediesView, Categories, RemedySets, MedKits

urlpatterns = [
    path('categories', Categories.as_view()),
    path('remedies', RemediesView.as_view()),
    path('remedy-sets', RemedySets.as_view()),
    path('med-kits', MedKits.as_view()),
]
