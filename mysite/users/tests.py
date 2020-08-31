from django.test import TestCase
from django.urls import resolve


def setUp(self):
    self.user = User.objects.create_user('john', 'john@doe.com', '1231234', '1학년')
    self.client.login(username='john', password='123')
    self.response = self.client.get(r('/'))

class IndexTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)


#	def test_home_page_returns_correct_html(self):
#        request = HttpRequest()
#        response = home_page(request)
#        html = response.content.decode('utf8')
#        expected_html = render_to_string('index.html')
#        self.assertEqual(html, expected_html)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)

        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>SH_WebBlog</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'index.html')