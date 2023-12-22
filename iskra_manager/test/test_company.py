import sys
import unittest
import json
import company
from requests.auth import HTTPBasicAuth
from requests.sessions import Session
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(__file__) + '/..'))


config = dirname(__file__) + '/../config.json'
with open(config) as config_file:
    config = json.load(config_file)

with Session() as session:
    session.auth = HTTPBasicAuth(
        config.get("user", ""), config.get("password", "")
    )
    session.headers.update({"Content-Type": "application/json"})


class TestCompany(unittest.TestCase):
    def test_create_delete_company(self):
        manager = company.CompanyManager(session, "test_1", config["testing"])
        result = manager.create_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully created")
        result = manager.delete_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully deleted")

    def test_is_new_company(self):
        manager = company.CompanyManager(session, "test_2", config["testing"])
        result = manager.is_new_company()
        self.assertEqual(result, True)

    def test_no_is_new_company(self):
        manager = company.CompanyManager(session, "test_3", config["testing"])
        result = manager.create_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully created")
        result = manager.is_new_company()
        self.assertEqual(result, False)
        result = manager.delete_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully deleted")

    def test_get_company_account(self):
        manager = company.CompanyManager(session, "test_4", config["testing"])
        result = manager.create_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully created")
        result = manager.get_company_account("DataAccount")
        self.assertEqual(result["type_name"], "DataAccount")
        result = manager.get_company_account("Account")
        self.assertEqual(result["type_name"], "Account")
        result = manager.delete_company()
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Company successfully deleted")


if __name__ == '__main__':
    unittest.main()

