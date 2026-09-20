DB_CONFIG = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "database": "hospital_db"
}

DATA_PATH = "datasets/"



## Configuration

### The `config.py` file stores the configuration details required by the ETL pipeline.

### It contains the MySQL database username, password, host, and database name.

### The `DATA_PATH` variable stores the location of the CSV files. 

### Keeping configuration details in a separate file makes the pipeline easier to maintain and prevents database settings from being repeated in multiple Python files.