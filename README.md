# my-ai

Simple script to use ChatGPT on your own files.

je_bert@Berts-MacBook-Pro my-ai % python3 -m venv venv          
je_bert@Berts-MacBook-Pro my-ai % . venv/bin/activate
(venv) je_bert@Berts-MacBook-Pro my-ai % pip3 install -r requirements.txt

## Installation

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy.
```
