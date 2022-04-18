from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from testing_demos.web.models import Profile
from testing_demos.web.views import ProfilesListView

UserModel = get_user_model()


class ProfilesListViewTests(TestCase):
    def test_get_expectCorrectTemplate(self):
        response = self.client.get(reverse('list profiles'))

        self.assertTemplateUsed(response, 'profile/list.html')

    def test_get_whenTwoProfiles_expectContextToContainTwoProfiles(self):
        # Arrange
        profiles_to_create = (
            Profile(first_name='Doncho', last_name='Minkov', age=15),
            Profile(first_name='Minko', last_name='Donchev', age=17),
        )

        Profile.objects.bulk_create(profiles_to_create)

        # Act
        response = self.client.get(reverse_lazy('list profiles'))

        # Assert
        profiles = response.context['object_list']
        self.assertEqual(len(profiles), 2)

    def test_get_whenNotLoggedInUser_expectContextUserToBeNoUser(self):
        response = self.client.get(reverse('list profiles'))
        self.assertEqual(
            ProfilesListView.no_logged_in_user_value,
            response.context[ProfilesListView.context_user_key],
        )

    def test_get_whenLoggedInUser_expectContextToBeUsername(self):
        user_data = {
            'username': 'aenlo',
            'password': 'asdqwe123',
        }

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('list profiles'))

        self.assertEqual(
            user_data['username'],
            response.context[ProfilesListView.context_user_key],
        )
