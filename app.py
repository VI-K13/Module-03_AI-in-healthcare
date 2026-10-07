
import streamlit as st
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


# Create a small symptom knowledge base.
# Each category contains keywords, a care level, and an explanation.

symptom_database = {
    "General Headache Symptoms": {
        "keywords": [
            "headache",
            "mild headache"
        ],
        "care_level": "Self-Care",
        "explanation": (
            "A mild headache can often be monitored with rest, hydration, "
            "and other basic self-care unless it becomes severe or unusual."
        )
    },

    "Common Cold": {
        "keywords": [
            "cough",
            "runny nose",
            "stuffy nose",
            "sneezing",
            "sore throat"
        ],
        "care_level": "Self-Care",
        "explanation": (
            "These symptoms are commonly associated with mild respiratory "
            "conditions that can often be monitored at home."
        )
    },

    "Flu-Like Symptoms": {
        "keywords": [
            "fever",
            "chills",
            "body aches",
            "fatigue"
        ],
        "care_level": "Doctor Visit",
        "explanation": (
            "Fever combined with body aches, fatigue, or chills may require "
            "medical evaluation, especially if symptoms become severe."
        )
    },

    "Possible Infection": {
        "keywords": [
            "high fever",
            "swelling",
            "pus",
            "infection",
            "severe sore throat"
        ],
        "care_level": "Doctor Visit",
        "explanation": (
            "These symptoms may indicate an infection that could require "
            "evaluation and treatment by a healthcare professional."
        )
    },

    "Severe Abdominal Symptoms": {
        "keywords": [
            "severe stomach pain",
            "severe abdominal pain",
            "persistent vomiting",
            "blood in stool"
        ],
        "care_level": "Urgent",
        "explanation": (
            "Severe abdominal symptoms may require prompt medical attention "
            "to determine their cause."
        )
    },

    "Breathing or Chest Emergency": {
        "keywords": [
            "chest pain",
            "difficulty breathing",
            "shortness of breath",
            "cannot breathe",
            "blue lips"
        ],
        "care_level": "Emergency",
        "explanation": (
            "Chest pain or serious breathing problems can be signs of a "
            "medical emergency and should receive immediate attention."
        )
    },

    "Neurological Emergency": {
        "keywords": [
            "face drooping",
            "slurred speech",
            "sudden weakness",
            "seizure",
            "unconscious"
        ],
        "care_level": "Emergency",
        "explanation": (
            "Sudden neurological symptoms can indicate a serious emergency "
            "and require immediate professional medical care."
        )
    }
}


def process_symptoms(text):
    # Convert the text to lowercase.
    text = text.lower()

    # Split the text into words.
    tokens = word_tokenize(text)

    # Remove punctuation and common stop words.
    filtered_tokens = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    # Reduce words to their basic form.
    processed_tokens = [
        lemmatizer.lemmatize(word)
        for word in filtered_tokens
    ]

    return processed_tokens


# Assign a priority to each care level.
care_priority = {
    "Self-Care": 1,
    "Doctor Visit": 2,
    "Urgent": 3,
    "Emergency": 4
}


def analyze_symptoms(symptoms):
    # Compare the user's symptoms with the symptom knowledge base.
    processed_tokens = process_symptoms(symptoms)
    processed_text = " ".join(processed_tokens)

    best_match = None
    highest_score = 0
    highest_priority = 0

    for condition, information in symptom_database.items():
        current_matches = []

        for keyword in information["keywords"]:
            keyword_tokens = process_symptoms(keyword)

            # Match single-word symptoms directly in the processed word list.
            if len(keyword_tokens) == 1:
                if keyword_tokens[0] in processed_tokens:
                    current_matches.append(keyword)

            # Match longer symptom phrases in the processed text.
            else:
                processed_keyword = " ".join(keyword_tokens)
                if processed_keyword in processed_text:
                    current_matches.append(keyword)

        score = len(current_matches)
        priority = care_priority[information["care_level"]]

        if score > highest_score or (
            score == highest_score
            and score > 0
            and priority > highest_priority
        ):
            highest_score = score
            highest_priority = priority

            best_match = {
                "condition": condition,
                "care_level": information["care_level"],
                "explanation": information["explanation"],
                "matched_symptoms": current_matches,
                "score": score
            }

    if best_match is None:
        return {
            "condition": "No Clear Match",
            "care_level": "Doctor Visit",
            "explanation": (
                "The symptoms did not clearly match the categories in this "
                "project. Consider speaking with a healthcare professional "
                "if symptoms continue or become concerning."
            ),
            "matched_symptoms": [],
            "score": 0
        }

    return best_match


st.set_page_config(
    page_title="AI Symptom & Care Guide",
    page_icon="🩺"
)

st.title("🩺 AI Symptom & Care Guide")

st.write(
    "Describe the symptoms you are experiencing, and the app will "
    "provide a general care recommendation."
)

user_symptoms = st.text_area(
    "Enter your symptoms:",
    placeholder="Example: I have a fever, headache, body aches, and chills."
)

if st.button("Analyze Symptoms"):

    if not user_symptoms.strip():
        st.warning("Please enter at least one symptom.")

    else:
        result = analyze_symptoms(user_symptoms)

        st.subheader("Analysis Result")

        st.write("**Possible Category:**", result["condition"])
        st.write("**Care Level:**", result["care_level"])

        if result["matched_symptoms"]:
            st.write(
                "**Recognized Symptoms:**",
                ", ".join(result["matched_symptoms"])
            )

        st.write("**Explanation:**")
        st.write(result["explanation"])

        if result["care_level"] == "Emergency":
            st.error(
                "These symptoms may require immediate medical attention."
            )

        elif result["care_level"] == "Urgent":
            st.warning(
                "These symptoms may require prompt medical attention."
            )

st.markdown("---")

st.caption(
    "Disclaimer: This application is for educational purposes only. "
    "It does not provide a medical diagnosis and does not replace "
    "professional medical advice."
)
