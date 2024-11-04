from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    firewall_rules = [{'ip': '192.168.1.100', 'status': 'Allowed'},
                {'ip': '192.168.1.101', 'status': 'Blocked'}]
    
    anomalies = [{'details': 'Port scanning detected from IP 192.168.1.105'}]
    
    return jsonify({'firewall_rules': firewall_rules, 'anomalies': anomalies})

if __name__ == '__main__':
    app.run(debug=True)
