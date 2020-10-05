from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import UsersView, ExerciseList, ExerciseOne

router = SimpleRouter()

router.register('users', UsersView, )
router.register('exercise', ExerciseList)


urlpatterns = [
    path('', include(router.urls)),
    path('exercise/log/<int:user_id>/', ExerciseOne.as_view())
]