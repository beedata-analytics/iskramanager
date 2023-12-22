import click
import json
import csv
import company
import contract
from requests.auth import HTTPBasicAuth
from requests.sessions import Session


@click.group()
def ciit():
    pass


@ciit.command()
@click.option("--config_file", type=click.Path(exists=True), required=True)
@click.option("--company_name", type=str, required=True)
@click.option("--company_id", type=str, required=True)
@click.option(
    "--operation",
    type=click.Choice(["create", "load", "delete", "list"]),
    required=True,
)
@click.option("--contracts_file", type=click.Path(exists=True), required=False)
@click.option("--testing", is_flag=True)
@click.option("--production", is_flag=True)
def run(
    config_file,
    company_name,
    company_id,
    operation,
    contracts_file=None,
    testing=True,
    production=False,
):
    try:
        with open(config_file) as config_file:
            config = json.load(config_file)
    except Exception as e:
        return False, f"Required configuration file: {e}"

    try:
        with Session() as session:
            session.auth = HTTPBasicAuth(
                config.get("user", ""), config.get("password", "")
            )
            session.headers.update({"Content-Type": "application/json"})
    except Exception as e:
        return False, f"HTTP session: {e}"

    contracts = []
    if contracts_file:
        with open(contracts_file) as file:
            contracts = [line[0] for line in csv.reader(file)]
    url = config.get("testing", "") if testing else config.get("production", "")
    um = company.CompanyManager(session, company_name, url)
    cm = contract.ContractManager(session, company_name, company_id, contracts, url)

    if operation == "create":
        was_created, message = um.create_company()
        if not was_created:
            return False, message
        if was_created and contracts:
            return cm.load_contracts()

    if operation == "delete":
        if contracts:
            return cm.delete_contracts()
        else:
            return um.delete_company()

    # TO DO
    # if operation == "list":


if __name__ == "__main__":
    ciit(obj={})
