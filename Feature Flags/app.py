from flask import Flask, render_template
from flagsmith import Flagsmith

app = Flask(__name__, template_folder='templates')

# Initialize Flagsmith client with environment key
flagsmith = Flagsmith(environment_key="Zdiebgp5mgJvQ7et4pNiDR")

@app.route('/')
def index():
    # The method below triggers a network request to fetch environment flags
    flags = flagsmith.get_environment_flags()

    # Check if the feature flag "button-toggle" is enabled
    button_enabled = flags.is_feature_enabled("button_toggle")

    return render_template('index.html', button_enabled=button_enabled)

if __name__ == '__main__':
    app.run(debug=True)

