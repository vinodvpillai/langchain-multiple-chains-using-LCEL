# LangChain Multiple Separate Chains Example

This repository demonstrates a simple example of using LangChain to create multiple separate chains with the LangChain Execution Language (LCEL).

## Overview

LangChain is a powerful framework for building applications with large language models. This example showcases how to create and manage multiple separate chains using LCEL, allowing for modular and reusable components in your language model applications.

## Features

- **Multiple Chains**: Demonstrates how to create and manage multiple separate chains.
- **LCEL Integration**: Utilizes LangChain Execution Language for defining and executing chains.
- **Modular Design**: Encourages modular and reusable components.

## Getting Started

### Prerequisites

- Python 3.11+
- `langchain` library
- `openai` library
- `python-dotenv` library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/vinodvpillai/langchain-multiple-chains-example.git
    cd langchain-multiple-chains-example
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

### Usage

Run the example:
    ```bash
    python main.py
    ```

### Example Output
```
python main.py
Some popular food options from England that you can enjoy while watching cricket include:

1. Fish and chips - a classic British dish consisting of battered fish and deep-fried chips
2. Shepherd's pie - a hearty dish made with minced meat and topped with mashed potatoes
3. Scones with clotted cream and jam - a traditional British tea-time treat
4. Bangers and mash - sausages served with mashed potatoes and onion gravy
5. Roast beef with Yorkshire pudding - a quintessential Sunday roast dish
6. Cornish pasties - savory pastries filled with meat and vegetables
7. Eton mess - a delicious dessert made with meringue, whipped cream, and strawberries

Enjoy these tasty dishes while cheering on England in the next Cricket World Cup!
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LangChain for providing the framework.
- The open-source community for continuous support and contributions.

