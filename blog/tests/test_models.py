from django.test import TestCase
from blog.models import Post

from django.contrib.auth.models import User


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        #Set up non-modified objects used by all test methods
        self.post = Post.objects.create(
            title = 'test post',
            slug = 'test_post',
            body = 'test body',
            author = self.user)

    def test_title_name(self):
        self.assertEquals(f'{self.post.title}','test post')

    def test_post_content(self):
        self.assertEqual(f'{self.post.slug}', 'test_post')
        self.assertEqual(f'{self.post.body}', 'test body')
        self.assertEqual(f'{self.post.author}', 'testuser')
