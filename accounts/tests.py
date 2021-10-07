from django.contrib.auth.models import User
from django.test import TestCase


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
        self.user = User.objects.create_user(
            username="test_user", email="user1@test.com"
        )
        self.user.set_password("password1")
        self.user.save()
        self.client.login(username="test_user", password="password1")

    def test_str_is_equal_to_username(self):
        test_user = User.objects.get(username='test_user')
        print(str(test_user))
        assert str(test_user) == test_user.username
