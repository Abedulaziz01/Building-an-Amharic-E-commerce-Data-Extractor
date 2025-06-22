import pandas as pd
import re

# === Emoji Removal Function ===
def remove_all_emojis(text):
    emoji_pattern = re.compile(
        "["

        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"  # dingbats
        "\U000024C2-\U0001F251"  # enclosed characters
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U0001FA70-\U0001FAFF"  # extended pictographs
        "\U00002600-\U000026FF"  # miscellaneous symbols
        "\u200d"                 # zero-width joiner
        "\u2640-\u2642"          # gender symbols
        "\uFE0F"                 # variation selectors
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub('', str(text))

# === Load Data and Remove Emojis ===
def main():
    input_file = "../data/telegram_data.csv"
    output_file = "../data/telegram_data_no_emoji.csv"
    column_to_clean = "Message"

    try:
        # Load CSV
        df = pd.read_csv(input_file)

        # Check column existence
        if column_to_clean not in df.columns:
            raise ValueError(f"Column '{column_to_clean}' not found in file.")

        # Remove emojis
        df[column_to_clean] = df[column_to_clean].apply(remove_all_emojis)

        # Save cleaned CSV
        df.to_csv(output_file, index=False)
        print(f"✅ Emoji-free data saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
