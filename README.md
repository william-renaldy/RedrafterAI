# Redrafter AI

## Overview

The Redrafter AI project is designed to redraft text using generative AI, providing improved clarity, conciseness, and engagement. The project includes the following files:

- `main.py`: The main script for running the Streamlit application.
- `processor.py`: The Processor class responsible for redrafting text using generative AI.
- `utility.py`: A utility module containing prompts for redrafting in different styles.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Install required packages using the following command:

```bash
pip install -r requirements.txt
```
### Usage
Set up your environment by creating a .env file and adding your API key:

```env
API_KEY=your_api_key_here
```
Run the Streamlit application:

```bash
streamlit run main.py
```
Open your web browser and navigate to the provided URL.

Enter the text you want to redraft, choose a tone, and click the "Redraft" button.
