import PyPDF2
import pandas as pd
from pathlib import Path

def extract_pdf_content(file_path: str, max_chars: int = 50000) -> str:
    """Extract text from PDF file with character limit"""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(pdf_reader.pages):
                if len(text) >= max_chars:
                    text += f"\n... [File truncated - {len(pdf_reader.pages) - i} pages remaining] ..."
                    break
                text += page.extract_text() + "\n"
        return text[:max_chars]
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def extract_excel_content(file_path: str, max_rows: int = 100) -> str:
    """Extract data from Excel file with optimized row limit"""
    try:
        excel_file = pd.ExcelFile(file_path)
        content = ""
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            total_rows = len(df)
            
            # Limit rows to avoid token overflow
            if total_rows > max_rows:
                df = pd.concat([df.head(max_rows//2), df.tail(max_rows//2)])
                content += f"\n{'='*50}\nSheet: {sheet_name} (Showing first {max_rows//2} and last {max_rows//2} rows of {total_rows} total)\n{'='*50}\n"
            else:
                content += f"\n{'='*50}\nSheet: {sheet_name} ({total_rows} rows)\n{'='*50}\n"
            
            content += df.to_string(max_rows=max_rows)
            content += "\n\nDataFrame Summary:\n"
            content += str(df.describe())
            
        return content
    except Exception as e:
        raise Exception(f"Error reading Excel file: {str(e)}")

def extract_csv_content(file_path: str, max_rows: int = 100) -> str:
    """Extract data from CSV file with optimized row limit"""
    try:
        df = pd.read_csv(file_path)
        total_rows = len(df)
        
        # Limit rows to avoid token overflow
        if total_rows > max_rows:
            df = pd.concat([df.head(max_rows//2), df.tail(max_rows//2)])
            content = f"Showing first {max_rows//2} and last {max_rows//2} rows of {total_rows} total\n\n"
        else:
            content = f"Total rows: {total_rows}\n\n"
        
        content += df.to_string()
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
