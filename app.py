from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Matrix Multiplication</h2>
        <form action="/multiply" method="post">
            Enter Matrix A (comma-separated rows, e.g., "1 2,3 4"): <br/>
            <textarea name="matrix_a" rows="3" cols="30"></textarea><br/><br/>
            Enter Matrix B (comma-separated rows, e.g., "5 6,7 8"): <br/>
            <textarea name="matrix_b" rows="3" cols="30"></textarea><br/><br/>
            <input type="submit" value="Multiply">
        </form>
    '''

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        # Get matrix strings from form
        matrix_a_str = request.form['matrix_a']
        matrix_b_str = request.form['matrix_b']

        # Convert string input to 2D integer lists
        A = [list(map(int, row.strip().split())) for row in matrix_a_str.strip().split(',')]
        B = [list(map(int, row.strip().split())) for row in matrix_b_str.strip().split(',')]

        # Check if dimensions match for multiplication
        if len(A[0]) != len(B):
            return "<p style='color:red;'>Matrix dimensions do not match for multiplication.</p>"

        # Perform matrix multiplication
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

        # Convert result to HTML table
        result_html = "<table border='1' cellpadding='5'>"
        for row in result:
            result_html += "<tr>" + "".join(f"<td>{num}</td>" for num in row) + "</tr>"
        result_html += "</table>"

        return f"<h3>Result:</h3>{result_html}<br/><a href='/'>Try Again</a>"

    except Exception as e:
        return f"<p style='color:red;'>Error: {str(e)}<br/>Please enter valid matrix input.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
