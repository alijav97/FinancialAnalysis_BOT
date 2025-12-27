"""
Test script to verify the Financial Analysis Bot setup
Run this to ensure everything is configured correctly
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_environment():
    """Test environment variables"""
    print("Testing environment variables...")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found")
        return False
    print("✓ ANTHROPIC_API_KEY is set")
    return True

def test_imports():
    """Test all required imports"""
    print("\nTesting imports...")
    try:
        import anthropic
        print("✓ anthropic")
        import pandas
        print("✓ pandas")
        import PyPDF2
        print("✓ PyPDF2")
        from docx import Document
        print("✓ python-docx")
        import pyttsx3
        print("✓ pyttsx3")
        import streamlit
        print("✓ streamlit")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_modules():
    """Test our custom modules"""
    print("\nTesting custom modules...")
    try:
        from file_extractor import extract_file_content
        print("✓ file_extractor")
        from claude_analyzer import create_claude_client
        print("✓ claude_analyzer")
        from report_generator import export_analysis
        print("✓ report_generator")
        return True
    except ImportError as e:
        print(f"❌ Module error: {e}")
        return False

def test_output_directory():
    """Check output directory"""
    print("\nChecking output directory...")
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
        print("✓ Created output directory")
    else:
        print("✓ Output directory exists")
    return True

def test_api_connection():
    """Test connection to Claude API"""
    print("\nTesting Claude API connection...")
    try:
        from anthropic import Anthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        client = Anthropic(api_key=api_key)
        
        # Quick test with claude-opus model (more reliable)
        response = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=100,
            messages=[{"role": "user", "content": "Say 'API connection successful' in one sentence."}]
        )
        print(f"✓ API connection successful")
        print(f"  Response: {response.content[0].text[:50]}...")
        return True
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("Financial Analysis Bot - Setup Test")
    print("="*60)
    
    results = []
    
    results.append(("Environment", test_environment()))
    results.append(("Imports", test_imports()))
    results.append(("Custom Modules", test_modules()))
    results.append(("Output Directory", test_output_directory()))
    results.append(("API Connection", test_api_connection()))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "="*60)
    if all_passed:
        print("✓ All tests passed! Bot is ready to use.")
        print("\nNext steps:")
        print("1. Command-line: python main.py")
        print("2. Web app: streamlit run streamlit_app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
