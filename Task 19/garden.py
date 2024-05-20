import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The horse raced past the barn fell.",  # Example from Wikipedia
    "The complex houses married and single soldiers and their families.",  # Another 
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenization and Named Entity Recognition (NER)
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(i, i.label_, i.label) for i in doc.ents])
    entity_fac = spacy.explain("FAC")
    print(f"FAC:{entity_fac}")    
    print("\n")  # Add space between sentences

# Comments on two entities
# Replace this with your analysis after running the code
"""
1. Entity: Band-Aid (ORG)
   Explanation: Organization (companies, agencies, institutions, etc.)
   Sense: Makes sense here since Band-Aid is a brand name, representing a company.

2. Entity: Mississippi (GPE)
   Explanation: Geopolitical Entity (countries, cities, states)
   Sense: Yes, the entity accurately identifies Mississippi as a state
"""