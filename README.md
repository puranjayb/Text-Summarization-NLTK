
# Text Summarization - Python Script for Extractive Summarization
## Project Description
- This project is a Python script that performs extractive text summarization. 
- It takes input text and generates a summary by extracting the most important sentences from the input text based on word frequency and sentence scores.

## Dependencies
- nltk: Python library for natural language processing
- string: Python library for string manipulation
- heapq: Python library for heap operations


## Installation
- To use the Text Summarization script, follow these steps:
- Clone the repository 
```bash
    git clone https://github.com/puranjayb/Text-Summarization-NLTK.git
```
- Make sure you are running **Python Version 3.9.0**
```bash
    pip install virtualenv
    virtualenv Summarization
    .\Summarization\Scripts\activate

    You may need to give access permission visit [here](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows#:~:text=To%20fix%20it%2C%20you%20should%20try%20executing%20Set-ExecutionPolicy,more%20unsafe%2C%20but%20recommended%20by%20MS%20Tech%20Support.) for that
```
- Install the required libraries and modules
```bash
    pip install -r requirements.txt
    nltk.download('punkt')
    nltk.download('stopwords')
```
    
