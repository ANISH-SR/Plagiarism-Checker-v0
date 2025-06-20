# Plagiarism Checker

A web-based plagiarism detection tool built with Flask that compares texts or documents to identify similarities. Features a modern dark/light mode interface built with Tailwind CSS and shadcn-inspired styling.

## Features

- **Text Comparison**: Direct text input comparison
- **File Upload Support**: Upload and compare .txt and .pdf files
- **Similarity Scoring**: Uses Python's difflib for accurate similarity detection
- **Modern UI**: Clean, responsive design with dark/light mode toggle
- **Real-time Results**: Instant similarity percentage with visual indicators

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### 1. Clone or Download the Project

```bash
cd /home/anish/intern/codeclause/plagirism_checker
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install Flask
pip install flask

# Install PyPDF2 for PDF support
pip install PyPDF2
```

### 4. Project Structure

Make sure your project has the following structure:

```
plagirism_checker/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional - using Tailwind CDN)
├── uploads/ (auto-created)
└── README.md
```

## Usage

### 1. Start the Application

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Run the Flask app
python app.py
```

### 2. Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### 3. Using the Plagiarism Checker

#### Text Comparison:
1. Select "Text Input" option
2. Enter text in both text areas
3. Click "Check Plagiarism"

#### File Comparison:
1. Select "File Upload" option
2. Upload two files (.txt or .pdf format)
3. Click "Check Plagiarism"

### 4. Understanding Results

- **0-29%**: Low similarity (likely original content)
- **30-69%**: Moderate similarity (review recommended)
- **70-100%**: High similarity (potential plagiarism)

## Features Guide

### Dark/Light Mode
- Click the sun/moon icon in the top-right corner to toggle themes
- Theme preference is saved in browser localStorage

### File Support
- **.txt files**: Direct text extraction
- **.pdf files**: Text extraction using PyPDF2
- **File size limit**: 16MB maximum

### Error Handling
- Empty file detection
- Unsupported file format warnings
- PDF extraction error handling
- Network and server error messages

## Development

### Running in Development Mode

```bash
# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run with Flask CLI
flask run
```

### Alternative Running Methods

```bash
# Direct Python execution
python app.py

# With debug mode
python -c "from app import app; app.run(debug=True)"
```

## Troubleshooting

### Common Issues

1. **"PDF support not available" error**:
   ```bash
   pip install PyPDF2
   ```

2. **"Files appear to be empty" error**:
   - Ensure files contain readable text
   - Check file encoding (UTF-8 recommended)
   - PDF files must contain extractable text (not image-based)

3. **Port 5000 already in use**:
   ```bash
   # Kill process using port 5000
   sudo lsof -ti:5000 | xargs kill -9
   
   # Or run on different port
   flask run --port 5001
   ```

4. **Virtual environment issues**:
   ```bash
   # Recreate virtual environment
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install flask PyPDF2
   ```

### File Upload Issues

- Ensure uploaded files are not corrupted
- Check file permissions
- Verify file format (.txt or .pdf only)
- Maximum file size is 16MB

## Technical Details

### Libraries Used
- **Flask**: Web framework
- **difflib**: Similarity calculation
- **PyPDF2**: PDF text extraction
- **Tailwind CSS**: Styling (via CDN)

### Algorithm
The plagiarism detection uses Python's `difflib.SequenceMatcher` which:
- Compares sequences of text
- Returns similarity ratio between 0.0 and 1.0
- Accounts for character-level and word-level similarities

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes as part of the CodeClause internship program.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure Python 3.7+ is being used
4. Check that virtual environment is activated
