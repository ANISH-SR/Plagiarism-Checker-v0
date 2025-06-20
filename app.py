from flask import Flask, render_template, request
from difflib import SequenceMatcher
import os
try:
    import PyPDF2
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def plagiarism_score(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio() * 100

def read_file_content(file):
    """Read and return file content as string"""
    try:
        # Reset file pointer to beginning
        file.seek(0)
        
        # Get file extension
        filename = file.filename.lower()
        
        if filename.endswith('.txt'):
            # Handle text files
            content = file.read()
            if isinstance(content, bytes):
                try:
                    return content.decode('utf-8')
                except UnicodeDecodeError:
                    return content.decode('utf-8', errors='ignore')
            return str(content)
        
        elif filename.endswith('.pdf'):
            # Handle PDF files
            if not PDF_SUPPORT:
                raise Exception("PDF support not available. Please install PyPDF2: pip install PyPDF2")
            
            try:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                
                if not text.strip():
                    raise Exception("Could not extract text from PDF. The PDF might be image-based or encrypted.")
                
                return text
            except Exception as pdf_error:
                raise Exception(f"Error reading PDF: {str(pdf_error)}")
        
        elif filename.endswith(('.doc', '.docx')):
            # For now, ask user to convert to .txt or .pdf
            raise Exception("Please convert .doc/.docx files to .txt or .pdf format")
        
        else:
            # Try to read as text file anyway
            content = file.read()
            if isinstance(content, bytes):
                try:
                    return content.decode('utf-8')
                except UnicodeDecodeError:
                    return content.decode('utf-8', errors='ignore')
            return str(content)
            
    except Exception as e:
        raise Exception(f"Error reading file '{file.filename}': {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    error = None
    
    if request.method == 'POST':
        try:
            comparison_type = request.form.get('comparison_type', 'text')
            
            if comparison_type == 'text':
                # Handle text comparison
                text1 = request.form.get('text1', '').strip()
                text2 = request.form.get('text2', '').strip()
                
                if not text1 or not text2:
                    error = "Please provide both texts for comparison"
                else:
                    score = round(plagiarism_score(text1, text2), 2)
                    
            elif comparison_type == 'file':
                # Handle file comparison
                file1 = request.files.get('file1')
                file2 = request.files.get('file2')
                
                if not file1 or not file1.filename or not file2 or not file2.filename:
                    error = "Please upload both files for comparison"
                else:
                    try:
                        text1 = read_file_content(file1)
                        text2 = read_file_content(file2)
                        
                        if len(text1.strip()) < 10 or len(text2.strip()) < 10:
                            error = "Files appear to be too short or empty (minimum 10 characters required)"
                        else:
                            score = round(plagiarism_score(text1, text2), 2)
                    except Exception as file_error:
                        error = str(file_error)
                        
        except Exception as e:
            error = f"Error processing request: {str(e)}"
    
    return render_template('index.html', score=score, error=error)

if __name__ == '__main__':
    app.run(debug=True)
