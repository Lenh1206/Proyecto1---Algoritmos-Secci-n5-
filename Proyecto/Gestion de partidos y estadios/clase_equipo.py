class Equipo():
    def __init__(self, id, code, group, name) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.group = group
    
    def return_to_sdd(self):
        return {'id':self.id, 
'code':self.code, 
'name':self.name,
'group':self.group}

