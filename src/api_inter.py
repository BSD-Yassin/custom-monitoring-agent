import requests 

class AgentApi():
    def __init__(self, logger):
        self.logger = logger 

class Ansible_tower(AgentApi):
    """
    As the concept of this agent is very simple, it could easily be ported to another provisioning tool or used on a private API
    Hence the sublass Ansible_tower, to account of any following API to come
    """
    def __init__(self, ansible_url):
        super().__init__()
        self.ansible_url = ansible_url
    
    def test_api_availability(self,ansible_url):
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

    def send_trigger_alert(self, ansible_url, trigger_data):
        """
        This sends the trigger_alert data to the Tower if anything is changed. 
        """
        try:
            request = requests.post(ansible_url, trigger_data)

            return request
        except:
            self.logger.error('Ansible API unavailable')
            return False
