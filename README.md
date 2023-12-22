## Iskra manager

The library allows to execute the following operations:

```sh
python main.py run
  --config_file <config_file>
  --company_name <company_name>
  --company_id <company_id>
  --operation  <create, load, delete, list>
  [--contracts_file <contracts_file>]  
  [--testing]
  [--production]  
```

##### 1.CREATE

Create a company and if the contracts_file parameter is provided, the process also proceeds to create the contracts included in that file.

Example: Creation of sieactiva company and load contracts in testing environment.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  create
  --contracts_file data/contracts.csv
  --testing  
```

##### 2. LOAD

Load new contracts for a company.

Example: Load of contracts from sieactiva company in testing environment.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  load
  --contracts_file data/contracts.csv
  --testing  
```

##### 3. DELETE

If the contracts_file parameter is provided, the process only proceeds to delete the contracts included in that file for the company_name.Otherwise the process deletes the company.

Example: Delete of contracts from sieactiva company in testing environment.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  delete
  --contracts_file data/contracts.csv
  --testing
```

##### 4. LIST

Generates a csv with contracts loaded of a certain company. (TO DO)


##### RUN tests

python -m unittest test/test_company.py

python -m unittest test/test_contracts.py (TO DO)
