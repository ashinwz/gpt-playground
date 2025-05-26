#!/usr/bin/env bash
set -e
python3 -m venv venv
. venv/bin/activate
pip install -r backend/requirements.txt
printf '\nVirtual environment created. Activate it with "source venv/bin/activate".\n'
