import unittest
from src.pipeline.data_pipeline import pull_data_from_api, store_data_in_db, feed_data_to_model

class TestDataPipeline(unittest.TestCase):

    def test_pull_data_from_api(self):
        data = pull_data_from_api()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)  # Assuming the API returns a list of data

    def test_store_data_in_db(self):
        sample_data = [{'id': 1, 'name': 'Sample Game', 'score': 100}]
        result = store_data_in_db(sample_data)
        self.assertTrue(result)  # Assuming the function returns True on success

    def test_feed_data_to_model(self):
        sample_data = [{'id': 1, 'name': 'Sample Game', 'score': 100}]
        predictions = feed_data_to_model(sample_data)
        self.assertIsNotNone(predictions)
        self.assertIsInstance(predictions, list)  # Assuming the model returns a list of predictions

if __name__ == '__main__':
    unittest.main()