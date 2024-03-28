from flask import Flask, request

app = Flask(__name__)

@app.route('/store', methods=['POST'])
def store_location():
    data = request.form
    lat = data.get('lat')
    long = data.get('long')
    if lat and long:
        with open('locations.txt', 'a') as f:
            f.write(f'Latitude: {lat}, Longitude: {long}\n')
        return 'Location stored successfully'
    return 'Invalid data', 400

if __name__ == '__main__':
    app.run(debug=True)
