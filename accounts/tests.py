from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@email.com',
            password='testpass1234',
			#is_staff="True"
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email,'test@email.com')
        self.assertEqual(user.email,'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        # self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='super_test',
            email='super_test@email.com',
            password='super_testpass1234'
        )
        self.assertEqual(admin_user.username, 'super_test')
        self.assertEqual(admin_user.email,'super_test@email.com')
        self.assertEqual(admin_user.email,'super_test@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)