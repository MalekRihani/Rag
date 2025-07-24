Pizza Q&A Bot

Overview

This project is a simple question-answering bot focused on pizza-related queries. It uses the langchain_ollama library with the llama3.2 model to process questions and provide answers. The bot retrieves relevant pizza reviews using a custom retriever and responds based on a predefined prompt template.

Features





Interactive command-line interface for asking pizza-related questions.



Uses the llama3.2 model from langchain_ollama for natural language processing.



Integrates a custom retriever to fetch relevant pizza reviews.



Exits gracefully when the user inputs q.

Prerequisites





Python 3.8 or higher



Required Python packages:





langchain_ollama



langchain_core



A custom retriever module (ensure it is implemented and accessible in the project directory).

Installation





Clone the repository:

git clone <repository-url>
cd <repository-directory>



Install the required dependencies:

pip install langchain_ollama langchain_core



Ensure the retriever module is properly set up in the project directory.

Usage





Run the script:

python pizza_qa_bot.py



Enter a pizza-related question when prompted.



To exit, type q and press Enter.

Example:

-----------------------------------------------------------------
Enter your question : What makes a good pizza crust?

[Response from the bot]
-----------------------------------------------------------------
Enter your question : q

Code Structure





Main Script: pizza_qa_bot.py (or rename as needed) contains the core logic.



Retriever: A custom module (vector.py) that provides the retriever object for fetching relevant reviews.



Prompt Template: Defines the structure for processing questions and reviews using PromptTemplate from langchain_core.



Model: Uses the llama3.2 model via OllamaLLM for generating responses.

Limitations





The retriever module is not included in this repository. You must implement or provide it separately.



The bot currently does not use the retrieved reviews in the response generation (empty reviews list in chain.invoke). Update the code to incorporate reviews as needed.



Requires a working installation of the llama3.2 model through langchain_ollama.

Contributing

Contributions are welcome! Please follow these steps:





Fork the repository.



Create a new branch (git checkout -b feature-branch).



Make your changes and commit (git commit -m "Add feature").



Push to the branch (git push origin feature-branch).



Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
