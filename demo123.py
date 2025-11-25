"""
sample.py
A sample Python script demonstrating:
- AI suggestions (as comments),
- recommended libraries,
- proper indentation,
- DevOps-related insecure patterns (commented out + marked as violation),
- secure best practices.
"""

# ==========================
# 📦 Recommended Libraries
# ==========================
# AI Suggestion: Consider using `requests` for API calls if needed.
# AI Suggestion: Use `python-dotenv` to manage environment variables securely.
# AI Suggestion: Use `logging` instead of print statements for production systems.

import os
import logging

# Configure logging (AI Suggestion: prefer structured logs in production)
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


# ================================================================
# 🔐 SECURITY DEMO: INSECURE PRACTICE (COMMENTED OUT — VIOLATION)
# ================================================================
# ❌ Hardcoded credentials — SECURITY VIOLATION (AI flagged)
# password = "SuperSecret123"   # <-- Do NOT do this in real systems
# API_KEY = "hardcoded_api_key_value"  # <-- Also bad practice

# AI Suggestion: Instead of hardcoding, load from environment variables.
# Example (below) shows secure method.


# ==========================
# ✅ Secure Alternative
# ==========================

def get_secure_config():
    """
    Safely retrieves configuration values from environment variables.
    AI Suggestion: Always provide defaults for local dev or fail gracefully.
    """
    config = {
        "API_KEY": os.getenv("API_KEY", None),
        "DB_HOST": os.getenv("DB_HOST", "localhost")
    }

    if config["API_KEY"] is None:
        logging.warning("API_KEY is not set. Using limited functionality mode.")

    return config


# ==========================
# 🧾 Basic Functional Example
# ==========================

def process_data(data):
    """
    Sample function to show indentation, comments, and AI suggestions.
    """
    # AI Suggestion: validate input before processing
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")

    logging.info("Processing data...")
    return [item * 2 for item in data]


# ==========================
# 🚀 Main Execution
# ==========================

def main():
    logging.info("Starting sample.py...")

    config = get_secure_config()
    logging.info(f"Loaded config: {config}")

    try:
        result = process_data([1, 2, 3])
        logging.info(f"Processed Result: {result}")
    except Exception as e:
        logging.error(f"Error while processing: {e}")


if __name__ == "__main__":
    main()
