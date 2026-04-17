# AI Troubleshooting Assistant

## Overview
This is a simple Python application that uses AI to:
- Analyse a technical equipment issue
- Suggest possible causes
- Recommend troubleshooting checks

## How it works
The user enters a description of a technical problem, and the AI returns:
- Possible causes
- Recommended checks

## Example

**Input:**
Forklift losing power when lifting

**Output:**
Possible Causes:
1. Hydraulic fluid level is low or contaminated.
2. Hydraulic pump or motor is malfunctioning.

Recommended Checks:
1. Inspect hydraulic fluid level and quality.
2. Check for hydraulic leaks.

## How to run

1. Navigate to the project folder:
```bash
cd ai_troubleshooting_assistant
```
2. Activate virtual environment:
```bash
source ../venv/bin/activate
```
3. Set your API key:
```bash
export OPENAI_API_KEY="your_api_key"
```
4. Run the application:
```bash
python3 app.py
```

## Requirements

See `requirements.txt`

## Notes

This is a learning project demonstrating basic AI integration using Python and OpenAI.

