import json
from dataclasses import dataclass
from argparse import ArgumentParser
import unittest

@dataclass
class SupportResource:
    """Dataclass to hold support resource information"""
    name: str
    url: str
    description: str

class MailTuner:
    """Class to provide access to support resources"""
    def __init__(self):
        self.support_resources = [
            SupportResource("FAQs", "https://example.com/faqs", "Frequently Asked Questions"),
            SupportResource("Tutorials", "https://example.com/tutorials", "Step-by-step guides"),
            SupportResource("Contact", "https://example.com/contact", "Get in touch with us")
        ]

    def get_support_resources(self):
        """Return a list of support resources"""
        return self.support_resources

    def get_support_resource(self, name):
        """Return a specific support resource by name"""
        for resource in self.support_resources:
            if resource.name.lower() == name.lower():
                return resource
        return None

def main():
    parser = ArgumentParser(description="Mail Tuner")
    parser.add_argument("--list-resources", action="store_true", help="List all support resources")
    parser.add_argument("--get-resource", type=str, help="Get a specific support resource by name")
    args = parser.parse_args()
    mail_tuner = MailTuner()
    if getattr(args, "list_resources", False):
        resources = mail_tuner.get_support_resources()
        for resource in resources:
            print(f"Name: {resource.name}, URL: {resource.url}, Description: {resource.description}")
    elif getattr(args, "get_resource", None):
        resource = mail_tuner.get_support_resource(args.get_resource)
        if resource:
            print(f"Name: {resource.name}, URL: {resource.url}, Description: {resource.description}")
        else:
            print("Resource not found")

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
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        unittest.main(argv=sys.argv[:1])
    else:
        main()
