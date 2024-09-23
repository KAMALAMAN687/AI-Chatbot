import spacy
import sys
import json

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def classify_intent(text):
    doc = nlp(text.lower())
    if "product" in text:
        return "Product Inquiry"
    elif "order" in text and ("status" in text or "track" in text):
        return "Check Order Status"
    elif "return" in text or "refund" in text:
        return "Returns and Refunds"
    elif "payment" in text:
        return "Payment Issues"
    elif "recommend" in text or "suggest" in text:
        return "Personalized Recommendations"
    return "Unknown Intent"

def extract_entities(text):
    doc = nlp(text)
    
    entities = {
        "product": None,
        "order_number": None,
        "user_id": None,
    }
    
    for ent in doc.ents:
        if ent.label_ == "PRODUCT":
            entities["product"] = ent.text
        elif ent.label_ == "DATE":
            entities["order_number"] = ent.text
        elif ent.label_ == "USER_ID":
            entities["user_id"] = ent.text
    return entities

if __name__ == "__main__":
    user_input = sys.argv[1]
    intent = classify_intent(user_input)
    entities = extract_entities(user_input)
    
    output = {
        "intent": intent,
        "entities": entities
    }
    print(json.dumps(output))
