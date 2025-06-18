from typing import Dict, List
import openai
from dotenv import load_dotenv
import os
from prompt import get_system_prompt  # ✅ Ton prompt système
from schemas import Message

# Charger les variables d'environnement (clé API)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_chat(messages: List[Dict]) -> Dict:
    """
    Traite les messages utilisateurs et appelle l'API OpenAI pour générer une réponse.
    Si la réponse contient une commande en JSON, elle est extraite et retournée séparément.
    """
    # Construire la liste des messages avec le prompt système
    chat_messages = [{"role": "system", "content": get_system_prompt()}] + messages

    # Appel à l’API OpenAI
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_messages,
            temperature=0.7
        )
    except Exception as e:
        return {"type": "error", "content": f"Erreur OpenAI : {str(e)}"}

    # Récupérer la réponse texte du modèle
    content = response.choices[0].message.content.strip()

    # ✅ Si la réponse contient une commande JSON
    if "COMMANDE_JSON:" in content:
        try:
            json_part = content.split("COMMANDE_JSON:")[1].strip()
            return {
                "type": "order",
                "content": json_part  # Ce sera parsé en JSON dans la route FastAPI
            }
        except Exception as e:
            return {
                "type": "message",
                "content": f"Erreur de parsing JSON : {str(e)}\nContenu : {content}"
            }

    # ✅ Sinon, simple message texte
    return {"type": "message", "content": content}
