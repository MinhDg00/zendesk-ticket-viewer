import requests 
from models.ticket import Ticket 
from config.config import *

class TicketRetriever:
    '''
    Facilitate ticket retrieving service 
    '''

    def __init__(self, user_name = USER_NAME, domain = DOMAIN, password = PASSWORD):
        self.user_name = user_name 
        self.domain = domain 
        self.password = password 
        self.url = ""
        self.limit = 25
        

    def retrieve_individual_ticket(self, id):
        '''
        Args: 
            id: ID of the ticket user wants to retrieve 
        Return: Ticket class 
        ''' 
        sid = str(id)
        self.url = f"https://{self.domain}.zendesk.com/api/v2/tickets/{sid}.json"
        response = requests.get(self.url, auth = (self.user_name, self.password))
        try:
            response.raise_for_status() 
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            raise
        
        ticket_info = response.json() 
        t = ticket_info["ticket"]

        return Ticket(t)

    def retrieve_ticket_by_page(self, page_number = 1):

        '''
        Args:
            page: the page that user want to retrieve tickets. 
        Retrieve tickets in specified page
        '''
        
        self.url =  f"https://{self.domain}.zendesk.com/api/v2/tickets.json?per_page={self.limit}&page={page_number}"
        response = requests.get(self.url, auth = (self.user_name, self.password))
        try:
            response.raise_for_status() 
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            raise
        
        page_tickets_info = response.json()

        return [Ticket(t) for t in page_tickets_info["tickets"]], page_tickets_info["previous_page"], page_tickets_info["next_page"]

    def get_page_count(self):
        self.url = f"https://{self.domain}.zendesk.com/api/v2/tickets/count.json"
        print(self.url)
        response = requests.get(self.url, auth = (self.user_name, self.password))
        try:
            response.raise_for_status() 
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            return -1

        count_info = response.json()
        count_decimal = count_info['count']['value']/ self.limit
        return int(count_decimal) if int(count_decimal) == count_decimal else int(count_decimal) + 1

    # def retrieve_all_ticket(self):
    #     """
    #     Retrieve all tickets through Zendesk API
    #     """

    #     self.url = "https://{self.domain}.zendesk.com/api/v2/tickets.json}"
    #     response = requests.get(self.url, auth = (self.user_name, self.password))
    #     try:
    #         response.raise_for_status() 
    #     except requests.exceptions.RequestException as er:
    #         print(er.response.text)
    #     except requests.exceptions.HTTPError as eh:
    #         print(eh.response.text)
        
    #     tickets_info = response.json() 

    #     return [Ticket(t) for t in tickets_info["tickets"]]