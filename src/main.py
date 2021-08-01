from models.ticket_viewer import TicketViewer
import sys 

def main(): 
    
    ticket_viewer = TicketViewer()
    ticket_viewer.display_header()
    command = ""

    while command != '3': 

        ticket_viewer.display_main_menu()
        command = input()

        if command == '1':
            ticket_viewer.view_ticket_list()
            page_command = ""

            while page_command.lower() not in ['e', 'exit']:
                ticket_viewer.display_page_menu()
                page_command = input() 
                if page_command.lower() in ['p', 'prev']:
                    ticket_viewer.view_ticket_list(ticket_viewer.current_page - 1)
                elif page_command.lower() in ['n', 'next']:
                    ticket_viewer.view_ticket_list(ticket_viewer.current_page + 1)
                elif page_command.isnumeric():
                    ticket_viewer.view_ticket_list(int(page_command))
                elif page_command.lower() in ['m', 'menu']:
                    ticket_viewer.display_back_to_main_menu() 
                    break 
                elif page_command.lower() in ['e', 'exit']:
                    sys.exit(ticket_viewer.display_end_message()) 
                else:
                    print('Invalid Input. Please input again: \n')

        elif command == '2':
            ticket_viewer.display_id_request()
            ticket_id = input()
            ticket_viewer.view_individual_ticket(ticket_id)
            ticket_viewer.display_back_to_main_menu()

        elif command == '3':
            sys.exit(ticket_viewer.display_end_message())

        else:
            print('Invalid Input. Please input again: \n')  
            
if __name__ == "__main__":
    main() 
