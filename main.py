from src import config
from src import monitor
from src import api_inter

class CustomAgent_Monitoring():
    """
    If you don't define a path for ansible_agent, it will be set on the default path
    """
    def __init__(self, config_path="./ansible_agent.cfg"):
        self.config = config.Settings.get_config(config_path)
        self.logger = config.Settings.start_log()
        self.monitor = monitor.Mon(self.config, self.logger)


if __name__ == "__main__":
    Instance = CustomAgent_Monitoring()
    print(Instance.config)
    print(Instance.logger)
    print(Instance.monitor)
