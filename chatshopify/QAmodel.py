import pandas as pd
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import os

# Function to load context from CSV
def load_context_from_csv(csv_file, column_name):
    assets_dir = os.path.join(os.getcwd(), 'media', 'assets')
    csv_file_path = os.path.join(assets_dir, csv_file)
    df = pd.read_csv(csv_file_path)
    context = " ".join(df[column_name].tolist())
    return context

def callQuestion(question):
    model_name = "deepset/roberta-base-squad2"

    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    csv_file_name = "Sfile1_1.csv"
    context_column ="Tutorial"

    context = load_context_from_csv(csv_file_name, context_column)
    
    
    QA_input = {
        'question': question,
        'context': context
    }

    res = nlp(QA_input)
    print("Answer:", res['answer'])
    return res['answer']