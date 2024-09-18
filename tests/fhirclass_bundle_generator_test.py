import unittest
from models.bundle import Bundle


class TestFHIRStructureDefinitionRenderer(unittest.TestCase):

    def test_bundle_iteration(self):
        # Create a sample Bundle instance with entries
        data = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [
                {"resource": {"id": "1"}},
                {"resource": {"id": "2"}},
            ]
        }
        bundle = Bundle(data)

        # Test that Bundle is iterable
        entries = list(bundle)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].resource.id, "1")
        self.assertEqual(entries[1].resource.id, "2")


if __name__ == '__main__':
    unittest.main()
