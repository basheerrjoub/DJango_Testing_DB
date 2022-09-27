from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is the testing Text.")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is the testing Text.")

    def test_respond_url_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Blog Posts")
