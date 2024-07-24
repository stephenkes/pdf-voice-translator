import PyPDF2
import pyttsx3

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Step 2 & 3: Convert text to speech and play it
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    pdf_path = "file:///C:/Users/USER/Documents/Rich%20Dad%20Poor%20Dad.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    speak_text(extracted_text)

if __name__ == "__main__":
    main()