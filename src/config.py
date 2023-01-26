from configparser import ConfigParser
import logging
import sys

class Settings():
    def __init__(self):
        pass
    
    @staticmethod
    def get_config(config_path):
        """
        This loads the configuration. The next step would be to add the capacity to load custom configurations.  
        """
        
        parser = ConfigParser()
        try :
            curr_config = parser.read_file(config_path)
        except:
            
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
    
    @staticmethod
    def start_log():
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
