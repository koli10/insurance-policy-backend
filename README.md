# insurance-policy-backend
🏦 Insurance Policy Management System - Backend
This is the Flask backend for the Insurance Policy Management System. It provides a RESTful API to manage insurance policies, allowing users to create, read, update, and delete (CRUD) insurance policies.

🚀 Tech Stack
Backend: Flask (Python)

Database: SQLite

API Testing: Postman

⚙️ Setup Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-github-username>/insurance-policy-backend.git
cd insurance-policy-backend
2️⃣ Create a Virtual Environment (Optional, but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Initialize the Database
bash
Copy
Edit
python init_db.py
This will create an insurance.db file with the required tables.

5️⃣ Run the Flask Server
bash
Copy
Edit
python app.py
The server will start on:
📍 http://127.0.0.1:5000/

🔥 API Endpoints
Method	Endpoint	Description
GET	/policies	Get all policies
POST	/policies	Add a new policy
GET	/policies/<id>	Get a specific policy
PUT	/policies/<id>	Update a policy
DELETE	/policies/<id>	Delete a policy
🔎 Testing with Postman
1️⃣ Open Postman
2️⃣ Use http://127.0.0.1:5000/policies to test API requests.
3️⃣ Send GET, POST, PUT, DELETE requests to interact with the database.

⚠️ Error Handling & Validation
Input validation is implemented to prevent bad data.

Proper HTTP status codes are returned for different errors.

Try-Except blocks handle unexpected errors gracefully.

🛠 Troubleshooting
1️⃣ Module Not Found Error?

Run pip install -r requirements.txt
2️⃣ Database Not Created?

Run python init_db.py
3️⃣ Port Already in Use?

Run kill -9 $(lsof -t -i:5000) on Mac/Linux

Restart your PC (Windows)

📜 License
This project is open-source under the MIT License.

