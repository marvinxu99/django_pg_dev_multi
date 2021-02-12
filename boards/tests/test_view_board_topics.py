from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..views import TopicListView
from ..models import Board, Topic, Post
from ..forms import NewTopicForm


class BoardTopicsTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        #self.url = reverse('boards:reply_topic', kwargs={'board_pk': self.board.pk, 'topic_pk': self.topic.pk})



    def test_board_topics_view_success_status_code(self):
        url = reverse('boards:board_topics', kwargs={ 'board_pk': 1 })
        print("URL=" + str(url))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('boards:board_topics', kwargs={ 'board_pk': 99 })
        print("URL=" + str(url))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    # def test_board_topics_view_contains_link_back_to_homepage(self):
    #     board_topics_url = reverse('boards:board_topics', kwargs={'board_pk': 1})
    #     response = self.client.get(board_topics_url)
    #     homepage_url = reverse('boards:boards_home')
    #     print('href=' + 'href="{0}"'.format(homepage_url))
    #     print(str(response))
    #     self.assertContains(response, 'href="{0}"'.format(homepage_url))
