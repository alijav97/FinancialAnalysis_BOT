# Quick Start Guide - Financial Analysis Bot

## Setup Complete! ✓

Your Financial Analysis Bot is ready to use. Here's how to get started:

### Option 1: Command-Line Interface

```bash
# Make sure you're in the project directory
cd c:\Users\alija\Downloads\London International - AI\Module C\Day 3\Project 3

# Run the bot
python main.py
```

Then:
1. Enter the path to your financial file (PDF, Excel, or CSV)
2. Wait for the analysis
3. Choose to export as Word, Audio, or ask follow-up questions

### Option 2: Web Interface (Streamlit)

```bash
# Run the Streamlit app
streamlit run streamlit_app.py
```

Then open your browser to `http://localhost:8501`

## File Requirements

- **PDF**: Financial reports, balance sheets, income statements
- **Excel**: .xlsx or .xls files with financial data
- **CSV**: Comma-separated financial data

## Output Formats

### Word Document
- Professional formatted report
- Sections: Key Insights, Reasoning & Logic, Recommendations
- Automatically generated with timestamp
- Saves to `output/` folder

### Audio Report
- MP3 file with English text-to-speech
- Full analysis read aloud
- Great for quick reviews
- Saves to `output/` folder

## API Key

Your Anthropic API key is stored in the `.env` file. This file is excluded from Git (see `.gitignore`).

⚠️ **Important**: Never commit `.env` to GitHub

## Project Structure

```
Project 3/
├── main.py                 # CLI application
├── streamlit_app.py        # Web application  
├── claude_analyzer.py      # Claude API integration
├── file_extractor.py       # File parsing
├── report_generator.py     # Output generation
├── requirements.txt        # Dependencies
├── .env                    # API key (not in git)
├── .env.example           # Template
├── .gitignore             # Git rules
└── README.md              # Full documentation
```

## Pushing to GitHub

1. Initialize Git (if not done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Financial Analysis Bot"
   ```

2. Add your repository:
   ```bash
   git remote add origin <YOUR_REPO_URL>
   git push -u origin main
   ```

The `.env` file will NOT be pushed (it's in `.gitignore`), keeping your API key safe.

## Deploying to Streamlit Cloud

1. Push code to GitHub (see above)
2. Go to https://streamlit.io/cloud
3. Create new app from your GitHub repo
4. In "Advanced Settings", add secret:
   ```
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
5. Deploy!

## Troubleshooting

**API Key Error?**
- Make sure `.env` file exists in the project root
- Check that `ANTHROPIC_API_KEY=` is set correctly

**PDF not extracting text?**
- Some PDFs are scanned images - they won't extract text
- Try an OCR-enabled PDF or convert to text first

**Audio generation slow?**
- First run initializes the text-to-speech engine
- Subsequent runs are faster

## Next Steps

1. Test with a sample financial file
2. Customize the analysis prompts in `claude_analyzer.py` if needed
3. Push to GitHub when ready
4. Deploy to Streamlit Cloud for production

---

**You're all set! Happy analyzing! 🎉**
