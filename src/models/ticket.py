class Ticket:
    '''
    Zendesk Ticket Class
    '''
    def __init__(self, ticket):

        self.created_at = ticket["created_at"]
        self.id = ticket["id"]
        self.assignee_id = ticket["assignee_id"]
        self.submitter_id = ticket["submitter_id"]
        self.subject = ticket["subject"]
        self.description = ticket["description"]
        self.requester_id = ticket["requester_id"]
        self.status = ticket["status"]

    def __str__(self):
        return f"Ticket Id: {self.id} || Created At:{self.created_at} || Assigned To: {self.assignee_id} || Status: {self.status}"      
    
    def get_ticket_detail(self):
        return f"\n Ticket ID: {self.id} \n Created At: {self.created_at} \n Assigned To: {self.assignee_id} \n Status: {self.status} \n Subject: {self.subject} \n Description: {self.description} \n"

