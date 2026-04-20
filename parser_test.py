# LLM Similarity Check - Parser Testing

student_input = "AI helps students learn better"

# Remove spaces
cleaned_input = student_input.strip()

# Validation
if not cleaned_input:
    print("Invalid input: Blank")
elif len(cleaned_input) < 5:
    print("Invalid input: Too short")
else:
    print("Valid input")
    print("Processing for similarity analysis...")
