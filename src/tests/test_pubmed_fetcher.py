import unittest
from pubmed_fetcher import fetch_pubmed_data, get_paper_details, is_non_academic_affiliation, filter_non_academic_authors

class TestPubMedFetcher(unittest.TestCase):
    def test_fetch_pubmed_data(self):
        query = "cancer[Title/Abstract]"
        result = fetch_pubmed_data(query, max_results=5)
        self.assertIsInstance(result, list)
        self.assertLessEqual(len(result), 5)

    def test_get_paper_details(self):
        pubmed_id = "12345678"  # Replace with a valid PubMed ID for testing
        result = get_paper_details(pubmed_id)
        self.assertIsInstance(result, dict)

    def test_is_non_academic_affiliation(self):
        self.assertTrue(is_non_academic_affiliation("Genentech Inc."))
        self.assertFalse(is_non_academic_affiliation("Harvard University"))

    def test_filter_non_academic_authors(self):
        paper_details = {
            "authors": [
                {"name": "John Doe", "affiliations": ["Genentech Inc."]},
                {"name": "Jane Smith", "affiliations": ["Harvard University"]}
            ]
        }
        result = filter_non_academic_authors(paper_details)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "John Doe")

if __name__ == "__main__":
    unittest.main()