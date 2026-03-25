from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create(name='Test User', email='test@example.com', team='marvel')
        Team.objects.create(name='marvel', members=['Test User'])
        Activity.objects.create(user='Test User', activity='Running', duration=30)
        Leaderboard.objects.create(team='marvel', points=100)
        Workout.objects.create(name='Test Workout', suggested_for='Test User')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)
