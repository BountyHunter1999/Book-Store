from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse,resolve


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

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hello There! I Should Not Be Here')
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

