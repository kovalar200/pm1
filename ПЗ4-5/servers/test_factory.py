from django.test import SimpleTestCase
from .models import QueryTypeFactory, SlowQuery, NoIndexQuery, InjectionQuery


class FactoryTest(SimpleTestCase):
    def test_create_slow(self):
        obj = QueryTypeFactory.create("slow", "SELECT 1", 3.0)
        self.assertIsInstance(obj, SlowQuery)
        self.assertIn("SLOW", obj.get_info())

    def test_create_noindex(self):
        obj = QueryTypeFactory.create("noindex", "SELECT 2")
        self.assertIsInstance(obj, NoIndexQuery)

    def test_create_injection(self):
        obj = QueryTypeFactory.create("injection", "1 OR 1=1")
        self.assertIsInstance(obj, InjectionQuery)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            QueryTypeFactory.create("unknown", "SELECT 3")