import json
import os

##########

"""
This is intended to allow the user to pass in a JSON Service Account Key instead
of the individual fields.

TODO - Make this forwards compatible with Google Secrets Manager
"""
if os.environ.get("DESTINATION_USE_JSON") == "true":
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        raise OSError("You must set the path to a JSON Service Account Key")

    # Load the JSON file and set the environment variables
    with open(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]) as _fp:
        creds = json.load(_fp)

        os.environ["DESTINATION_PROJECT_ID"] = creds["project_id"]
        os.environ["DESTINATION_PRIVATE_KEY"] = creds["private_key"]
        os.environ["DESTINATION_CLIENT_EMAIL"] = creds["client_email"]


BIGQUERY_DESTINATION_CONFIG = {
    "DESTINATION__BIGQUERY__LOCATION": os.environ.get("DESTINATION_LOCATION"),
    "DESTINATION__BIGQUERY__CREDENTIALS__PROJECT_ID": os.environ.get("DESTINATION_PROJECT_ID"),
    "DESTINATION__BIGQUERY__CREDENTIALS__PRIVATE_KEY": os.environ.get("DESTINATION_PRIVATE_KEY"),
    "DESTINATION__BIGQUERY__CREDENTIALS__CLIENT_EMAIL": os.environ.get("DESTINATION_CLIENT_EMAIL"),
}


SQL_SOURCE_CONFIG = {
    "SOURCES__SQL_DATABASE__CREDENTIALS__DRIVERNAME": os.environ.get("SOURCE_DRIVERNAME"),
    "SOURCES__SQL_DATABASE__DATABASE": os.environ.get("SOURCE_DATABASE"),
    "SOURCES__SQL_DATABASE__HOST": os.environ.get("SOURCE_HOST"),
    "SOURCES__SQL_DATABASE__PORT": os.environ.get("SOURCE_PORT"),
    "SOURCES__SQL_DATABASE__USERNAME": os.environ.get("SOURCE_USERNAME"),
    "SOURCES__SQL_DATABASE__PASSWORD": os.environ.get("SOURCE_PASSWORD"),
}
