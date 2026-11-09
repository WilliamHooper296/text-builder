
import re

input_file = "bible.txt"
output_file = "bible.txt"

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Remove book names and chapter:verse references
text = re.sub(
    r'^[\w ]+\s+\d+:\d+\s*',
    '',
    text,
    flags=re.MULTILINE
)

# Remove paragraph formatting markers
text = text.replace("¶", "")

# Save cleaned text
with open(output_file, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Successfully cleaned Bible text and saved to {output_file}")
