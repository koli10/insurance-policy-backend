# Insurance Policy Management System - Backend

This is the Flask backend for the Insurance Policy Management System. It provides a RESTful API to manage insurance policies, allowing users to perform CRUD (Create, Read, Update, Delete) operations.

## Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite
- **API Testing:** Postman

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/koli10/insurance-policy-backend.git
cd insurance-policy-backend
```

### 2. Create a Virtual Environment (Optional, but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
```bash
python init_db.py
```
This will create an `insurance.db` file with the required tables.

### 5. Run the Flask Server
```bash
python app.py
```
The server will start on:
**http://127.0.0.1:5000/**

## API Endpoints

| Method | Endpoint           | Description         |
|--------|-------------------|---------------------|
| GET    | `/policies`       | Get all policies   |
| POST   | `/policies`       | Add a new policy   |
| GET    | `/policies/<id>`  | Get a specific policy |
| PUT    | `/policies/<id>`  | Update a policy    |
| DELETE | `/policies/<id>`  | Delete a policy    |

## Testing with Postman
1. Open **Postman**
2. Use `http://127.0.0.1:5000/policies` to test API requests.
3. Send **GET, POST, PUT, DELETE** requests to interact with the database.

## Error Handling & Validation
- Input validation is implemented to prevent bad data.
- Proper HTTP status codes are returned for different errors.
- Try-Except blocks handle unexpected errors gracefully.

## Troubleshooting

### 1. Module Not Found Error?
```bash
pip install -r requirements.txt
```

### 2. Database Not Created?
```bash
python init_db.py
```

### 3. Port Already in Use?
```bash
kill -9 $(lsof -t -i:5000)  # Mac/Linux
```
For **Windows**, restart your PC or try another port.

## License
This project is open-source under the MIT License.

