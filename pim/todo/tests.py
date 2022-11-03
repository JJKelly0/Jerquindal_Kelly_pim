from django.test import TestCase
from unittest.mock import patch  # , Mock

from pim.todo.models import Task


class TestSendingEmail(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('models.send_an_email')
    def test_sending_email_on_complete(self, mock_send_email):
        task = Task.objects.create(name="First", notify="foo@bar.com")
        task.Complete = True
        task.save()
        assert mock_send_email.called

    @patch('models.send_an_email')
    def test_not_sending_email_on_complete(self, mock_send_email):
        task = Task.objects.create(name="First", notify="foo@bar.com")
        task.Complete = True
        task.save()
        assert not mock_send_email.called
