from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Cole Rapczynski! I am adding my first coding change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        major = request.form.get('major')

        return render_template(
            'contact.html',
            submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            major=major
        )

    return render_template('contact.html', submitted=False)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
