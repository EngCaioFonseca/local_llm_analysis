# LLM Data Analysis Assistant

## Overview

This Streamlit-based web application leverages the power of local Large Language Models (LLMs) to analyze CSV and Excel datasets. It uses the Llama 2 7B Chat model to provide intelligent data analysis and general question answering capabilities.

## Features

- Upload and preview CSV or Excel files
- Display basic dataset information
- LLM-powered data analysis based on user questions
- General chat interface for broader queries
- Local execution of Llama 2 model using llama-cpp-python

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Openpyxl
- llama-cpp-python

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/llm-data-analysis-assistant.git
   cd llm-data-analysis-assistant
   ```

2. Install the required packages:
   ```
   pip install streamlit pandas openpyxl llama-cpp-python
   ```

3. Download the Llama 2 7B Chat model:
   The model will be automatically downloaded when you run the application for the first time.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Use the file uploader to select a CSV or Excel file for analysis

4. Ask questions about the data in the text area provided

5. Use the sidebar to ask general questions to the LLM

## How it Works

1. The application loads the Llama 2 7B Chat model using llama-cpp-python
2. Users can upload CSV or Excel files, which are then parsed using Pandas
3. Basic information about the dataset is displayed
4. Users can ask questions about the data, which are then processed by the LLM
5. The LLM generates responses based on the dataset information and the user's question
6. A general chat interface is provided in the sidebar for broader queries

## Customization

- You can adjust the model parameters in the `load_model()` function:
  - `n_ctx`: Sets the context window size (default: 2048)
  - `n_threads`: Sets the number of CPU threads to use (default: 4)

## Limitations

- The app runs the LLM locally, so performance will depend on your machine's capabilities
- The Llama 2 7B model, while powerful, may not be as capable as larger models or specialized data analysis tools
- The analysis is based on the text description of the data, not on direct manipulation of the dataset

## Contributing

Contributions to improve the LLM Data Analysis Assistant are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Streamlit for the web app framework
- The Llama 2 model developers
- TheBloke for providing the quantized GGUF model
- The llama-cpp-python library developers
