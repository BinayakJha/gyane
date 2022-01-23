from django.test import TestCase
from http import HTTPStatus
# Create your tests here.
class RobotsTestCase(TestCase):
    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertEqual(response.content, b'User-Agent: *\nDisallow: /cgi-bin/\nSitemap: https://gyane.xyz/sitemap.xml')


