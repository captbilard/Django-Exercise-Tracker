import datetime

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Users, Exercise


class ModelsTestCase(TestCase):
    def setUp(self):
        Users.objects.create(
            username="Tester"
        )
        Exercise.objects.create(
            date="2020-05-03",
            username=Users.objects.get(username="Tester"),
            description="Bench Press",
            duration=datetime.timedelta(minutes=60)
        )

    def test_user_was_created(self):
        response = Users.objects.get(pk=1)
        self.assertEqual(response.username, "Tester")

    def test_exercise_was_created(self):
        response = Exercise.objects.get(description="Bench Press")
        self.assertEqual(response.username.username, "Tester")
        self.assertEqual(response.date, datetime.date(2020, 5, 3))


class EndpointTestCase(APITestCase):
    def setUp(self):
        url = reverse('users-list')
        self.user = self.client.post(url, data={
            "username":"Tester1"
        })
        self.response = self.client.get('/api/users/1/')

    def test_create_user(self):
        data = {"username": "Tester2"}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Users.objects.get().username, "Tester2")
    
    def test_get_all_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_exercise(self):
        url = reverse('exercise-list')
        data = {
            "description": "Sit ups",
            "duration":"30",
            "username": self.response.data['url']
        }
        response = self.client.post(url, data, format='json')
        #print(self.response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['date'], "2020-10-06")
    
    def test_get_exercise_log_user(self):
        #user_id = self.response.data['id']
        response = self.client.get('/api/exercise/log/1/')
        for item in response:
            print(item)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        