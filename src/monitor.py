import hashlib
import sys
import os
from configparser import ConfigParser

class Mon():
    def __init__(self, config, logger):
        self.config = config 
        self.logger = logger
        
    def get_files_stat(self):
        """
        This loads the file details from reference file given from Ansible. 
        """
        parser = ConfigParser()
        log_infos = parser.read_file(self.config['DEFAULT']['ConfFile'])
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
            file_hash = self.checksum(name_file=dir_file)
            file_size = self.check_file_size()
        ## return monitor_data
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



