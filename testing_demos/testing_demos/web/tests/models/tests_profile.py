from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_demos.web.models import Profile


class ProfileTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Doncho',
        'last_name': 'Minkov',
        'age': 15
    }

    def test_profileCreate_whenFirstNameContainsOnlyLetters_expectSuccess(self):
        profile = Profile(
            **self.VALID_PROFILE_DATA,
        )
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profileCreate_whenFirstNameContainsADigit_expectToFail(self):
        first_name = 'Doncho1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profileCreate_whenFirstNameContainsADollarSign_expectToFail(self):
        first_name = 'Donc$ho'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profileCreate_whenFirstNameContainsASpace_expectToFail(self):
        first_name = 'Don cho'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profileFullName_whenValid_expectCorrectFullName(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        expected_fullname = f'{self.VALID_PROFILE_DATA["first_name"]} {self.VALID_PROFILE_DATA["last_name"]}'
        self.assertEqual(f'{expected_fullname}', profile.full_name)
