from django.test import TestCase
from django.test import Client

class AnimalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_hello(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
    
    def test_goodbye(self):
        response = self.client.get('/goodbye/')
        self.assertEqual(response.status_code, 200)
