from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_learn_page_status_code(self):
        response = self.client.get('/learn/')
        self.assertEqual(response.status_code, 200)

    def test_shop_page_status_code(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code,200)
# Create your tests here.
