import requests
import json
import re
from google.cloud import bigquery
from google.oauth2 import service_account

class QueryBigquery:
    def __init__(self):
        with open("env.txt", "r") as f:
            self.env_var = json.load(f)
        with open("url.json", "r") as f:
            self.link = json.load(f)
        credentials = service_account.Credentials.from_service_account_file(self.env_var['credentials_path'])
        self.client = bigquery.Client(credentials=credentials, project=self.env_var['project_id'])
        self.job_config = bigquery.job.QueryJobConfig(use_query_cache=self.env_var['use_query_cache'])

    def run_merge_scripts(self):
        with open("merge_script_path.txt", "r") as f:
            for sql_script in f:
                sql_url = sql_script.strip()
                if re.match("^#",sql_url):
                    continue
                try:
                    query = requests.get(sql_url).text
                    result = self.client.query_and_wait(query, job_config=self.job_config).to_dataframe().to_json()
                    return "SQL script run is successful"
                except requests.ConnectionError as e:
                    return f"Invalid URL for {sql_url} -- {e}"

            
    def query_selector(self, report_name):
        if report_name in self.link:
            self.url = self.link[report_name]
            try:
                query = requests.get(self.url).text
                result = self.client.query_and_wait(query, job_config=self.job_config).to_dataframe().to_json()
                return result
            except requests.ConnectionError as e:
                return f"Invalid URL for {report_name} - {self.url} {e}"
        else:
            return f"The report name {report_name} is not in the list"

