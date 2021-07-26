from pages.views import HomePageView
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve

# Create your tests here.
class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "Yo, duh!!")
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view.__name__
        )