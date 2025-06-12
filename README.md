# Self Intro Web App

This Flask app generates a fictional self-introduction using Azure OpenAI's GPT-4o model.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables for Azure OpenAI:
   - `AZURE_OPENAI_KEY`: Your API key
   - `AZURE_OPENAI_ENDPOINT`: Base endpoint URL (e.g., `https://your-resource.openai.azure.com/`)

3. Run the app:
   ```bash
   python app.py
   ```

Then open `http://localhost:5000` in your browser.
