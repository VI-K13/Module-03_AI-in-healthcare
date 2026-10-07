# AI Symptom & Care Guide

## Project Overview

AI Symptom & Care Guide is a simple AI-driven healthcare application that analyzes symptoms entered by the user and provides a general care recommendation.

The application uses Natural Language Processing (NLP) to process the user's symptom description and compare it with a small symptom knowledge base. Based on the recognized symptoms, the application returns a possible symptom category, a care level, the symptoms it recognized, and a short explanation.

This project was created for educational purposes and is not intended to provide a real medical diagnosis.

## Features

The application can:

- Accept symptom descriptions written in normal language
- Process the text using basic NLP techniques
- Recognize symptom keywords and phrases
- Match symptoms with a small healthcare knowledge base
- Provide one of four care levels:
  - Self-Care
  - Doctor Visit
  - Urgent
  - Emergency
- Show the symptoms that were recognized
- Explain why the result was selected
- Avoid guessing when there is no clear match
- Display warnings for urgent or emergency-level results
- Provide a simple Streamlit user interface
- Include a medical disclaimer

## How It Works

The application first processes the symptom description using NLTK.

The NLP process includes:

1. Converting the text to lowercase
2. Tokenizing the sentence into individual words
3. Removing punctuation and common stop words
4. Lemmatizing the remaining words

After preprocessing, the application compares the user's symptoms with keywords stored in the symptom knowledge base.

Each symptom category has:

- A list of symptom keywords
- A care level
- An explanation

The program counts how many symptoms match each category. The category with the strongest match is selected.

If two categories have the same score, the application gives priority to the more serious care level.

The care levels used in this project are:

- Self-Care
- Doctor Visit
- Urgent
- Emergency

## Technologies Used

- Python
- Google Colab
- NLTK
- Streamlit
- Cloudflare Tunnel
- GitHub

## Symptom Categories

The current version of the application includes several basic symptom categories:

- General Headache Symptoms
- Common Cold
- Flu-Like Symptoms
- Possible Infection
- Severe Abdominal Symptoms
- Breathing or Chest Emergency
- Neurological Emergency

## Example Results

### Example 1

Input:

I have a headache

Result:

Possible Category: General Headache Symptoms  
Care Level: Self-Care  
Recognized Symptoms: headache

### Example 2

Input:

I have fever, chills, headache, and body aches

Result:

Possible Category: Flu-Like Symptoms  
Care Level: Doctor Visit  
Recognized Symptoms: fever, chills, body aches

### Example 3

Input:

I have severe stomach pain and persistent vomiting

Result:

Possible Category: Severe Abdominal Symptoms  
Care Level: Urgent

### Example 4

Input:

I have chest pain and difficulty breathing

Result:

Possible Category: Breathing or Chest Emergency  
Care Level: Emergency

### No Clear Match Example

The application was also tested with symptoms that were not included in the knowledge base.

Input:

I am feeling dizzy

Result:

Possible Category: No Clear Match  
Care Level: Doctor Visit

Instead of guessing a condition, the application provides a general recommendation when it cannot find a clear match.

## Testing

I tested the application with different symptom descriptions to check whether the symptom matching and care levels worked correctly.

The test cases included mild headache symptoms, cold symptoms, flu-like symptoms, severe abdominal symptoms, breathing or chest symptoms, and symptoms that were not included in the knowledge base.

The testing showed that the application could recognize the symptom patterns stored in the database and provide different care levels depending on the result.

It also showed one of the limitations of the project. If a symptom is not included in the knowledge base, the application cannot identify it and returns No Clear Match.

## How to Run the Project

The project was developed and tested in Google Colab.

To run the project:

1. Open the Jupyter Notebook in Google Colab.
2. Run the notebook cells from top to bottom.
3. The notebook installs the required libraries.
4. The notebook creates the Streamlit application file called `app.py`.
5. Start the Streamlit server.
6. Run the Cloudflare tunnel cell.
7. Open the temporary public link that appears.
8. Enter a symptom description in the text box.
9. Click **Analyze Symptoms**.

The application will display the result below the symptom input.

## Project Files

The repository includes:

- `2372_Module_3_AI_Symptom_Care_Guide_Viktoriya.ipynb`
- `app.py`
- `README.md`

The notebook contains the full project development process, testing, and explanations.

The `app.py` file contains the final Streamlit application.

The `README.md` file explains the project and how it works.

## Limitations

This application has several important limitations.

The symptom knowledge base is small and was created for this educational project. Because of this, the application cannot recognize every possible symptom or medical condition.

The project does not use real patient records or a professionally validated medical dataset.

The results are based mainly on keyword matching, so different wording may affect whether a symptom is recognized.

The application should not be used for real medical diagnosis or treatment decisions.

## Future Improvements

If I continued developing this project, I would like to improve it by:

- Adding more symptoms
- Adding more health categories
- Using a larger healthcare dataset
- Improving recognition of different ways people describe symptoms
- Adding confidence scores
- Testing more symptom combinations
- Improving the Streamlit interface
- Exploring a machine learning model
- Exploring an LLM-based version of the symptom checker
- Improving the way the application handles symptoms that belong to multiple categories

## What I Learned

This project helped me understand how Natural Language Processing can be used in a simple healthcare application.

I worked with tokenization, stop-word removal, lemmatization, keyword matching, and basic text processing.

I also learned how important the symptom database is because the quality of the application's results depends on the information included in the knowledge base.

The project also gave me experience using Streamlit to create an interface, testing different user inputs, troubleshooting errors, and running a web application from Google Colab.

## AI Assistance

I developed and coded this project with some assistance from ChatGPT.

I used ChatGPT mainly for brainstorming ideas, coding guidance, troubleshooting errors, and improving parts of the application.

I reviewed the code, tested the application, worked through errors, and made decisions about the project structure, symptom categories, care levels, and final design.

## Research Sources

- Centers for Disease Control and Prevention (CDC) – used to review common respiratory and flu-like symptoms.

  (https://www.cdc.gov/index.html)
  
- MedlinePlus – used to review general symptom information and when medical attention may be needed.

  (https://medlineplus.gov/)

- Streamlit Documentation – used as a reference for creating the application interface.

  (https://docs.streamlit.io/)

## Disclaimer

This application was created for educational and demonstration purposes only.

It does not provide a medical diagnosis and should not replace advice from a qualified healthcare professional.
