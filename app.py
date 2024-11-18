from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Example in-memory database (you can replace this with a real database later)
certifications = {
    "12345": {
        "name": "John Doe",
        "status": "Active",
        "issue_date": "2023-01-01",
        "expiry_date": "2025-01-01"
    },
    "67890": {
        "name": "Jane Smith",
        "status": "Expired",
        "issue_date": "2020-01-01",
        "expiry_date": "2023-01-01"
    }
}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to handle certification verification
@app.route('/verify', methods=['GET'])
def verify():
    cert_id = request.args.get('certID')  # Get certification ID from query parameters
    if cert_id in certifications:
        cert = certifications[cert_id]
        return jsonify({
            "success": True,
            "data": {
                "name": cert["name"],
                "status": cert["status"],
                "issue_date": cert["issue_date"],
                "expiry_date": cert["expiry_date"]
            }
        })
    return jsonify({"success": False, "message": "Certification not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)