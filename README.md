# Financial Analysis Bot 📊

An intelligent financial analysis tool powered by Claude AI that analyzes financial documents and provides comprehensive insights with reasoning and recommendations.

## Features

- 📁 **Multi-format Support**: Analyze PDF, Excel, and CSV files
- 🤖 **Claude-Powered Analysis**: Deep financial insights with AI reasoning
- 📄 **Word Export**: Generate professional Word documents with analysis
- 🔊 **Audio Reports**: Convert analysis to English audio format
- 💬 **Follow-up Questions**: Ask clarifying questions about the analysis
- 🌐 **Streamlit Web App**: User-friendly web interface

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd financial-analysis-bot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate      # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your Anthropic API key:
     ```
     ANTHROPIC_API_KEY=sk-ant-...
     ```

## Usage

### Command Line Application

```bash
python main.py
```

Then:
1. Enter the path to your financial file
2. View the analysis results
3. Choose to export as Word, Audio, or ask follow-up questions

### Streamlit Web Application

```bash
streamlit run streamlit_app.py
```

Then open your browser to the local URL shown (usually `http://localhost:8501`)

## Project Structure

```
financial-analysis-bot/
├── main.py                 # Command-line application
├── streamlit_app.py        # Web application
├── claude_analyzer.py      # Claude API integration
├── file_extractor.py       # File parsing utilities
├── report_generator.py     # Output generation
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## API Key Setup

⚠️ **Important**: Never commit your API key to GitHub!

1. Get your API key from [Anthropic Console](https://console.anthropic.com)
2. Create a `.env` file (not tracked by git):
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```
3. The `.env` file is in `.gitignore` and won't be pushed to GitHub

## File Format Support

### Supported Formats
- **PDF**: Financial reports, statements, audits
- **Excel**: Spreadsheets with financial data (.xlsx, .xls)
- **CSV**: Comma-separated values

### Data Extraction
- Automatically extracts text and tables
- Provides summary statistics for numerical data
- Preserves data structure and relationships

## Analysis Output

The bot provides:

1. **Key Financial Insights**: Main findings and patterns
2. **Reasoning & Logic**: How conclusions were reached
3. **Recommendations**: Actionable suggestions

## Export Formats

- **Word Document (.docx)**: Professional formatted report with all analysis
- **Audio (MP3)**: English text-to-speech narration of analysis

## Deployment to GitHub

1. Initialize git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Financial analysis bot"
   ```

2. Add remote and push:
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

## Streamlit Cloud Deployment

1. Push code to GitHub (see above)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create new app from GitHub repo
4. Set secrets:
   - In Streamlit Cloud dashboard, add `.streamlit/secrets.toml`:
     ```
     ANTHROPIC_API_KEY = "sk-ant-..."
     ```

## Requirements

- Python 3.8+
- Anthropic API key
- See `requirements.txt` for all dependencies

## Troubleshooting

**Error: ANTHROPIC_API_KEY not found**
- Ensure `.env` file exists with your API key
- Check that `.env` is in the same directory as the scripts

**PDF extraction issues**
- Some PDFs with scans may not extract text properly
- Try OCR-enabled PDFs for best results

**Audio generation slow**
- First run initializes text-to-speech engine
- Subsequent runs are faster

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and create a Pull Request

## License

MIT License - feel free to use this project

## Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ using Claude AI and Python**
