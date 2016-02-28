from flask import Flask,jsonify,request,abort,make_response
import flask
import json

app = Flask(__name__)

int_paginationVal = 1
listStates = []
int_lenStates = None

def _loadStates():
    global listStates,int_lenStates
    with open('states.json','r') as data_file:    
        data = json.load(data_file)
        listStates = data['states']
        int_lenStates = len(listStates)
        #print(str(data)+str(int_lenStates))

@app.route('/')
def index():
    return "Hello, World!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'errorCode': 'Not found'}), 404)

@app.route('/states/api/v1.0/getstates')
def getAllStates():
    resp = jsonify( {"states": listStates} )
    return resp

@app.route('/states/api/v1.0/getstates/<int:beg>',methods=['GET'])
def getSomeStates(beg):
    if( beg not in range(int_lenStates)):
        abort(404)
    intSize = None
    try:
        intSize = int(request.args.get('size'))
    except Exception as e:
        print('Invalid size argument')
    if intSize:
        #To return next value header 
        int_nextVal = beg+intSize
    else:
        #Use default pagination value if not specified by the user
        int_nextVal = beg+int_paginationVal
    resp = jsonify( {"states": listStates[beg:][:(int_nextVal-beg)]} )
    if int_nextVal >= len(listStates):
        resp.headers['Next-Val'] = -1
    else:
        resp.headers['Next-Val'] = int_nextVal
    return resp

if __name__ == '__main__':
    _loadStates()
    app.run(debug=True)