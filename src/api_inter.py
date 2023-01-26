
class AgentApi():
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
