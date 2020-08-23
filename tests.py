from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Check for a response of 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_tools(self):
        tester = app.test_client(self)
        response = tester.get('/tools', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_search(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/search', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_create_account(self):
        tester = app.test_client(self)
        response = tester.get('/user/create_account', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/user/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_create_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/create_recipe',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_category_search(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/search/dessert',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_owner_recipe_search(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/search/user/davesmith123',
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_owner_removed_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/search/user/<owner>/removed',
                              data=(),
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_view_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/view_recipe/<recipe_id>',
                              data=(),
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for a response of 200
    def test_edit_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipes/edit_recipe/<recipe_id>',
                              data=(),
                              content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check if content is html/text in 'home_page' route
    def test_index_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes')
        self.assertTrue(response.content_type, 'html/text')

    # Check if correct content is displyed in 'home_page' route
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes')
        self.assertTrue(b'Check out our latest recipes' in response.data)

    # Check for a response of 200 in 'home_page' route
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes')
        self.assertTrue(b'Check out our latest recipes' in response.data)


if __name__ == '__main__':
    unittest.main()
