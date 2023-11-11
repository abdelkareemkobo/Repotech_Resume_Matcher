# ATS Helper
An application that parse, extract data from pdf files and then use them to recommend keywords that increase the similiairty and make you able to pass the ATS system 


## Table of Contents

## Installation

1. Clone the repository: `git clone https://github.com/your-username/ats-helper.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Navigate to the project directory: `cd notebooks/streamlit_versions`
4. Run streamlit `sr main.py` 
5. Upload the pdf files and it will work 
### Note 
- Change the cohere api in the direcotry to your api; 

## Features

- **Resume Parsing**: Extracts relevant information from resumes, such as name, contact details, skills, and work experience.
- **Cosine Similarity**: Uses cosine similarity to match job descriptions with applicant resumes, providing a score indicating the similarity.
- **AI-powered Suggestions**: Provides AI-generated suggestions for improving job descriptions or identifying potential candidates.

## Notes about the work 
1. The work hasn't been completed yet 
   1. the cos similairty needs to be adjusted to show the real improvements 
   2. I didn't use qdrant anymore it's not need feel free to use your database
   3. for the api i am using cohere which is cheaper than using openai and alot cheaper than using your own llama model :) 


