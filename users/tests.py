from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            "first_name": "Paul",
            "last_name": "Jacob",
            "username": "paultest",
            "email": "paul@jacob.com",
            "password1": "Paul1234",
            "password2": "Paul1234",
        }
        self.path = reverse("users:registration")

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Registration")
        self.assertTemplateUsed(response, "users/registration.html")

    def test_user_registration_post_success(self):
        response = self.client.post(self.path, self.data)
        username = self.data["username"]

        # check creating user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("users:login"))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data["username"])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
