from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Check home page for a response of 200 and html/text content
    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check tools page for a response of 200 and html/text content
    def test_tools_page(self):
        tester = app.test_client(self)
        response = tester.get('/tools', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check recipe search for a response of 200 and html/text content
    def test_search_results(self):
        tester = app.test_client(self)
        response = tester.post('/recipes/search',
                               data=dict(search="chocolate"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check create account page for a response of 200 and html/text content
    def test_create_account_page(self):
        tester = app.test_client(self)
        response = tester.get('/user/create_account', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check login page for a response of 200 and html/text content
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/user/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check create recipe page for a response of 200 and html/text content
    def test_create_recipe_page(self):
        with app.test_client(self) as tester:
            with tester.session_transaction() as sess:
                sess['username'] = 'davesmith23'
        response = tester.get('/recipes/create_recipe',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check category search for a response of 200 and html/text content
    def test_category_search_results(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/search/<category>',
                              data=dict(category="breakfast"),
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check user recipe search for a response of 200 and html/text content
    def test_owner_recipe_search_results(self):
        with app.test_client(self) as tester:
            with tester.session_transaction() as sess:
                sess['username'] = 'davesmith23'
        response = tester.get('/recipes/search/user/<owner>',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check user removed recipes for a response of 200 and html/text content
    def test_owner_removed_recipes_results(self):
        with app.test_client(self) as tester:
            with tester.session_transaction() as sess:
                sess['username'] = 'davesmith23'
        response = tester.get('/recipes/search/user/<owner>/removed',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check view recipe page for a response of 200 and html/text content
    def test_view_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/view_recipe/5f42c1461faca2fa26e596d9',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')

    # Check edit recipe page for a response of 200 and html/text content
    def test_edit_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/edit_recipe/5f42c1461faca2fa26e596d9',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type, 'html/text')


if __name__ == '__main__':
    unittest.main()
