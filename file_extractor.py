import PyPDF2
import pandas as pd
from pathlib import Path

def extract_pdf_content(file_path: str) -> str:
    """Extract text from PDF file"""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def extract_excel_content(file_path: str) -> str:
    """Extract data from Excel file"""
    try:
        excel_file = pd.ExcelFile(file_path)
        content = ""
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            content += f"\n{'='*50}\nSheet: {sheet_name}\n{'='*50}\n"
            content += df.to_string()
            content += "\n\nDataFrame Info:\n"
            content += str(df.describe())
            
        return content
    except Exception as e:
        raise Exception(f"Error reading Excel file: {str(e)}")

def extract_csv_content(file_path: str) -> str:
    """Extract data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        content = df.to_string()
        content += "\n\nDataFrame Statistics:\n"
        content += str(df.describe())
        return content
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")

def extract_file_content(file_path: str) -> str:
    """
    Extract content from financial file (PDF, Excel, CSV)
    
    Args:
        file_path: Path to the financial file
    
    Returns:
        Extracted text content
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_extension = file_path.suffix.lower()
    
    if file_extension == '.pdf':
        return extract_pdf_content(file_path)
    elif file_extension in ['.xlsx', '.xls']:
        return extract_excel_content(file_path)
    elif file_extension == '.csv':
        return extract_csv_content(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: PDF, Excel, CSV")

def get_file_summary(file_path: str) -> dict:
    """Get file metadata"""
    file_path = Path(file_path)
    return {
        "name": file_path.name,
        "size": file_path.stat().st_size,
        "type": file_path.suffix
    }
