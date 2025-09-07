from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AuthTestCase(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_login_view(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(reverse('account_login'), {
            'login': 'testuser',
            'password': 'testpassword'
        })
        self.assertRedirects(response, '/dashboard/')

    def test_signup(self):
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'a.very.complex.password123',
            'password2': 'a.very.complex.password123',
            'bio': 'This is a test bio.',
            'location': 'Test Location',
            'birth_date': '2000-01-01'
        })
        self.assertRedirects(response, '/dashboard/')
        self.assertTrue(self.User.objects.filter(username='newuser').exists())
