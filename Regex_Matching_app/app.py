from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'DR-1329'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']

        try:
            # Validate regex pattern
            re.compile(regex_pattern)
        except re.error:
            flash('Invalid regex pattern. Please enter a valid regex.', 'error')
            return redirect(url_for('home'))

        # Perform regex matching
        matched_strings = re.findall(regex_pattern, test_string)

        # Dummy email validation result (replace this with your actual validation logic)
        email_validation = 'Valid' if re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', test_string) else 'Invalid'

        return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matched_strings, email_validation=email_validation)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']

        # Simple email validation regex
        email_regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

        if re.match(email_regex, email):
            flash('Valid email address!', 'success')
        else:
            flash('Invalid email address. Please enter a valid email.', 'error')

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
