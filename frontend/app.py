import streamlit as st
import requests
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="AfroLiva - Assistant Mode 🖤")

# Titre de la page
st.title("🖤 Bienvenue chez AfroLiva")

# Initialiser les discussions
if "conversations" not in st.session_state:
    st.session_state.conversations = {"active": [], "history": []}

# Sélection ou démarrage d'une nouvelle discussion
st.sidebar.title("📂 Discussions")
if st.sidebar.button("➕ Nouvelle discussion"):
    if st.session_state.conversations["active"]:
        # Sauvegarder la discussion active dans l'historique
        st.session_state.conversations["history"].append(st.session_state.conversations["active"])
    # Réinitialiser la discussion active
    st.session_state.conversations["active"] = []

# Afficher l'historique des discussions
if st.session_state.conversations["history"]:
    selected_discussion = st.sidebar.selectbox(
        "📜 Historique des discussions",
        options=range(len(st.session_state.conversations["history"])),
        format_func=lambda i: f"Discussion {i + 1}",
    )
    if st.sidebar.button("🔄 Charger cette discussion"):
        # Charger une discussion précédente
        st.session_state.conversations["active"] = st.session_state.conversations["history"][selected_discussion]

# Affichage de l'historique de la discussion active
for msg in st.session_state.conversations["active"]:
    with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🛍️"):
        st.markdown(msg["content"])

# Saisie utilisateur
if prompt := st.chat_input("Parlez-moi de votre commande (ex : Je veux une robe wax taille M)"):
    st.session_state.conversations["active"].append({"role": "user", "content": prompt})

    # Affichage immédiat du message utilisateur
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Appel backend
    try:
        response = requests.post(
            "http://localhost:8000/chat/",
            json=[{"role": m["role"], "content": m["content"]} for m in st.session_state.conversations["active"]]
        )

        if response.status_code == 200:
            data = response.json()

            assistant_msg = data["response"]
            st.session_state.conversations["active"].append({"role": "assistant", "content": assistant_msg})

            with st.chat_message("assistant", avatar="🛍️"):  
                st.markdown(assistant_msg)

            if data.get("order"):
                st.success("🎉 Commande validée avec succès ! Voici votre résumé :")
                st.json(data["order"])

                if st.button("✅ Confirmer le paiement"):
                    st.balloons()
                    st.success(f"💳 Paiement accepté le {datetime.now().strftime('%d/%m/%Y %H:%M')}")

        else:
            st.error(f"Erreur serveur : {response.status_code}")
            st.text(response.text)

    except Exception as e:
        st.error(f"Connexion au backend échouée : {e}")