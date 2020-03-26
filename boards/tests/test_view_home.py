from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..views import BoardListView
from ..models import Board, Topic, Post
from ..forms import NewTopicForm


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('boards:boards_home')
        self.response = self.client.get(url)


    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve("/boards/")
        self.assertEquals(view.func.view_class, BoardListView)


    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'board_pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
