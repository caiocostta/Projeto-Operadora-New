from App.Models.operatordb import connectToOperatorDB

def getAllOperators() -> list:
    query = ''' select * from operator 
            order by operatorName asc
            '''
    conn = connectToOperatorDB()

    conn.execute(query)
    operators = conn.fetchall()
    conn.commit()
    conn.close()

    return operators

def getOperatorByID (operatorId: int) -> str:
    query = ''' SELECT * FROM Operator WHERE OperatorID = {} '''.format(operatorId)
    conn = connectToOperatorDB()

    conn.execute(query)
    operator = conn.fetchone()
    conn.commit()
    conn.close()

    try:
        return operator
    except:
        return None

def getOperatorByName (operatorName) -> str:
    query = ''' SELECT * FROM Operator WHERE OperatorName LIKE '%{}%' '''.format(operatorName)
    conn = connectToOperatorDB()

    conn.execute(query)
    operator = conn.fetchall()
    conn.commit()
    conn.close()

    try:
        return operator
    except:
        return None

def getOperatorByEqualName (operatorName) -> str:
    query = ''' SELECT * FROM Operator WHERE OperatorName = '{}' '''.format(operatorName)
    conn = connectToOperatorDB()

    conn.execute(query)
    operator = conn.fetchone()
    conn.commit()
    conn.close()

    try:
        return operator
    except:
        return None


def getAllContacts() -> list:
    query = ''' select * from Contact '''
    conn = connectToOperatorDB()

    conn.execute(query)
    contacts = conn.fetchall()
    conn.commit()
    conn.close()

    return contacts

def getContactsByOperatorID(operatorID) -> list:
    query = ''' SELECT * FROM Contact 
            WHERE OperatorID ={}
            '''.format(operatorID)
    conn = connectToOperatorDB()

    conn.execute(query)
    contacts = conn.fetchall()
    conn.commit()
    conn.close()
    try:
        return contacts
    except:
        return None
