# agent.py

# Import OpenAI library
import os

from openai import OpenAI

# Put your API key here
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Function to analyze symptoms
def analyze_symptoms(symptoms):
    """
    This function sends symptoms to the AI
    and gets possible medical explanations.
    """

    prompt = f"""
    A patient reports the following symptoms: {symptoms}

    Suggest possible medical conditions and advise
    whether the patient should see a doctor.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# Test the agent
if __name__ == "__main__":

    symptoms = "fever, headache, fatigue"

    result = analyze_symptoms(symptoms)

    print("AI Response:")
    print(result)