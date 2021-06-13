import unittest

from asset import Asset

class TestAsset(unittest.TestCase):
    def test_asset_init(self):
        """
        Test initialisation of asset
        """
        name = "Acme Ltd"
        type = "Equity"
        sector = "Healthcare"
        test_asset = Asset(name, type, sector)
        result = test_asset.format_asset()
        self.assertEqual(result, "Name: Acme Ltd, Type: Equity, Sector: Healthcare")

if __name__ == '__main__':
    unittest.main()