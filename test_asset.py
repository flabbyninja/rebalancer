import unittest

from asset import Asset

class TestAsset(unittest.TestCase):

    def setUp(self):
        super(TestAsset, self).setUp()
        name = "Acme Ltd"
        type = "Equity"
        sector = "Healthcare"
        self.test_asset = Asset(name, type, sector)

    def test_asset_format(self):
        """
        Test format of asset output
        """
        result = self.test_asset.format_asset()
        self.assertEqual(result, "Name: Acme Ltd, Type: Equity, Sector: Healthcare")

    def test_asset_values(self):
        """
        Test initialisation of asset values
        """
        self.assertEqual(self.test_asset.name, "Acme Ltd")
        self.assertEqual(self.test_asset.sector, "Healthcare")
        self.assertEqual(self.test_asset.type, "Equity")


if __name__ == '__main__':
    unittest.main()