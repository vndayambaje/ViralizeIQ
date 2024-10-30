#!/bin/bash

# Set project root directory name
PROJECT_NAME="ViralizaIQ"

# Create the main project directory
mkdir -p "$PROJECT_NAME"

# Create subdirectories for app and its components
mkdir -p "$PROJECT_NAME/app"
mkdir -p "$PROJECT_NAME/app/static/css"
mkdir -p "$PROJECT_NAME/app/static/js"
mkdir -p "$PROJECT_NAME/app/templates"

# Create models directory
mkdir -p "$PROJECT_NAME/models"

# Create data directory with subdirectories
mkdir -p "$PROJECT_NAME/data/raw"
mkdir -p "$PROJECT_NAME/data/processed"

# Create utils directory
mkdir -p "$PROJECT_NAME/utils"

# Create scripts directory
mkdir -p "$PROJECT_NAME/scripts"

# Create main project files
touch "$PROJECT_NAME/app/__init__.py"
touch "$PROJECT_NAME/app/main.py"
touch "$PROJECT_NAME/app/config.py"
touch "$PROJECT_NAME/app/templates/dashboard.html"

# Create model files
touch "$PROJECT_NAME/models/sentiment_analysis.py"
touch "$PROJECT_NAME/models/engagement_predictor.py"
touch "$PROJECT_NAME/models/trend_analysis.py"

# Create data directory sample file
touch "$PROJECT_NAME/data/sample_data.csv"

# Create utility files
touch "$PROJECT_NAME/utils/data_preprocessing.py"
touch "$PROJECT_NAME/utils/api_client.py"
touch "$PROJECT_NAME/utils/a_b_testing.py"
touch "$PROJECT_NAME/utils/visualization.py"

# Create deployment scripts
touch "$PROJECT_NAME/scripts/deploy_aws.sh"
touch "$PROJECT_NAME/scripts/db_setup.sql"
touch "$PROJECT_NAME/scripts/setup_env.sh"

# Create main project files
touch "$PROJECT_NAME/Dockerfile"
touch "$PROJECT_NAME/requirements.txt"
touch "$PROJECT_NAME/README.md"

echo "Directory structure for $PROJECT_NAME has been created successfully!"
