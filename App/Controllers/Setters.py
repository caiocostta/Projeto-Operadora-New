from App.Models.operatordb import connectToOperatorDB


def addOperator(operatorName:str, businessHour:str, operatorNotes:str) -> bool:
    try:
        query = '''insert into Operator 
        values ('{}', '{}', '{}')
        '''.format(operatorName, businessHour, operatorNotes)
        conn = connectToOperatorDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao adicionar Operadora")
        return False

def updateOperator(operatorID:int, newOperatorName: str,  newNotes: str, newBusinessHour: str) -> bool:
    try:
        query = '''UPDATE  Operator 
                SET OperatorName= '{}',
                notes= '{}',
                businessHour= '{}'
                WHERE OperatorID= {};
        '''.format(newOperatorName, newNotes, newBusinessHour, operatorID)
        conn = connectToOperatorDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao adicionar Operadora")
        return False

def addContact(operatorID:int, telphone:str, celphone:str) -> bool:
    try:
        query = '''insert into Contact 
        values ('{}', '{}', '{}')
        '''.format(operatorID, telphone, celphone)
        conn = connectToOperatorDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao adicionar Telefone")
        return False

def putContact(operatorID:int, telphone:str, celphone:str) -> bool:
    try:
        query = '''UPDATE Contact 
        SET TelPhone = '{}',
        CelPhone = '{}'
        WHERE OperatorID = {}
        '''.format(telphone, celphone, operatorID)
        conn = connectToOperatorDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao adicionar Telefone")
        return False

def deleteOperator(operatorID: int):
    try:
        query = '''DELETE FROM Operator 
                WHERE OperatorID = {}
                
                DELETE FROM Contact 
                WHERE OperatorID = {}
                '''.format(operatorID, operatorID)
        
        conn = connectToOperatorDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar Operadora")
        return False
