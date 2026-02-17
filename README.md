# Healthcare Chatbot

A simple Streamlit-based chatbot that analyzes a diseases-and-symptoms dataset and gives medical advice suggestions based on the uploaded data. This project is intended for demonstration and educational purposes only — it is not a substitute for professional medical advice.

## Features
- Load and analyze a CSV dataset (Diseases_Symptoms.csv).
- Provide symptom-to-disease suggestions based on the dataset.
- Simple Streamlit UI for uploading the dataset and interacting with the chatbot.
- Lightweight and easy to run locally.

## Table of contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset format](#dataset-format)
- [Example workflow](#example-workflow)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Contact](#contact)

## Requirements
- Python 3.8+
- Streamlit
- pandas (and any other packages listed in requirements.txt)

Make sure to install dependencies from the `requirements.txt` file in the repository.

## Installation
1. Clone the repository (if not already cloned):
   ```bash
   git clone https://github.com/Hash-ir777/Healthcare_Chatbot.git
   
   cd Healthcare_Chatbot
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
   # macOS/Linux
   source .venv/bin/activate

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Streamlit app. Replace `app.py` with the actual Streamlit script filename if different (e.g., `streamlit_app.py`):
   ```bash
   streamlit run app.py
   ```

2. In the Streamlit web UI:
   - Use the file uploader to upload `Diseases_Symptoms.csv`.
   - Follow the on-screen instructions to interact with the chatbot and get suggestions based on symptoms you provide.

## Dataset format
The app expects a CSV file named `Diseases_Symptoms.csv` (or any CSV with the same column structure). Typical columns:
- `disease` — the disease name
- `symptoms` — a list/CSV/string of symptoms associated with the disease

If your dataset uses different column names or structure, either rename columns to match or adjust the data loading/processing code in the app.

## Example workflow
1. Upload `Diseases_Symptoms.csv`.
2. Enter symptoms into the chatbot UI (comma-separated or as prompted).
3. The app will analyze the dataset and return possible disease matches or advice derived from the dataset.

## Troubleshooting
- "Streamlit command not found": ensure streamlit is installed in the active environment (`pip install streamlit`) and that the virtual environment is activated.
- "CSV upload fails" or "KeyError": check the CSV file columns and make sure they match the expected names used by the app.
- If you get unexpected behavior, check the console logs where you ran `streamlit run` for stack traces.

## Contributing
Contributions are welcome. Suggested ways to help:
- Improve dataset parsing and matching logic.
- Add tests or CI to validate functionality.
- Improve the UI/UX on the Streamlit page.
- Add more documentation or example datasets.

To contribute:
1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/my-change`
3. Make your changes and commit.
4. Push and open a pull request.

## Contact
If you have questions or want help improving the README or app, open an issue or contact the repository owner: @Yusufali2004 @Hash-ir777.

---
