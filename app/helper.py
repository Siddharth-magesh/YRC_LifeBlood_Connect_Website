from nltk.tokenize import word_tokenize
import math
from datetime import datetime

def replace_none(text):
    words = word_tokenize(text.lower())
    replaced_words = ['none' if word in ['none','-',"no","nill","nan","na"] else word for word in words]
    return ' '.join(replaced_words)

def is_nan(value):
    return isinstance(value,float) and math.isnan(value)

def convert_to_date(date_strings):
    date_objects = []
    for date in date_strings:
        if is_nan(date):
            date_objects.append(None)
        else:
            date_objects.append(datetime.strptime(date, '%d-%m-%Y').date())
    return date_objects