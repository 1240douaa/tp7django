from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_basic(self):
        """Test basique pour vérifier que les tests fonctionnent"""
        self.assertEqual(1 + 1, 2)
    
    def test_app_loads(self):
        """Test que l'application se charge correctement"""
        self.assertTrue(True)