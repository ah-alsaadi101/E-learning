from rest_framework import status
from rest_framework.test import APITestCase


class AccountsAPITests(APITestCase):
    def test_api_root_and_health_are_available(self):
        api_response = self.client.get('/api/')
        self.assertEqual(api_response.status_code, status.HTTP_200_OK)
        self.assertIn('accounts', api_response.data)
        self.assertIn('auth_examples', api_response.data)

        health_response = self.client.get('/api/health/')
        self.assertEqual(health_response.status_code, status.HTTP_200_OK)
        self.assertEqual(health_response.data['status'], 'ok')

    def test_register_login_and_profile_flow(self):
        register_response = self.client.post(
            '/api/accounts/users/register/',
            {
                'username': 'api_student',
                'email': 'student@example.com',
                'password': 'StrongPass123!',
                'role': 'student',
            },
            format='json',
        )
        self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', register_response.data)

        login_response = self.client.post(
            '/api/accounts/users/login/',
            {
                'username': 'api_student',
                'password': 'StrongPass123!',
            },
            format='json',
        )
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        token = login_response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        profile_response = self.client.get('/api/accounts/users/profile/')
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)
        self.assertEqual(profile_response.data['username'], 'api_student')
