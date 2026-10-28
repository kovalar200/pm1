from django.test import SimpleTestCase
from .singleton import SuspiciousQueryLogger


class SingletonTest(SimpleTestCase):
    def test_single_instance(self):
        logger1 = SuspiciousQueryLogger()
        logger2 = SuspiciousQueryLogger()
        self.assertIs(logger1, logger2)
        self.assertEqual(id(logger1), id(logger2))

    def test_shared_state(self):
        logger1 = SuspiciousQueryLogger()
        logger2 = SuspiciousQueryLogger()
        logger1.clear()
        logger1.log("slow", "SELECT 1")
        self.assertEqual(len(logger2.get_all_logs()), 1)