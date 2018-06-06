from unittest import TestCase
from code import DBConnection
import mock
import mongomock
import errno


class TestsDBConnection(TestCase):

    def setUp(self):
        self.dbconnection = DBConnection()
        self.dbconnection.client = mongomock.MongoClient()
        self.dbconnection.db = self.dbconnection.client[
            self.dbconnection.db_name]

    def test_save_in_database(self):
        self.dbconnection = DBConnection()
        self.dbconnection.is_in_database = mock.MagicMock(return_value=False)
        self.assertIsNotNone(self.dbconnection.save_in_database("lola", 3))

    def test_save_in_database_already_in_db(self):
        self.dbconnection = DBConnection()
        self.dbconnection.is_in_database = mock.MagicMock(return_value=True)
        self.assertIsNotNone(self.dbconnection.save_in_database("lola", 3))

    def test_get_all_data_from_database(self):
        self.dbconnection = DBConnection()
        self.dbconnection.save_in_database("lola", 2)
        item = self.dbconnection.get_all_data_from_database()
        assert(('lola', 2) in item)

    def test_delete_database(self):
        self.dbconnection = DBConnection()
        self.dbconnection.delete_database()
        item = self.dbconnection.get_all_data_from_database()
        assert(item == [])

    def test_get_all_data_when_db_is_empty(self):
        self.dbconnection = DBConnection()
        self.dbconnection.delete_database()
        item = self.dbconnection.get_all_data_from_database()
        assert(item == [])

    def test_is_in_database(self):
        self.dbconnection = DBConnection()
