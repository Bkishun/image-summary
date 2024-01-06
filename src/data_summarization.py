from src.components.data_ingestion import image_to_text
from src.components.data_transformation import summarize
def predict_summary(filename):
    text = image_to_text(filename)
    summary = summarize(text)
    return summary,text