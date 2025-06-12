from flask import Flask, render_template, request, Response, stream_with_context
import openai
import os

app = Flask(__name__)

# Sample configuration - replace with your Azure OpenAI details
openai.api_type = "azure"
openai.api_key = os.environ.get("AZURE_OPENAI_KEY", "YOUR_AZURE_OPENAI_KEY")
openai.api_base = os.environ.get("AZURE_OPENAI_ENDPOINT", "https://your-endpoint.openai.azure.com/")
openai.api_version = "2024-05-01-preview"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("name", "")
    prompt = f"{name} という名前で、2000字程度の架空の自己紹介を日本語で書いてください。"

    def stream():
        response = openai.ChatCompletion.create(
            engine="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            temperature=0.7,
            stream=True,
        )
        for chunk in response:
            if "choices" in chunk and len(chunk["choices"]) > 0:
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    yield delta["content"]

    return Response(stream_with_context(stream()), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
