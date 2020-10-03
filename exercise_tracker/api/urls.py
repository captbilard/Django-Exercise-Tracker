from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import UsersView, ExerciseView

router = SimpleRouter()

router.register('users', UsersView)
router.register('add', ExerciseView)

urlpatterns = [
    path('exercise/', include(router.urls))
]