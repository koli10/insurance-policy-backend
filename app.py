from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database & Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Insurance Policy Model
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(100), unique=True, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    policy_type = db.Column(db.String(100), nullable=False)
    premium_amount = db.Column(db.Float, nullable=False)

# Marshmallow Schema
class PolicySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Policy

policy_schema = PolicySchema()
policies_schema = PolicySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API Routes (CRUD Operations)

# Get all policies
@app.route('/policies', methods=['GET'])
def get_policies():
    all_policies = Policy.query.all()
    return jsonify(policies_schema.dump(all_policies))

# Get a single policy by ID
@app.route('/policies/<int:id>', methods=['GET'])
def get_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404
    return policy_schema.jsonify(policy)

# Add a new policy
@app.route('/policies', methods=['POST'])
def add_policy():
    data = request.json
    if not data.get('policy_number') or not data.get('customer_name'):
        return jsonify({"error": "Missing required fields"}), 400

    new_policy = Policy(
        policy_number=data['policy_number'],
        customer_name=data['customer_name'],
        policy_type=data['policy_type'],
        premium_amount=data['premium_amount']
    )

    db.session.add(new_policy)
    db.session.commit()
    return policy_schema.jsonify(new_policy)

# Update a policy
@app.route('/policies/<int:id>', methods=['PUT'])
def update_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404

    data = request.json
    policy.policy_number = data.get('policy_number', policy.policy_number)
    policy.customer_name = data.get('customer_name', policy.customer_name)
    policy.policy_type = data.get('policy_type', policy.policy_type)
    policy.premium_amount = data.get('premium_amount', policy.premium_amount)

    db.session.commit()
    return policy_schema.jsonify(policy)

# Delete a policy
@app.route('/policies/<int:id>', methods=['DELETE'])
def delete_policy(id):
    policy = Policy.query.get(id)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404

    db.session.delete(policy)
    db.session.commit()
    return jsonify({"message": "Policy deleted successfully"}), 200

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
