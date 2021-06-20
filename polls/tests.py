
from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question
from django.urls import reverse


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text = "Past Question", days = -30)
        response = client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        create_question(question_text = "Future Question", days = 30)
        response = client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_past_question(self):
        question = create_question(question_text = "Past question", days = -30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days = 1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_question = Question (pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours = 23, seconds = 59)
        recent_question = Question (pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)
