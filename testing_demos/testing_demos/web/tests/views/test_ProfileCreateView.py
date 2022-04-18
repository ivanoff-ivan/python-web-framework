from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile


class ProfileCreateViewTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Doncho',
        'last_name': 'Minkov',
        'age': 14,
    }

    def test_createProfile_whenAllValid_expectToCreate(self):
        self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['age'], profile.age)

    def test_createProfile_whenAllValid_expectToRedirectToDetails(self):
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.first()

        expected_url = reverse('details profile', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)

