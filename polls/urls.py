from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'answers', views.AnswersViewSet)
router.register(r'choices', views.ChoicesViewSet)
router.register(r'questions', views.QuestionsViewSet)
router.register(r'persons', views.PersonsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]