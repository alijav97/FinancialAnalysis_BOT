import os
from anthropic import Anthropic

def get_api_key():
    """Get API key from environment variable"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables. Please set it in .env file")
    return api_key

def create_claude_client():
    """Create and return Anthropic client"""
    api_key = get_api_key()
    return Anthropic(api_key=api_key)

def analyze_financial_data(file_content: str, file_name: str, conversation_history: list = None) -> str:
    """
    Analyze financial data using Claude
    
    Args:
        file_content: Extracted text content from financial file
        file_name: Name of the file being analyzed
        conversation_history: List of previous messages for context
    
    Returns:
        Analysis from Claude
    """
    client = create_claude_client()
    
    if conversation_history is None:
        conversation_history = []
    
    # Add the analysis request
    user_message = f"""
    I have a financial data file: {file_name}
    
    Here is the content:
    
    {file_content}
    
    Please provide:
    1. Key Financial Insights - Main findings and patterns
    2. Reasoning & Logic - Explanation of how you arrived at these insights
    3. Recommendations - Actionable suggestions based on the analysis
    
    Format your response clearly with these three sections.
    """
    
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2048,
        system="""You are an expert financial analyst with deep knowledge of accounting, 
        financial metrics, investment analysis, and business strategy. Provide thorough, 
        data-driven analysis with clear reasoning.""",
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history

def ask_followup_question(question: str, conversation_history: list) -> str:
    """
    Ask a follow-up question about the financial analysis
    
    Args:
        question: Follow-up question from user
        conversation_history: Previous conversation context
    
    Returns:
        Claude's response
    """
    client = create_claude_client()
    
    conversation_history.append({
        "role": "user",
        "content": question
    })
    
    response = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=2048,
        system="""You are an expert financial analyst with deep knowledge of accounting, 
        financial metrics, investment analysis, and business strategy. Provide thorough, 
        data-driven analysis with clear reasoning.""",
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history
