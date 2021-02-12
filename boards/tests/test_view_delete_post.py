from django.forms import ModelForm

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Post, Topic
from ..views import PostUpdateView


class DeletePostTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        self.post = Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        self.url = reverse('boards:delete_post', kwargs={
            'board_pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })


class LoginRequiredDeletePostTests(DeletePostTestCase):
    def test_redirection(self):
        login_url = reverse('accounts:login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class UnauthorizedDeletePostTests(DeletePostTestCase):
    def setUp(self):
        super().setUp()
        username = 'jane'
        password = '321'
        user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        '''
        A topic should be edited only by the owner.
        Unauthorized users should get a 404 response (Page Not Found)
        '''
        self.assertEquals(self.response.status_code, 404)


class AuthorizedDeletePostTests(DeletePostTestCase):
    def setUp(self):
        super().setUp()
        username = 'john'
        password = '123'
        self.client.login(username=username, password=password)

    def test_status_code(self):
        '''
        A post should be deleted only by the owner.
        after successful deleting, user will be redirected.
        '''
        # Before delete
        self.assertEquals(Post.objects.all().count(), 1)

        # delete
        self.response = self.client.get(self.url)
        self.assertEquals(self.response.status_code, 302)

        #post delete
        self.assertEquals(Post.objects.all().count(), 0)
