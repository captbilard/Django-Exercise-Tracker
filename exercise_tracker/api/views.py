from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Users, Exercise
from .serializers import UserSerializer, ExerciseSerializer


class UsersView(viewsets.ModelViewSet):
    '''Viewset to provide CRUD for users'''
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class ExerciseList(viewsets.ModelViewSet):
    '''Viewset to provide CRUD for Exercise'''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']


class ExerciseOne(View):
    '''View to get the exercise log of one user'''
    def get(self, request, user_id):
        final_result = []
        # Gets the from value of date
        date_from = request.GET.get('from')
        # Gets the to value of date
        date_to = request.GET.get('to')

        user = Users.objects.get(pk=user_id)
        count = user.get_count()
        user_data = {
            "_id": user.id,
            "username": user.username,
            "count": count
        }
        final_result.append(user_data)

        exercise_query = user.entries

        if date_from:
            exercise_query = exercise_query.filter(date__gte=datetime.strptime(date_from, '%Y-%m-%d'))
        else:
            exercise_query = exercise_query.all()

        if date_to:
            exercise_query = exercise_query.filter(date__lte=datetime.strptime(date_to, '%Y-%m-%d'))
        else:
            exercise_query = exercise_query.all()

        # Get limit
        limit = int(request.GET.get('limit') or 5)
        # Get offset, "https://docs.djangoproject.com/en/3.1/topics/db/queries/#limiting-querysets" read link for more
        offset = int(request.GET.get('offset') or 0)
        # Returns the result based on limit and offset
        exercise_query = exercise_query[offset:limit+offset]

        log = []
        for item in exercise_query.all():
            log.append({
                "description": item.description,
                "duration": item.duration,
                "date": item.date
            })
        final_result.append(log)
        # return Response(final_result, status=status.HTTP_200_OK)
        return JsonResponse({"result": final_result}, status=200)
