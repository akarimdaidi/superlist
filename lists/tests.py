from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class ListsTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_corret_html(self):
		request = HttpRequest()
		response = home_page(request)

		expect_html = render_to_string('home.html')

		self.assertEqual(response.content.decode(), expect_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		item_value = 'A new list item'
		request.POST['item_text'] = item_value

		response = home_page(request)

		self.assertIn(item_value, response.content.decode())

		expect_html = render_to_string(
			'home.html',
			{'new_item_text': item_value}
		)

		self.assertEqual(response.content.decode(), expect_html)
