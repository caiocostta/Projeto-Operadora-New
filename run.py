from flask import Flask, redirect, render_template, request
from App.Controllers.Getters import getAllOperators, getAllContacts, getContactsByOperatorID, getOperatorByEqualName, getOperatorByID, getOperatorByName
from App.Controllers.Setters import addOperator, addContact, deleteOperator, putContact, updateOperator

app = Flask(__name__, template_folder='App/Templates',  static_folder='App/Static')

operatorInfo = any
allOperators = any
allContacts = any

@app.context_processor
def setMenuGlobalVariables():
  allOperators = getAllOperators()
  allContacts = getAllContacts()
  return {
    "allOperators":allOperators,
    "allContacts":allContacts
    }




@app.route("/", methods=['POST', 'GET'])
def postOperator():
  if request.method == 'POST':
    operator = request.form
    if getOperatorByEqualName(operator['name']) == None:
      addOperator(operator['name'], operator['businessHour'], operator['notes'])
      operatorID = getOperatorByEqualName(operator['name'])
      addContact(operatorID[0], operator['telphone'], operator['celphone'])
      return render_template('Index.html') 
    else:
      return render_template('Index.html', alertError=True) 
     
  elif request.method == 'GET':
    return render_template('Index.html')

@app.route("/edit/<operatorID>", methods=['POST', 'GET'])
def putOperator(operatorID):
  if request.method == 'POST':
    operator = request.form
    updateOperator(operatorID, operator['nameEdit'], operator['notes'], operator['businessHour'])
    putContact(operatorID, operator['telphoneEdit'], operator['celphoneEdit'])
    if operator ['celphoneNew'] != '' or operator['telphoneNew'] != '':
      addContact(operatorID, operator['telphoneNew'], operator['celphoneNew'])
    return redirect('/')
  elif request.method == 'GET':
    operatorEdit = getOperatorByID(operatorID)
    contactEdit = getContactsByOperatorID(operatorID)
    return render_template('Index.html', operatorID=operatorID, modalOn=True, operatorEdit=operatorEdit, contactEdit=contactEdit, index=0)

@app.route("/delete/<operatorID>", methods=["POST", "GET"])
def removeOperator(operatorID):
  deleteOperator(operatorID)
  return redirect('/')

@app.route('/search', methods=["POST", "GET"])
def searchOperator():
  searchValue = request.form
  operatorSearch = getOperatorByName(searchValue['search'])
  print(operatorSearch)
  contactSearch = ''
  if searchValue != '':
    for opSearch in operatorSearch:
      if(operatorSearch != None):
        contactSearch = getContactsByOperatorID(opSearch[0])

  return render_template('Index.html', operatorSearch=operatorSearch, contactSearch=contactSearch)

if __name__=='__main__':
  app.run(debug=True, host='0.0.0.0', port=3000)
