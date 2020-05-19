#!/bin/bash

find . -type d -name __pycache__  -not -path "./venv/*" -exec rm -rf {} \;

find . -type d -name .mypy_cache  -not -path "./venv/*" -exec rm -rf {} \;

find . -type d -name .pytest_cache  -not -path "./venv/*" -exec rm -rf {} \;
