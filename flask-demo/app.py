from flask import Flask, render_template, request

import model

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Flask!</h1>"

@app.route("/greet/<username>")
def greet(username):
    return render_template(
        "greet.html",
        username=username,
    )

@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int):
    return str(x + y)

# GET /api/v1/get_emp_info/<str:bu_id>/<str:dep_id>
@app.route("/api/v1/get_emp_info/<string:bu_id>/<string:dep_id>")
def get_emp_info(bu_id, dep_id):
    sql = f"""
        select
            emp_name,
            bu_id,
            dep_id,
            emp_id,
            emp_email
        from emp
        where bu_id = '{bu_id}' and dep_id = '{dep_id}'
    """
    # result = execute_sql(sql)
    result = [
        {
            "emp_name": "Alice Smith",
            "bu_id": bu_id,  # Matches your variable
            "dep_id": dep_id,  # Matches your variable
            "emp_id": "EMP001",
            "emp_email": "alice.smith@company.com",
        },
        {
            "emp_name": "Bob Jones",
            "bu_id": bu_id,
            "dep_id": dep_id,
            "emp_id": "EMP002",
            "emp_email": "bob.jones@company.com",
        },
        {
            "emp_name": "Carlos Mendez",
            "bu_id": bu_id,
            "dep_id": dep_id,
            "emp_id": "EMP003",
            "emp_email": "carlos.mendez@company.com",
        },
        {
            "emp_name": "Diana Prince",
            "bu_id": bu_id,
            "dep_id": dep_id,
            "emp_id": "EMP004",
            "emp_email": "diana.prince@company.com",
        },
        {
            "emp_name": "Evan Wright",
            "bu_id": bu_id,
            "dep_id": dep_id,
            "emp_id": "EMP005",
            "emp_email": "evan.wright@company.com",
        },
    ]
    return result

# /hello_param?username=Allen&age=22
@app.route("/hello_param")
def hello_param():
    username = request.args.get("username")
    age = request.args.get("age")
    if not username:
        return "What is your name?"
    if not age:
        return f"Hello {username}. How old are you?"
    return f"Hello {username}, you are {age} years old."

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'POST':
        return outStr%('Hello %s'%(request.form.get('username')))
    return outStr%("")

@app.route('/hello_post2', methods=['GET', 'POST'])
def hello_post2():
    request_method = request.method
    username = request.form.get("username")
    return render_template(
        "hello_post.html",
        request_method=request_method,
        username=username,
    )

@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001,
    )
