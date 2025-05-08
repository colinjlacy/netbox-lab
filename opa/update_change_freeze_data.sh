#!/bin/bash

OPA_URL="http://localhost:8181/v1/data/locks"
LOCKS_FILE="/opt/netbox/opa/freeze.json"

# Check if file exists
if [ ! -f "$LOCKS_FILE" ]; then
  echo "Error: $LOCKS_FILE not found!"
  exit 1
fi

# Upload lock data to OPA
curl -X PUT "$OPA_URL" \
     -H "Content-Type: application/json" \
     --data-binary "@$LOCKS_FILE"
