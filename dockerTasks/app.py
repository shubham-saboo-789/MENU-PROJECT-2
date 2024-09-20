from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def run_docker_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docker', methods=['POST'])
def docker_command():
    command = request.json.get('command')
    output = run_docker_command(command)
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
