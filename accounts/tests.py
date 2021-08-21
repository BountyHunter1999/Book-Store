from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse,resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


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
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hello There! I Should Not Be Here')
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')


    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )

