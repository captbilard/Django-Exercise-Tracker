import datetime

from django.test import TestCase

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
