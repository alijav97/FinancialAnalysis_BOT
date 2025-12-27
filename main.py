"""
Financial Analysis Bot using Claude API
Main entry point for the application
"""
import os
from dotenv import load_dotenv
from file_extractor import extract_file_content, get_file_summary
from claude_analyzer import analyze_financial_data, ask_followup_question
from report_generator import export_analysis

# Load environment variables
load_dotenv()

def main():
    """Main function to run the financial analysis bot"""
    print("="*60)
    print("Financial Analysis Bot")
    print("="*60)
    print("\nSupported formats: PDF, Excel (.xlsx, .xls), CSV")
    
    # Get file path from user
    file_path = input("\nEnter the path to your financial file: ").strip()
    
    try:
        # Get file summary
        file_info = get_file_summary(file_path)
        print(f"\nFile: {file_info['name']}")
        print(f"Size: {file_info['size']} bytes")
        print(f"Type: {file_info['type']}")
        
        # Extract content
        print("\nExtracting content from file...")
        file_content = extract_file_content(file_path)
        
        # Analyze with Claude
        print("\nAnalyzing financial data with Claude...")
        analysis, conversation_history = analyze_financial_data(
            file_content, 
            file_info['name']
        )
        
        print("\n" + "="*60)
        print("ANALYSIS RESULTS")
        print("="*60)
        print(analysis)
        
        # Export options
        while True:
            print("\n" + "="*60)
            print("Export Options:")
            print("1. Export as Word document")
            print("2. Export as Audio (English)")
            print("3. Ask follow-up question")
            print("4. Exit")
            
            choice = input("\nSelect an option (1-4): ").strip()
            
            if choice == "1":
                output_file = export_analysis(analysis, file_info['name'], "word")
                print(f"\n✓ Report saved to: {output_file}")
                
            elif choice == "2":
                print("\nGenerating audio report...")
                output_file = export_analysis(analysis, file_info['name'], "audio")
                print(f"\n✓ Audio saved to: {output_file}")
                
            elif choice == "3":
                question = input("\nEnter your follow-up question: ").strip()
                print("\nProcessing question...")
                response, conversation_history = ask_followup_question(
                    question, 
                    conversation_history
                )
                print("\n" + "="*60)
                print("RESPONSE")
                print("="*60)
                print(response)
                
            elif choice == "4":
                print("\nThank you for using Financial Analysis Bot!")
                break
            else:
                print("Invalid option. Please select 1-4.")
    
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please check your file path and try again.")

if __name__ == "__main__":
    main()
