from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

physics_pdf_path = 'text_books/basicphysics.pdf'
chemistry_pdf_path = 'text_books/chemistry.pdf'
biology_pdf_path = 'text_books/modernbiology.pdf'

physics_text = extract_text_from_pdf(physics_pdf_path)
chemistry_text = extract_text_from_pdf(chemistry_pdf_path)
biology_text = extract_text_from_pdf(biology_pdf_path)
    
with open("extracted_texts/physics_text.txt","w") as text_file:
    text_file.write(physics_text)
    
with open("extracted_texts/chemistry_text.txt","w") as text_file:
    text_file.write(chemistry_text)

with open("extracted_texts/biology_text.txt","w") as text_file:
    text_file.write(biology_text)