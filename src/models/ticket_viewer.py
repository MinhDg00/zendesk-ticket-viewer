import requests 
from config.config import *
from models.ticket_retriever import TicketRetriever

class TicketViewer: 
    
    def __init__(self):
        self.retriever = TicketRetriever(USER_NAME, DOMAIN, PASSWORD) 
        self.page_count = self.retriever.get_page_count() 
        self.current_page = 1
        self.has_next_page = None  
        self.has_prev_page = None 

    def view_ticket_list(self, page_number = 1):
        
        if 1 <= int(page_number) <= int(self.page_count):
            try:
                ticket_list_per_page, prev_page_url, next_page_url =  self.retriever.retrieve_ticket_by_page(page_number)
                self.has_prev_page = (prev_page_url is not None)
                self.has_next_page = (next_page_url is not None)
                for t in ticket_list_per_page:
                    print(t)
                print()
                print(f"Page {page_number}/{self.page_count}")
                self.current_page = page_number 
            except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
                print(e.response.text)
                return
        else:
            print( f"\n Invalid Page Number or Next/Previous Page does not exist. Please Input Again!!\n")
                    
    def view_individual_ticket(self, id):
        try:
            ticket = self.retriever.retrieve_individual_ticket(id)
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
            print(e.response.text)
            return

        if ticket: print(ticket.get_ticket_detail())
        else: print('Id not does not exist')

    def display_header(self):
        print("\n-------------------- ZENDESK TICKET VIEWER --------------------\n") 
        print("                     Domain: zccmdang                         \n")
        print("                     Username: minh.dg96gmail.com             \n")
        print("-----------------------------------------------------------------\n")

    def display_main_menu(self):
        print("\n~~~MAIN MENU OPTIONS~~~\n") 
        print("- Press 1 to view all tickets")
        print("- Press 2 to view details of a ticket")
        print("- Press 3 to quit\n")

    def display_page_menu(self):
        print("\n~~~PAGINATION OPTIONS~~~\n")
        print("- Type p/prev to go to previous page")
        print("- Type n/next to go to next page ")
        print(f"- Type page number (1 to {self.page_count}) to jump to specific ticket page ")
        print("- Type m/menu to go back to main view options ")
        print("- Type e/exit to exit the ticket viewer \n")

    def display_id_request(self):
        print("\nInput ticket id: ")

    def display_back_to_main_menu(self):
        print("\nBack to main menu optsions ... ")
        
    def display_end_message(self):
        print("\nProgram exited")
        print("Thank you for using Zendesk Ticket Viewer version zccmdang \n")
    
    def display_invalid_message(self):
        print("\n ERROR: Invalid Input. Please Input Again.")