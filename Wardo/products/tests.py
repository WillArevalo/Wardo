from django.test import TestCase, Client

# Create your tests here.
class HomeTest(TestCase):
	#defino las variables para que sean reutilizables
	def setUp(self):
		self.client = Client()
		self.response = self.client.get("/")

	def test_home(self):
		self.assertTrue(1==1)
		self.assertFalse(1!=1)
		self.assertEquals(1,1)
		self.assertIn(1,[1,2,3])

	def test_render(self):
		self.assertEquals(self.response.status_code, 200)

	def test_context(self):
		self.assertIn('products',self.response.context)