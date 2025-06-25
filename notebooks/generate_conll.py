import pandas as pd

# Load preprocessed CSV (update path if necessary)
df = pd.read_csv("data/messages.csv")

# Write to CoNLL format
with open("data/ner_raw.conll", "w", encoding="utf-8") as f:
    for tokens in df["tokens"]:
        for token in str(tokens).split():
            f.write(f"{token} O\n")  # Label every token with 'O'
        f.write("\n")  # Separate each message with a blank line
