from os import path

import confuse

BASE_DIR = path.dirname(path.abspath(__file__))

config = confuse.Configuration("Transfer", __name__)
config.set_file(path.join(BASE_DIR, "credentials.yaml"))

SOURCE = str(config["source"])
DESTINATION = str(config["destination"])

CSV_SOURCE_PATH = str(config["csv_source_path"])

POSTGRES_DESTINATION_CREDS = {
    "dbname": config["pg_dest"]["dbname"],
    "user": config["pg_dest"]["user"],
    "password": config["pg_dest"]["password"],
    "host": config["pg_dest"]["host"],
    "port": config["pg_dest"]["port"],
}
