#!/bin/bash

# Set variables
POLICY_ID="change_freeze"
OPA_URL="http://127.0.0.1:8181/v1/policies/${POLICY_ID}"

# Read file content into a variable
POLICY_DATA=$(cat /opt/netbox/opa/change_freeze.rego)

echo "$POLICY_DATA"

# Send the policy to OPA via POST request
curl -X PUT "$OPA_URL" \
     -H "Content-Type: text/plain" \
     --data-binary "$POLICY_DATA"
