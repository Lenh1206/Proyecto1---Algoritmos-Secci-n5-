class Entrada:
    def __init__(self, id, cliente, asiento, fecha, partido, is_vip, status):
        self.id = id
        self.sit = asiento
        self.date = fecha
        self.match = partido
        self.is_vip = is_vip
        self.status = status
        self.cliente = cliente
    
    def return_sdd(self):
        return {'id':self.id,
'sit':self.sit,
'date':self.date,
'game':self.match,
'is_vip':self.is_vip,
'status':self.status,
'client_id':self.cliente}

