import unittest

import os
from persistence import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

class TestPersistence(unittest.TestCase):

    def setUp(self):
        super(TestPersistence, self).setUp()
        self.db_file = 'test.sqlite3'
        conn_string = 'sqlite:///{}'.format(self.db_file)
        engine = create_engine(conn_string)
        Base.metadata.create_all(engine) # here we create all tables
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def test_asset_save(self):
        """
        Test saving asset to database
        """
        new_user = User(name='test')
        self.session.add(new_user)
        self.session.commit()

    def tearDown(self) -> None:
        super(TestPersistence, self).tearDown()
        if os.path.exists(self.db_file):
            os.remove(self.db_file)


if __name__ == '__main__':
    unittest.main()