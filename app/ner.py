import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Simulated resume snippet
text = """
John Doe is a software engineer with 5 years of experience in Python, Docker, and AWS.
He previously worked at Google and graduated from Stanford University in 2018.
"""

# Process the text
doc = nlp(text)

# Print named entities
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
