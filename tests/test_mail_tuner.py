import unittest
from src.mail_tuner import MailTuner, SupportResource

class TestMailTuner(unittest.TestCase):
    def test_get_support_resources(self):
        mail_tuner = MailTuner()
        resources = mail_tuner.get_support_resources()
        self.assertEqual(len(resources), 3)

    def test_get_support_resource(self):
        mail_tuner = MailTuner()
        resource = mail_tuner.get_support_resource("FAQs")
        self.assertIsNotNone(resource)
        self.assertEqual(resource.name, "FAQs")

    def test_get_support_resource_not_found(self):
        mail_tuner = MailTuner()
        resource = mail_tuner.get_support_resource("Unknown")
        self.assertIsNone(resource)

if __name__ == "__main__":
    unittest.main()
