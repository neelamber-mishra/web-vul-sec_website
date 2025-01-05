from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crawl', methods=['GET', 'POST'])
def crawl_directories():
    if request.method == 'POST':
        url = request.form.get('url')
        result = subprocess.run(
            ['python', 'scripts/crawl_script.py', url], capture_output=True, text=True
        )
        
        # Split the result into summary and links
        output_lines = result.stdout.strip().split("\n")
        summary = output_lines[0] if output_lines else "No summary available."
        links = output_lines[1:] if len(output_lines) > 1 else []

        return render_template('crawl_output.html', summary=summary, links=links)
    return render_template('crawl.html')


@app.route('/brute_force', methods=['GET', 'POST'])
def brute_force():
    if request.method == 'POST':
        url = request.form.get('url')
        username = request.form.get('username')
        password_file = request.files['password_file']

        if password_file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], password_file.filename)
            password_file.save(file_path)

            # Call the brute force script
            result = subprocess.run(
                ['python', 'scripts/bruteforce_script.py', url, username, file_path],
                capture_output=True,
                text=True
            )

            # Clean up the uploaded file
            os.remove(file_path)

            summary = result.stdout.strip() if result.stdout else "No output received."

            return render_template('brute_force_output.html', summary=summary)

    return render_template('brute_force.html')


@app.route('/sql_injection', methods=['GET', 'POST'])
def sql_injection():
    if request.method == 'POST':
        url = request.form.get('url')
        result = subprocess.run(
            ['python', 'scripts/sql_injection_script.py', url], capture_output=True, text=True
        )

        summary = result.stdout.strip() if result.stdout else "No output received."

        return render_template('sql_injection_output.html', summary=summary)

    return render_template('sql_injection.html')


@app.route('/xss_attack', methods=['GET', 'POST'])
def xss_attack():
    if request.method == 'POST':
        url = request.form.get('url')
        payload = request.form.get('payload')

        result = subprocess.run(
            ['python', 'scripts/xss_attack_script.py', url, payload],
            capture_output=True,
            text=True
        )

        summary = result.stdout.strip() if result.stdout else "No output received."

        return render_template('xss_attack_output.html', summary=summary)

    return render_template('xss_attack.html')


if __name__ == '__main__':
    app.run(debug=True)
