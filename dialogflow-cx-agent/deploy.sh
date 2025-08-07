#!/bin/bash

# Dialogflow CX Agent Deployment Script

# Check if required tools are installed
echo "Checking for required tools..."
if ! command -v gcloud &> /dev/null; then
    echo "gcloud CLI is not installed. Please install it first."
    exit 1
fi

echo "Required tools are installed."

# Set variables (update these with your actual values)
PROJECT_ID="your-project-id"
LOCATION_ID="your-location-id"  # e.g., us-central1
AGENT_ID="your-agent-id"

# Create a temporary directory for processed files
mkdir -p /root/dialogflow-cx-agent/temp

echo "Processing configuration files..."

# Process all JSON files to replace placeholders
for file in /root/dialogflow-cx-agent/intents/*.json; do
    sed -e "s/PROJECT_ID/$PROJECT_ID/g" \
        -e "s/LOCATION_ID/$LOCATION_ID/g" \
        -e "s/AGENT_ID/$AGENT_ID/g" \
        "$file" > "/root/dialogflow-cx-agent/temp/$(basename "$file")"
done

for file in /root/dialogflow-cx-agent/entities/*.json; do
    sed -e "s/PROJECT_ID/$PROJECT_ID/g" \
        -e "s/LOCATION_ID/$LOCATION_ID/g" \
        -e "s/AGENT_ID/$AGENT_ID/g" \
        "$file" > "/root/dialogflow-cx-agent/temp/$(basename "$file")"
done

for file in /root/dialogflow-cx-agent/webhooks/*.json; do
    sed -e "s/PROJECT_ID/$PROJECT_ID/g" \
        -e "s/LOCATION_ID/$LOCATION_ID/g" \
        -e "s/AGENT_ID/$AGENT_ID/g" \
        "$file" > "/root/dialogflow-cx-agent/temp/$(basename "$file")"
done

for file in /root/dialogflow-cx-agent/flows/*.json; do
    sed -e "s/PROJECT_ID/$PROJECT_ID/g" \
        -e "s/LOCATION_ID/$LOCATION_ID/g" \
        -e "s/AGENT_ID/$AGENT_ID/g" \
        "$file" > "/root/dialogflow-cx-agent/temp/$(basename "$file")"
done

echo "Configuration files processed."

echo "Deployment instructions:"
echo "1. Create a new Dialogflow CX agent in the Google Cloud Console"
echo "2. Use the Dialogflow CX API or Console to import the processed configuration files from /root/dialogflow-cx-agent/temp/"
echo "3. Update the webhook URIs with your actual API endpoints"
echo "4. Set the API key in the webhook headers"

echo "Deployment script completed. Please review the processed files in /root/dialogflow-cx-agent/temp/ before importing."
