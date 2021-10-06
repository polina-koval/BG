from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class SignUpPageTests(TestCase):

    def setUp(self) -> None:
        self.username = 'testuser'
        self.first_name = 'Test'
        self.last_name = 'User'
        self.email = 'testuser@email.com'
        self.password = 'testpass123'

    def test_signup_page_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/signup.html')

    def test_signup_form(self):
        response = self.client.post('/accounts/signup/', data={
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)


class TestStr(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user",
                                             email="user1@test.com", is_staff=True)
        self.user.set_password("password1")
        self.user.save()

    def test_str_is_equal_to_username(self):
        self.client.force_authenticate(self.user)
        test_user = User.objects.get(username='test_user')
        print(str(test_user))
        assert str(test_user) == test_user.username
