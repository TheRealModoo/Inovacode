import json

def build_recommendation_prompt(summary: dict) -> str:
    return f"""
Tu es un analyste en sécurité routière pour une municipalité.

Ta tâche :
1. analyser les tendances observées dans les données d'une zone de collision,
2. identifier les facteurs de risque probables,
3. proposer des recommandations concrètes pour réduire les collisions.

Règles importantes :
- base-toi uniquement sur les données fournies;
- n'invente pas de causes non appuyées par les données;
- parle en termes de "facteurs associés" ou "tendances observées";
- évite les affirmations absolues;
- réponse en français;
- ton professionnel, clair, concis;
- retourne STRICTEMENT un JSON valide avec cette structure :

{{
  "risk_level": "Faible | Moyen | Élevé | Critique",
  "summary": "court paragraphe",
  "risk_factors": ["facteur 1", "facteur 2", "facteur 3"],
  "recommendations": ["recommandation 1", "recommandation 2", "recommandation 3"],
  "confidence_note": "courte note sur les limites des données"
}}

Données :
{json.dumps(summary, ensure_ascii=False, indent=2)}
""".strip()
