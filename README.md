

---

```markdown
# Matrix Multiplier API

This is a simple Flask API that multiplies two matrices. You send a POST request with two matrices `A` and `B`, and the API responds with the resulting matrix `A × B`.

---

## 📦 Project Structure

```

matrix-multiplier/
│
├── main.py               # Flask app with matrix multiplication logic
├── requirements.txt      # Required Python packages
└── README.md             # Project documentation

````

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/matrix-multiplier.git
cd matrix-multiplier
````

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python main.py
```

You should see output like:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

## 📡 API Usage

### Endpoint

```
POST /multiply
```

### Request Header

```
Content-Type: application/json
```

### JSON Payload

```json
{
  "A": [[1, 2], [3, 4]],
  "B": [[5, 6], [7, 8]]
}
```

### Sample CURL Command

```bash
curl -X POST http://127.0.0.1:5000/multiply \
     -H "Content-Type: application/json" \
     -d '{"A": [[1, 2], [3, 4]], "B": [[5, 6], [7, 8]]}'
```

### Response

```json
{
  "result": [[19, 22], [43, 50]]
}
```

---

## 🧮 Matrix Multiplication Rule

To multiply matrices A (of shape *m×n*) and B (of shape *n×p*), the number of columns in A must equal the number of rows in B. The resulting matrix will have shape *m×p*.

---

## ⚠️ Error Handling

* If either matrix is missing:

  ```json
  {"error": "Both matrices A and B are required."}
  ```

* If matrix dimensions are incompatible:

  ```json
  {"error": "Incompatible matrix dimensions for multiplication."}
  ```

---

## 📄 License

MIT License

```

---

```
