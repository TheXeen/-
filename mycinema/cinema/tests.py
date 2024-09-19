from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from cinema.models import Hall


class HallAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'password123'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        self.hall_create_url = reverse('hall_create_api')
        self.valid_data = {
            "name": "Test Hall",
            "size": 100  
        }
        self.invalid_data = {
            "name": "",
            "size": 0  
        }

    def test_create_valid_hall(self):
        response = self.client.post(self.hall_create_url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hall.objects.count(), 1)
        self.assertEqual(Hall.objects.get().name, 'Test Hall')

    def test_create_invalid_hall(self):
        response = self.client.post(self.hall_create_url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

