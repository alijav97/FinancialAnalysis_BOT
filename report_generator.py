from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import pyttsx3
from pathlib import Path
from datetime import datetime

def create_word_report(analysis: str, file_name: str, output_path: str = "output") -> str:
    """
    Create a Word document with financial analysis
    
    Args:
        analysis: Analysis text from Claude
        file_name: Name of the analyzed file
        output_path: Directory to save the report
    
    Returns:
        Path to created document
    """
    Path(output_path).mkdir(exist_ok=True)
    
    doc = Document()
    
    # Add title
    title = doc.add_heading('Financial Analysis Report', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    # Add metadata
    metadata = doc.add_paragraph()
    metadata.add_run('File Analyzed: ').bold = True
    metadata.add_run(file_name)
    
    metadata = doc.add_paragraph()
    metadata.add_run('Date Generated: ').bold = True
    metadata.add_run(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Add analysis
    doc.add_heading('Analysis', level=1)
    
    # Parse and format analysis sections
    lines = analysis.split('\n')
    current_section = None
    
    for line in lines:
        if line.strip():
            if 'Key' in line and 'Insights' in line:
                doc.add_heading('Key Financial Insights', level=2)
                current_section = 'insights'
            elif 'Reasoning' in line or 'Logic' in line:
                doc.add_heading('Reasoning & Logic', level=2)
                current_section = 'reasoning'
            elif 'Recommendation' in line:
                doc.add_heading('Recommendations', level=2)
                current_section = 'recommendations'
            else:
                doc.add_paragraph(line, style='List Bullet')
        else:
            doc.add_paragraph()
    
    # Save document
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(output_path) / f"Financial_Analysis_{timestamp}.docx"
    doc.save(str(output_file))
    
    return str(output_file)

def create_audio_report(analysis: str, output_path: str = "output") -> str:
    """
    Create audio report from analysis using text-to-speech
    
    Args:
        analysis: Analysis text from Claude
        output_path: Directory to save the audio file
    
    Returns:
        Path to created audio file
    """
    Path(output_path).mkdir(exist_ok=True)
    
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    # Configure voice settings
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Save audio file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(output_path) / f"Financial_Analysis_{timestamp}.mp3"
    
    engine.save_to_file(analysis, str(output_file))
    engine.runAndWait()
    
    return str(output_file)

def export_analysis(analysis: str, file_name: str, format: str = "word", output_path: str = "output") -> str:
    """
    Export analysis in specified format
    
    Args:
        analysis: Analysis text from Claude
        file_name: Name of analyzed file
        format: Export format ('word' or 'audio')
        output_path: Output directory
    
    Returns:
        Path to exported file
    """
    if format.lower() == "word":
        return create_word_report(analysis, file_name, output_path)
    elif format.lower() == "audio":
        return create_audio_report(analysis, output_path)
    else:
        raise ValueError(f"Unsupported format: {format}. Use 'word' or 'audio'")
