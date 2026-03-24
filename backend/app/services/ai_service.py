import json
import requests
from app.services.prompt_builder import build_recommendation_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def generate_location_recommendation(summary: dict) -> dict:
    prompt = build_recommendation_prompt(summary)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    raw_text = data.get("response", "").strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {
            "risk_level": "Inconnu",
            "summary": raw_text,
            "risk_factors": [],
            "recommendations": [],
            "confidence_note": "La réponse du modèle n'était pas un JSON parfaitement valide."
        }