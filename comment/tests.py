from django.test import TestCase
from .models import ReviewComments

class ReviewCommentsTestCase(TestCase):

    def setUp(self):
        # Create a sample ReviewComments instance for testing
        self.review = ReviewComments(
            ratings=5,
            comments="This is a test comment.",
            equipment_name="Test Equipment",
            Time_stamp="2023-09-12",
            customer="Test Customer"
        )
        self.review.save()

    def test_review_attributes(self):
        # Test the attributes of the ReviewComments model
        self.assertEqual(self.review.ratings, 5)
        self.assertEqual(self.review.comments, "This is a test comment.")
        self.assertEqual(self.review.equipment_name, "Test Equipment")
        self.assertEqual(str(self.review.Time_stamp), "2023-09-12")
        self.assertEqual(self.review.customer, "Test Customer")

    def test_review_str(self):
        # Test the __str__ method of the ReviewComments model
        expected_str = f"Rating: {self.review.ratings}, Equipment: {self.review.equipment_name}"
        self.assertEqual(str(self.review), expected_str)
