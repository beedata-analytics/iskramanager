# -*- coding: utf-8 -*-
import json
from multiprocessing import Pool


class HTTPError(Exception):
    pass


def create_contract(data):
    session = data[0]
    company_name = data[1]
    company_id = data[2]
    contract_id = data[3]
    url = data[4]

    data = {"@type": "Contract", "id": contract_id, "companyId": company_id}
    url += f"/data/{company_name}"

    response = session.post(url, data=json.dumps(data))
    if response.status_code != 201:
        err_detail = f"{contract_id}: {response.status_code} - {response.text}"
        raise HTTPError(f"Error creating contract {err_detail}")


def delete_contract(data):
    session = data[0]
    company_name = data[1]
    contract_id = data[2]
    url = f"{data[3]}/data/{company_name}/{contract_id}"

    response = session.delete(url)
    if response.status_code != 200:
        err_detail = f"{contract_id}: {response.status_code} - {response.text}"
        raise HTTPError(f"Error deleting contract {err_detail}")


class ContractManager:
    def __init__(self, session, company_name, company_id, contracts, url):
        self.session = session
        self.company_name = company_name
        self.company_id = company_id
        self.contracts = contracts
        self.base_url = url

    def load_contracts(self):
        queue = [
            (
                self.session,
                self.company_name,
                self.company_id,
                contract_id,
                self.base_url,
            )
            for contract_id in self.contracts
        ]
        try:
            with Pool() as pool:
                pool.map(create_contract, queue)
            return "True", "Contracts were sucessfully load"
        except HTTPError as e:
            return False, e

    def delete_contracts(self):
        queue = [
            (
                self.session,
                self.company_name,
                contract_id,
                self.base_url,
            )
            for contract_id in self.contracts
        ]
        try:
            with Pool() as pool:
                pool.map(delete_contract, queue)
            return "True", "Contracts were sucessfully deleted"
        except HTTPError as e:
            return False, e
