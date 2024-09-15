from main import add

import pandas as pd

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('your_dataset.csv')

    def test_summary_statistics(self):
        summary_stats = self.df.describe(include='all')
        self.assertTrue(not summary_stats.empty, "Summary statistics should not be empty")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

