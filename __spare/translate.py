# Use a pipeline as a high-level helper
from transformers import pipeline

enru_pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")

ruen_pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")


tr = ruen_pipe('Привет, как дела?')[0]['translation_text']
op = enru_pipe(tr)[0]['translation_text']

print(tr)
print(op)