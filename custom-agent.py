import hashlib
import sys
import os
import requests
from configparser import ConfigParser
import logging

chksum_list = os.listdir()

class CustomAgent_Monitoring():
    def __init__(self, config_path="./ansible_agent.cfg"):
        self.config_path = config_path
        self.config = self.get_config()
        self.logger = self.start_log()
        self.ansitower_availability = self.test_api_availability(self.config["DEFAULT"]["AnsibleUrl"])
        self.inifile = self.config['DEFAULT']['ConfFile']
        self.monitoring_data = []

    def get_config(self):
        """
        This loads the configuration. The next step would be to add the capacity to load custom configurations.  
        """
        parser = ConfigParser()
        config_path = self.config_path
        parser["DEFAULT"] = {
            "AnsibleUrl": "http://127.0.0.1:8000",
            "DirFiles": "../dir_files/",
            "ConfFile": "../ansible_monitor.ini",
            "Logging": "True",
            "LoggingOutput": "custom_agent.log"}

        curr_config = parser
        with open(f"logs/{config_path}", "w") as cfg:
            parser.write(cfg)
            cfg.close()
            return curr_config

    def start_log(self):
        """
        This creates a centralized log for the whole app
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler('logs/logs.log')
        fileHandler.setFormatter(logging.Formatter(
            fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        logger.addHandler(fileHandler)
        streamHandler = logging.StreamHandler(stream=sys.stdout)
        streamHandler.setFormatter(logging.Formatter(
            fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        logger.addHandler(streamHandler)
        return logger

    def test_api_availability(self, ansible_url):
        """
        This checks the API availability, can be used as decorator before a query, or test for debug
        """
        try:
            response = requests.get(ansible_url, "API_TEST")
            if response.status_code == 200:
                self.logger.info('Connection to API')
            return True
        except:
            self.logger.error("API couldn't be found.")
            return False

    def send_trigger_alert(self, trigger_data):
        """
        This sends the trigger_alert data to the Tower if anything is changed. 
        """
        try:
            ansiaddr = self.config["DEFAULT"]["AnsibleUrl"]
            request = requests.post(ansiaddr, trigger_data)

            return request
        except:
            self.logger.error('Ansible API unavailable')
            self.logger.error(
                f'The alert was documented in : {self.config["DEFAULT"]["LoggingOutput"]}')
            return False

    def get_files_stat(self):
        """
        This loads the file details from reference file given from Ansible. 
        """
        parser = ConfigParser()
        log_infos = parser.read_file(self.config_path)
        print(log_infos)


    def checksum(self, name_file, hash_function="sha256"):
        """
        This checks the file checksum value from the reference to the actual file 
        """
        with open(f"./{self.config['dir_path']}{name_file}", 'rb') as actual_file:
            bytes = actual_file.read()
            if hash_function == "md5":
                try:
                    readable_hash = hashlib.md5(bytes).hexdigest()
                except:
                    self.logger.error(
                        f"Something went wrong while trying to find the checksum. {hash_function} : {actual_file}")
            elif hash_function == "sha256":
                try:
                    readable_hash = hashlib.sha256(bytes).hexdigest()
                except:
                    self.logger.error(
                        f"Something went wrong while trying to find the checksum. {hash_function} : {actual_file}")
            else:
                self.logger.error(
                    f"This hashtype doesn't exist. {hash_function}")
            return readable_hash

    def check_file_size(self, name_file):
        """
        This checks the file size 
        """
        with open(f"./{self.config['dir_path']}{name_file}", 'rb') as actual_file:
            pass

    def check_file_attrs(self):
        """
        This will centralize every function for the attributes to be analyzed, from a default directory.
        """
        dir_path = self.config["DEFAULT"]["DirFiles"]
        dir_files = os.listdir(dir_path)
        for dir_file in dir_files:
            self.checksum(name_file=dir_file)
            continue
    
    def check_apps():
        """
        This will follow up on the state of declared apps 
        """
        pass

    def check_user_activity():
        """
        This will follow the user activity
        """
        pass


if __name__ == "__main__":
    Instance = CustomAgent_Monitoring()
    Instance.get_files_stat()
