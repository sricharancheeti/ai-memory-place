import io
import PyPDF2
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- CORS Configuration ---
origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Helper Function for Text Splitting ---
def split_text_into_sections(text: str, sentences_per_section: int = 20) -> list[dict]:
    """A simple function to split text into sections based on sentence count."""
    sentences = text.replace('\n', ' ').split('. ')
    sections = []
    
    # Group sentences into sections
    for i in range(0, len(sentences), sentences_per_section):
        section_sentences = sentences[i:i + sentences_per_section]
        section_text = ". ".join(section_sentences)
        
        # Don't add empty sections
        if section_text.strip():
            sections.append({
                "title": f"Section {len(sections) + 1}",
                "text": section_text.strip() + "."
            })
            
    return sections

# --- API Endpoints ---

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "Hello from AI Memory Palace Backend!"}


@app.post("/upload-pdf/")
async def create_upload_file(file: UploadFile = File(...)):
    """
    Accepts a PDF, extracts text, splits it into sections, and returns JSON.
    """
    # Read the PDF file in-memory
    file_content = await file.read()
    pdf_stream = io.BytesIO(file_content)
    
    # Extract text from the PDF
    reader = PyPDF2.PdfReader(pdf_stream)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
        
    # Split the text into sections
    sections = split_text_into_sections(full_text)
    
    return {"sections": sections}