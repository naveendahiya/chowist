from django.test import TestCase

from places.forms import ReviewForm


class TestReviewForm(TestCase):
    """ReviewForm test suite"""

    def test_form_invalid(self):
        form = ReviewForm()
        self.assertFalse(form.is_valid())

    def test_form_valid(self):
        form_data = {
            "title": "Great restaurant",
            "body": "This restaurant is really good",
            "rating": 5,
        }
        form = ReviewForm(form_data)
        self.assertTrue(form.is_valid())