import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample resume text (you can later replace this with extracted resume text)
text = """
Jane Doe is a data scientist with 6 years of experience in Python, TensorFlow, and AWS.
She holds a Master's degree from MIT and has worked at Meta and Tesla.
"""

# Process the text
doc = nlp(text)

# Print all named entities
print("Named Entities found:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
