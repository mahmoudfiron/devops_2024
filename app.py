from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)


@app.route('/status')
def status():
    # Retrieve the environment variable
    status_value = os.getenv('MY_WEB_APP_STATUS', '')
    current_time = datetime.datetime.now().isoformat()

    if not status_value:
        # Return error if variable is missing or empty
        return jsonify(
            message="Environment variable MY_WEB_APP_STATUS is missing",
            time=current_time
        ), 400

    # Return status and current time if the variable is set
    return jsonify(
        status=status_value,
        time=current_time
    )


@app.route('/')
def home():
    return jsonify(message="Flask app is running! Try /status to get environm")


if __name__ == '__main__':
    # Listen on port 8017
    app.run(host='0.0.0.0', port=8017)
