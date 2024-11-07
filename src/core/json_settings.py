import os
import json

def load_settings():
  """Load configuration settings from settings.json."""
  settings_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
  try:
      with open(settings_path, 'r') as f:
          return json.load(f)
  except FileNotFoundError:
      raise FileNotFoundError(f"Settings file not found at {settings_path}")
  except json.JSONDecodeError:
      raise ValueError("Error parsing settings.json. Please check the JSON format.")