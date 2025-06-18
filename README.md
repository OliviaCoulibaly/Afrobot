🧠 AfroBot – Chatbot de Commande de Vêtements
AfroBot est un projet de chatbot intelligent permettant aux utilisateurs de commander des vêtements par simple conversation. Le projet utilise FastAPI en backend et Streamlit en frontend.

📁 Structure du projet
bash
Copier
Modifier
AFROB...
├── backend
│   ├── __init__.py
│   ├── chatbot.py           # Logique principale du chatbot
│   ├── main.py              # Point d'entrée FastAPI
│   ├── prompt.py            # Prompts personnalisés
│   ├── schemas.py           # Modèles Pydantic
│   └── requirements.txt     # Dépendances backend
├── frontend
│   ├── app.py               # Interface utilisateur Streamlit
│   └── requirements.txt     # Dépendances frontend
├── openai/                  # (Optionnel) Intégrations OpenAI
├── .gitignore
🚀 Lancer le projet
1. Backend (FastAPI)
bash
Copier
Modifier
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
L'API sera disponible sur : http://127.0.0.1:8000

2. Frontend (Streamlit)
bash
Copier
Modifier
cd frontend
pip install -r requirements.txt
streamlit run app.py
L'interface utilisateur sera lancée automatiquement dans votre navigateur.

📦 Fonctions principales
🎯 Compréhension du langage naturel via OpenAI

👚 Commande de vêtements (taille, couleur, catégorie, quantité, etc.)

🧾 Validation de commande

🧠 Historique de conversation

🌐 Interface simple et intuitive

📄 Exemples de messages
arduino
Copier
Modifier
"Je veux une chemise bleue taille L"
"Commande-moi 2 pantalons noirs en M"
"Ajoute une jupe rouge et des chaussures noires"
🔧 Technologies utilisées
Python 3.10+

FastAPI

Streamlit

Pydantic

OpenAI API

📬 Contact
Pour toute suggestion ou bug, merci de me contacter.

