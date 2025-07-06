from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

neighborhoods = [
    {
        "name": "Phagwara Main Road",
        "amenities": ["food courts", "cafes", "hostels", "gym","wifi"],
        "safety": 4,
        "cost": 5000
    },
    {
        "name": "Deep Nagar",
        "amenities": ["quiet", "gym", "wifi", "vegetarian mess","food courts"],
        "safety": 4,
        "cost": 6000
    },
    {
        "name": "Green Valley",
        "amenities": ["costly", "cafes", "gym", "wifi","food courts"],
        "safety": 5,
        "cost": 10000
    },
    {
        "name": "Law Gate",
        "amenities": ["grocery", "gym", "food courts","wifi"],
        "safety": 3,
        "cost": 4000
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/match', methods=['POST'])
def match_neighborhoods():
    data = request.json
    user_amenities = [a.strip().lower() for a in data.get("amenities", [])]
    min_safety = int(data.get("min_safety_rating", 0))
    max_cost = int(data.get("max_cost_of_living", 999999))

    matched = []
    for n in neighborhoods:
        n_amenities = [a.lower() for a in n['amenities']]
        has_all = all(amenity in n_amenities for amenity in user_amenities)
        if has_all and n['safety'] >= min_safety and n['cost'] <= max_cost:
            matched.append({"name": n["name"]})

    return jsonify(matched)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
