"""
Example usage of the Financial Analysis Bot
This demonstrates how to use the bot programmatically
"""
from dotenv import load_dotenv
from claude_analyzer import analyze_financial_data, ask_followup_question

# Load environment variables
load_dotenv()

def example_analysis():
    """Example: Analyze sample financial data"""
    
    # Sample financial data (you would extract this from a real file)
    sample_data = """
    ACME Corporation - Financial Summary 2024
    
    Revenue by Quarter:
    Q1: $2,500,000
    Q2: $2,750,000
    Q3: $3,100,000
    Q4: $3,400,000
    Total Revenue: $11,750,000 (up 18% YoY)
    
    Operating Expenses:
    Salaries: $4,500,000
    Marketing: $1,200,000
    Operations: $2,100,000
    R&D: $1,800,000
    Total: $9,600,000
    
    Net Income: $2,150,000
    Net Profit Margin: 18.3%
    
    Assets:
    Cash: $1,500,000
    Accounts Receivable: $800,000
    Inventory: $600,000
    Equipment: $2,100,000
    Total Assets: $5,000,000
    
    Liabilities:
    Accounts Payable: $400,000
    Short-term Debt: $500,000
    Long-term Debt: $1,200,000
    Total Liabilities: $2,100,000
    
    Equity: $2,900,000
    Current Ratio: 3.67
    Debt-to-Equity: 0.72
    """
    
    print("="*60)
    print("FINANCIAL ANALYSIS BOT - EXAMPLE")
    print("="*60)
    print("\nAnalyzing sample financial data...")
    print("-"*60)
    
    # Perform analysis
    analysis, history = analyze_financial_data(
        sample_data,
        "ACME_Corp_2024_Summary.txt"
    )
    
    print("\nInitial Analysis:")
    print("-"*60)
    print(analysis)
    
    # Example follow-up question
    print("\n" + "="*60)
    print("FOLLOW-UP QUESTION")
    print("="*60)
    
    followup = "What should ACME focus on to improve profitability?"
    print(f"\nQuestion: {followup}")
    print("-"*60)
    
    response, history = ask_followup_question(followup, history)
    print("\nResponse:")
    print("-"*60)
    print(response)
    
    print("\n" + "="*60)
    print("Example complete! The bot can now analyze your files.")
    print("="*60)

if __name__ == "__main__":
    example_analysis()
