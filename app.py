from flask import Flask, render_template,send_from_directory
import random

app = Flask(__name__)

paths = [
    "/hidden-dashboard",
    "/confidential-settings",
    "/private-files",
    "/restricted-access",
    "/top-secret-folder",
    "/no-entry-here",
    "/classified-documents",
    "/sensitive-info",
    "/secure-zone",
    "/do-not-open"
]
flag_path = random.choice(paths)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder or 'static', 'robots.txt')

@app.route(flag_path)
def flag():
    # Assuming the flag is stored in a template called 'flag.html'
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)