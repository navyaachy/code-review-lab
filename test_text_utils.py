from text_utils import clean_text, word_count
def clean_text(text):
  return text.strip().lower()
def word_count(text):
  return len(text.split())

assert clean_text("  Hello August  ") == "hello august"
assert word_count("Open source tools") == 3

print("All tests passed")
