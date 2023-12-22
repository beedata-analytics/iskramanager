# -*- coding: utf-8 -*-
import json


class HTTPError(Exception):
    pass


class CompanyManager:
    def __init__(self, session, company_name, url):
        self.session = session
        self.company_name = company_name
        self.base_url = url

    def create_company(self):
        if self.is_new_company():
            try:
                self.create_company_account("DataAccount")
                self.create_company_account("Account")
                self.update_company_settings()
                return True, "Company successfully created"
            except HTTPError as e:
                return False, f"{e}"
        else:
            return True, "The company already exists"

    def delete_company(self):
        try:
            self.delete_company_account("DataAccount")
            self.delete_company_account("Account")
            return True, "Company successfully deleted"
        except HTTPError as e:
            return False, f"{e}"

    def is_new_company(self):
        url = f"{self.base_url }/db/{self.company_name}"
        response = self.session.get(url)
        return response.status_code == 404

    def create_company_account(self, type_account):
        data = {
            "@type": type_account,
            "id": self.company_name,
            "title": self.company_name,
        }
        account = "/data" if type_account == "DataAccount" else "/db"
        url = f"{self.base_url}{account}"
        response = self.session.post(url, data=json.dumps(data))
        if response.status_code != 200:
            message = f"{response.status_code} - {response.response_text}"
            raise HTTPError(message)

    def get_company_account(self, type_account):
        account = "/data" if type_account == "DataAccount" else "/db"
        url = f"{self.base_url}{account}/{self.company_name}"
        response = self.session.get(url)
        return response.json()

    def delete_company_account(self, type_account):
        account = "/data" if type_account == "DataAccount" else "/db"
        url = self.base_url + f"/{account}/{self.company_name}"
        response = self.session.delete(url)
        if response.status_code != 200:
            message = f"{response.status_code} - {response.text}"
            raise HTTPError(message)

    def update_company_settings(self):
        # Update required settings for the db account
        data = {
            "@behaviors": ["guillotina_serviceaccount.interfaces.IServiceAccount"],
            "languages": ["es", "ca"],
            "default_language": "ca",
        }
        url = self.base_url + f"/db/{self.company_name}"
        response = self.session.patch(url, data=json.dumps(data))
        if response.status_code != 204:
            message = f"{response.status_code} - {response.response_text}"
            raise HTTPError(message)
