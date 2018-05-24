from flask import Flask
from flask import jsonify
import glob
import json
filelist = (glob.glob('C:\\Users\\p.mykhailyk\\Seafile\\p4ne_training\\config_files\\*.txt'))
Total_list = []
hostname = ''
for ff in filelist:
    fw = open(ff)
    lines = list(fw)
    fw.close()
    for string in lines:
        pos = string.find('hostname')
        if pos == 0:
            small_1 = string[int(pos):]
            small_2 = small_1.replace('hostname', '')
            small_3 = small_2.strip()
            Total_list = Total_list + [small_3]
#print(Total_list)
#print(pos)
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return('Hello, enter parameters:configs, config/hostname')
@app.route('/configs')
def configs():
    return(jsonify(Total_list))
@app.route('/config/<hostname>')
def config(hostname):
    return("IP")


if __name__ == '__main__':
    app.run(debug=True)