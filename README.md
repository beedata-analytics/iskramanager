### Iskra manager

The library allows to execute 4 type of actions:

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

1. Create
   Allows to create a company and if the contracts_file parameter is provided, the process also proceeds to create the contracts included in that file.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  create
  --contracts_file data/contracts.csv
  --testing  
```

2. Load
   Allows to load new contracts for a company.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  load
  --contracts_file data/contracts.csv
  --testing  
```

3. Delete
   If the contracts_file parameter is provided, the process only proceeds to delete the contracts included in that file.
   Otherwise the process deletes the company.

```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  delete
  --contracts_file data/contracts.csv
  --testing
```

4. List [TO DO]
   Generates a csv with contracts loaded of a certain company.
```sh
python main.py run
  --config_file config.json
  --company_name sieactiva
  --company_id 999999
  --operation  list  
  --testing
```

##### RUN tests
python -m unittest test/test_company.py
python -m unittest test/test_contracts.py [TO DO]
