from django.test import TestCase, Client

class SimpleTests(TestCase):
    def test_blog_page_status_code(self):
        client = Client()
        response = client.get('/blog/')
        self.assertEqual(response.status_code, 200)
