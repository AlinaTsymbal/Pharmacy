from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import RemediesView, Categories, RemedySets, MedKits, RemedyDetails, BasketView

urlpatterns = [
    path('categories', Categories.as_view()),
    path('remedies', RemediesView.as_view()),
    path('remedy-sets', RemedySets.as_view()),
    path('med-kits', MedKits.as_view()),
    path('remedy/<int:remedy_id>', RemedyDetails.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('check-login', TokenVerifyView.as_view()),
    path('basket', BasketView.as_view()),
]
