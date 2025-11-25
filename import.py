################################################################################
# TEST CASE 1 — Missing import (should NOT be flagged, normal application code)
################################################################################

import json

def get_user_home():
    path = os.path.expanduser("~")   # os is NOT imported (agent must ignore)
    return path


################################################################################
# TEST CASE 2 — Indentation inconsistency (agent must IGNORE indentation issues)
################################################################################

def handler():
    if True:
       print("Hello")    # 7 spaces vs 4, shouldn't matter
    return True


################################################################################
# TEST CASE 3 — Hardcoded IP (agent MUST flag this as DevOps-impact risk)
################################################################################

DEBUG = True
API_URL = "http://10.1.2.3:9000"   # Hardcoded environment-specific IP address


################################################################################
# TEST CASE 4 — DevOps-style config embedded in code (agent MUST flag)
################################################################################

DOCKER_CONFIG = """
FROM ubuntu latest   # invalid syntax: missing colon
"""

K8S_DEPLOYMENT = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-app
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: app
          image: myapp:latest
          ports
            - containerPort: 80   # YAML indentation + syntax error (should be flagged)
"""


################################################################################
# TEST CASE 5 — Fake CI/CD config in a Python string (agent MUST detect DevOps file)
################################################################################

GITHUB_ACTIONS_WORKFLOW = """
name: Build Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Run script
        run: python build.py --env=production
"""
