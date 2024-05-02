# fetch_feature_flag_status.py

from flagsmith import Flagsmith

def fetch_feature_flag_status():
    # Initialize Flagsmith client with environment key
    flagsmith = Flagsmith(environment_key="Zdiebgp5mgJvQ7et4pNiDR")

    # Fetch environment flags
    flags = flagsmith.get_environment_flags()

    # Check if the feature flag "button_toggle" is enabled
    button_enabled = flags.is_feature_enabled("button_toggle")

    # Print the status to console
    print("Feature flag 'button_toggle' status:", button_enabled)

if __name__ == "__main__":
    fetch_feature_flag_status()
