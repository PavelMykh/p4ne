import requests, pprint, json
from flask import Flask, render_template
from flask import jsonify

#comma = ['/api/v1/host', '/api/v1/network-device', '/api/v1/topology/physical-topology']

controller = "devnetapi.cisco.com/sandbox/apic_em"
urlBase = "https://" + controller

print(urlBase)
def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers = header, verify = False)
    return response.json()['response']['serviceTicket']





app = Flask(__name__)
@app.route('/')

@app.route('/index')
def index():
    return render_template('topology.html')

@app.route('/api/topology')
def data():
    respP = requests.get(urlBase + "/api/v1/topology/physical-topology", headers=header1, verify=False)
    print(respP.url)
    print(respP.text)
    return(jsonify(respP.json()['response']))

if __name__ == '__main__':
    ticket = new_ticket()
    header1 = {"content-type": "application/json","X-Auth-Token": ticket}
    app.run(debug=True, use_reloader=False)


#for z in comma:
#    urlP = "https://" + controller + str(z)
 #   respP = requests.get(urlP, headers=header, verify=False)
#    pprint.pprint(json.dumps(respP.json()))
#    print(urlP)
#print(json.dumps(responce1.json()))
#pprint.pprint(json.dumps(responce1.json()))
#print(urlP)