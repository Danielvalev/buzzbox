from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'firstname', 'lastname', 'password')

        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.last_name, 'lastname')

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_restaurant_manager)

        self.assertEqual(str(super_user), 'testuser@super.com')  # Test __str__ method

        # Test Value Error
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', first_name='first_name', last_name='last_name', password='password',
                is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', first_name='first_name', last_name='last_name', password='password',
                is_superuser=True, is_staff=False)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@super.com', 'firstname', 'lastname', 'password')

        self.assertEqual(user.email, 'testuser@super.com')
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.last_name, 'lastname')

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_restaurant_manager)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', first_name='first_name', last_name='last_name', password='password',
                is_superuser=False)
