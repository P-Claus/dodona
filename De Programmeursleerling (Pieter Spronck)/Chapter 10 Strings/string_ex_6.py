text = "I'm sorry, sir."

cleaned_text = text.replace("'", " ")
cleaned_text1 = cleaned_text.replace(",", "")
cleaned_text2 = cleaned_text1.replace(".", "")
final_text_lower = cleaned_text2.lower()

final_text = final_text_lower.split()

print(final_text)