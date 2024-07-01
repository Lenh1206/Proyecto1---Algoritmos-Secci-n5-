from log_clients import lista_clientes, lista_tickets

def check_in(id_ticket_showed, lista_tickets):
    ticket_to_compare = None
    for ticket in lista_tickets:
        if ticket.id == id_ticket_showed:
           ticket_to_compare = ticket 
    if ticket_to_compare:
        if ticket_to_compare.status == 'Unclaimed':
            print('\nTodo en orden. La entrada ha sido validada.')
            ticket_to_compare.status = 'Claimed'
        else:
            print('\nEl ticket ya se encuentra reclamado. Es posible que el ticket no sea autentico.')
    else:
        print('\nNo hay un ticket registrado con la id señalada.')
                
    