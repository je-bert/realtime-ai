# realtime-ai

A simple script to utilize ChatGPT on your custom files and connect to various APIs for real-time data integration.

## Installation

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

  ```
  > cd realtime-ai
  ```

4. Create a new virtual environment

  MacOS & Linux
  ```
  > python -m venv venv
  > . venv/bin/activate
  ```

  Windows
  ```
  > python -m venv venv
  > venv/Scripts/activate.bat
  ```

5. Install the requirements

  ```
  > pip install -r requirements.txt
  ```

6. Set OpenAI API key

  Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

7. Place your own data into `data/data.txt`.

## Example usage

Test fetching `TSLA` stock data.
```
> python main.py "What is the current stock price of TSLA?"
[*********************100%***********************]  1 of 1 completed
Stock data exported successfully to data/TSLA.txt
The current stock price of TSLA is $291.5899963378906.
```

Test reading `data/data.txt` file.
```
> python main.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python main.py "what is my cat's name"
Your cat's name is Muffy.
```