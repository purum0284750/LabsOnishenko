import re
text1="emoji 😀 не слово"
def tokenize(text: str) -> list[str]:
    return re.findall("[\w-]+", text)
text2 = tokenize(text1)
print(text2)