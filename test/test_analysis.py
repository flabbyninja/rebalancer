from unittest.case import expectedFailure
from analysis.analysis import analyse_sectors
import unittest

from asset import Asset
import analysis

class TestAnalysis(unittest.TestCase):
    def test_asset_analysis(self):
        """
        Test analysis
        """
        assets = [Asset("Acme", "Equity", "Technology"), Asset("Beta", "Fixed Income", "Healthcare"), Asset("Carrot", "Derivative", "Healthcare")]
        result = analyse_sectors(assets)
        expectedResult = {
            "Technology": 1,
            "Healthcare": 2
        }
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()