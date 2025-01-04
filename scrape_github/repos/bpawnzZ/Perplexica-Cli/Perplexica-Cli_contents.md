# Repository: bpawnzZ/Perplexica-Cli

## File: .gitignore

```
.aider*
.env
build/
__pycache__/
*.egg-info/
*.pyc
perplexica_cli/perplexica_search.py.bak

```

## File: README.md

```
# Perplexica CLI

## Note
## You will need to modify the `perplexica_simple.py` and `perplexica_search.py` files with values that match your setup. Once you do that, install the package as described below.

## Description

Perplexica CLI provides command-line interfaces for interacting with the Perplexica Search API. It allows you to perform searches, list available models, and more.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bpawnzZ/Perplexica-Cli.git
   cd Perplexica-Cli
   ```

2. **Install the Package**

   ```bash
   pip install -e .
   ```

   This command installs the package in editable mode, ensuring that any changes you make to the source code are immediately reflected.

## Usage

### Commands

- **Simple Search**

  ```bash
  perplexica-simple -p "your search prompt"
  ```

  **Options:**
  - `-p, --prompt`: The search prompt (required).
  - `-s, --sources`: Show sources.
  - `-t, --timeout`: Timeout in seconds (default: 30).

- **Search**

  ```bash
  perplexica-search -p "your search prompt" -f webSearch -o speed
  ```

  **Options:**
  - `-p, --prompt`: The search prompt (required).
  - `-t, --timeout`: Timeout in seconds (default: 30).
  - `-f, --focus`: Focus mode for the search (default: webSearch).
  - `-o, --optimization`: Optimization mode (default: speed).
  - `--chat-provider`: Chat model provider.
  - `--chat-model`: Chat model name.
  - `--embedding-provider`: Embedding model provider.
  - `--embedding-model`: Embedding model name.
  - `-l, --list-models`: List available models and exit.

### Examples

1. **Perform a Search**

   ```bash
   perplexica-search -p "What is the capital of France?" -f webSearch -o speed
   ```

2. **List Available Models**

   ```bash
   perplexica-search -l
   ```

3. **Perform a Simple Search with Sources**

   ```bash
   perplexica-simple -p "give me an overview of sentiment regarding the crypto market" -s
   ```

   **Example Output:**

   ```plaintext
   Certainly! Here’s an overview of the sentiment regarding the crypto market:

   - **Definition and Importance**: Crypto market sentiment refers to the overall attitude or emotion that investors and traders have toward the cryptocurrency market. It is a collective sentiment—either bullish or bearish—based on factors such as market trends, news events, and social media discussions. This sentiment is crucial because it can significantly influence market behavior and price movements [1][7].

   - **Current Sentiment**: As of the latest data, the sentiment score for the cryptocurrency market is currently 100, indicating a strongly bullish sentiment. This suggests that the market is currently optimistic about the future of cryptocurrencies [11].

   - **Sources of Sentiment Data**:
     - **Community Votes**: Platforms like CoinMarketCap measure community sentiment by tallying bullish and bearish votes from users. This provides a direct gauge of how retail investors feel about the market [2].
     - **Technical Indicators**: Tools and platforms use technical indicators such as moving averages and oscillators to estimate market sentiment. These indicators help in identifying trends and potential turning points [11].
     - **Sentiment Analysis Tools**: Services like StockGeist.ai provide real-time sentiment monitoring of hundreds of cryptocurrencies. By analyzing social media, news articles, and other data sources, these tools can predict price movements [10].

   - **Factors Influencing Sentiment**:
     - **Market Trends**: The overall direction of the market, whether it is rising or falling, significantly impacts sentiment. For example, a prolonged bull run can boost investor confidence, while a bear market can lead to pessimism [1][4].
     - **News Events**: Major news events, such as regulatory changes, technological advancements, and macroeconomic factors, can sway market sentiment. Positive news can drive prices up, while negative news can cause prices to drop [1][5].
     - **Social Media and Forums**: Discussions on social media platforms and forums can amplify or dampen market sentiment. Positive or negative sentiment expressed by influential figures or large communities can have a significant impact [6][12].

   - **Behavioral Indicators**:
     - **Profit-Taking Patterns**: Analyzing profit-taking behavior can help identify market tops. A decline in profit-taking is often a sign of market "greed" and can indicate that the market is overbought [4].
     - **Transaction Flows**: Experts use data such as the "age" of Bitcoins held at addresses to categorize traders and predict their behavior. For instance, long-term holders might be less likely to sell during price drops, while short-term traders might be more reactive [5].

   - **Impact on Investment Decisions**:
     - **Tax Efficiency**: While sentiment is a powerful indicator, tax efficiency is also crucial for portfolio management. Crypto tax software can help investors maximize deductions and find tax-loss harvesting opportunities, ensuring they do not overpay or underpay their tax obligations [3].
     - **Predictive Power**: Understanding market sentiment can help investors make more informed decisions. For example, a positive sentiment can signal a good time to buy, while a negative sentiment might suggest a more cautious approach [13].

   - **Challenges and Considerations**:
     - **Volatility**: The crypto market is known for its high volatility, which can make sentiment analysis more challenging. Rapid price movements can quickly shift sentiment from bullish to bearish or vice versa [8].
     - **Speculation**: The market is often driven by speculation, especially in the early stages of new projects. This can lead to significant price fluctuations that may not always align with fundamental value [9].

   In summary, the current sentiment in the crypto market is bullish, driven by positive market trends, favorable news, and optimistic community sentiment. However, it is important to consider multiple factors and use a combination of tools to make well-informed investment decisions [1][7][11].

   Sources:
   - Crypto Market Sentiment Analysis Explained: https://academy.wirexapp.com/post/crypto-market-sentiment-guide
   - Crypto Community Sentiment - CoinMarketCap: https://coinmarketcap.com/sentiment/
   - How to Find & Analyze Crypto Market Sentiment - zenledger.io: https://zenledger.io/blog/what-is-crypto-market-sentiment/
   - Understanding the Current Sentiment in the Crypto Market: https://insights.santiment.net/read/understanding-the-current-sentiment-in-the-crypto-market-8255
   - Understanding Market Sentiment: How Crypto Sentiment Affects Prices: https://simpleswap.io/blog/how-crypto-sentiment-affects-prices
   - Crypto Sentiment Analysis Guide - Bitsgap: https://bitsgap.com/blog/understanding-and-using-sentiment-analytics-in-crypto-trading
   - What Is Crypto Market Sentiment? A Barometer for Investor ... - RoboFi: https://robofi.io/blog/what-is-crypto-market-sentiment/
   - Crypto Market Sentiment: Get to Know The Impact! - Quant Matter: https://quantmatter.com/crypto-market-sentiment-get-to-know-the-impact/
   - Understanding Crypto Market Trends - One Trading: https://onetrading.com/blogs/understanding-crypto-market-trends
   - Crypto Market Sentiment Analysis: https://www.stockgeist.ai/crypto-sentiment-analysis/
   - Bitcoin & Crypto Sentiment Today - CoinCodex: https://coincodex.com/sentiment/
   - Sentiment Analysis in Crypto Trading: A Beginners' Guide: https://www.kucoin.com/learn/trading/sentiment-analysis-in-crypto-trading-a-beginners-guide
   - Role of Sentiment Analysis in Crypto Trading: https://www.blockchain-council.org/blogs/sentiment-analysis-in-crypto-trading/
   - Crypto Fear & Greed Index - Bitcoin Sentiment - Alternative.me: https://alternative.me/crypto/fear-and-greed-index/
   - Not all words are equal: Sentiment and jumps in the ...: https://www.sciencedirect.com/science/article/pii/S1042443123001889
   ```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

## File: perplexica.ts

```
#!/usr/bin/env node

import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import inquirer from 'inquirer';
import axios from 'axios';
import ora from 'ora';
import chalk from 'chalk';

interface SearchResponse {
  answer: string;
  sources: Array<{
    title: string;
    url: string;
  }>;
}

const focusModes = [
  'webSearch',
  'academicSearch',
  'newsSearch',
  'codeSearch',
  'patentSearch'
] as const;

type FocusMode = typeof focusModes[number];

const optimizationModes = ['speed', 'balanced'] as const;
type OptimizationMode = typeof optimizationModes[number];

async function performSearch(
  query: string, 
  focusMode: FocusMode,
  optimizationMode: OptimizationMode
): Promise<SearchResponse> {
  const spinner = ora('Searching...').start();
  
  try {
    const response = await axios.post('http://100.71.229.63:3001/api/search', {
      query,
      focusMode,
      optimizationMode,
      history: []
    });

    spinner.succeed('Search completed');
    return response.data;
  } catch (error) {
    spinner.fail('Search failed');
    if (axios.isAxiosError(error)) {
      throw new Error(`Search failed: ${error.message}`);
    }
    throw error;
  }
}

async function main() {
  const argv = await yargs(hideBin(process.argv))
    .option('query', {
      alias: 'q',
      describe: 'Search query',
      type: 'string'
    })
    .option('focus', {
      alias: 'f',
      describe: 'Focus mode',
      choices: focusModes,
      type: 'string'
    })
    .option('optimization', {
      alias: 'o',
      describe: 'Optimization mode',
      choices: optimizationModes,
      default: 'balanced' as OptimizationMode,
      type: 'string'
    })
    .help()
    .argv;

  let query = argv.query;
  let focusMode = argv.focus as FocusMode;
  const optimizationMode = argv.optimization as OptimizationMode;

  if (!query || !focusMode) {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'query',
        message: 'Enter your search query:',
        when: !query
      },
      {
        type: 'list',
        name: 'focusMode',
        message: 'Select focus mode:',
        choices: focusModes,
        when: !focusMode
      }
    ]);

    query = query || answers.query;
    focusMode = focusMode || answers.focusMode;
  }

  try {
    const result = await performSearch(query, focusMode, optimizationMode);
    
    console.log('\n' + chalk.bold('Answer:'));
    console.log(result.answer);
    
    if (result.sources && result.sources.length > 0) {
      console.log('\n' + chalk.bold('Sources:'));
      result.sources.forEach((source, index) => {
        console.log(`${index + 1}. ${chalk.blue(source.title)}`);
        console.log(`   ${chalk.gray(source.url)}`);
      });
    }
  } catch (error) {
    console.error(chalk.red(error instanceof Error ? error.message : 'An unknown error occurred'));
    process.exit(1);
  }
}

main().catch(error => {
  console.error(chalk.red('Fatal error:', error));
  process.exit(1);
});

```

## File: __init__.py

```
# Package initialization

```

## File: perplexica_search.py

```
#!/usr/bin/env python3
import argparse
import json
import sys
import requests
from typing import Optional, Dict, List, Tuple

def get_available_models() -> Tuple[Dict, Dict]:
    """Get available chat and embedding models from the API"""
    chat_models = {
        "custom_openai": {
            "qwen/qwen-2.5-72b-instruct": {
                "provider": "custom_openai",
                "model": "qwen/qwen-2.5-72b-instruct",
                "customOpenAIKey": "your_api_key",
                "customOpenAIBaseURL": "http://your-custom-endpoint.com"
            }
        }
    }
    embedding_models = {
        "openai": {
            "text-embedding-3-small": {
                "provider": "openai",
                "model": "text-embedding-3-small",
                "api_key": "your_api_key"
            }
        }
    }
    return chat_models, embedding_models

def search(
    prompt: str,
    focus_mode: str = "webSearch",
    optimization_mode: str = "speed",
    chat_provider: Optional[str] = None,
    chat_model: Optional[str] = None,
    embedding_provider: Optional[str] = None,
    embedding_model: Optional[str] = None,
    timeout: int = 30
) -> None:
    """
    Send a search request to the Perplexica API and print the results
    """
    base_url = "http://100.71.229.63:3001/api"
    url = f"{base_url}/search"
    
    # Increase connection timeout and read timeout
    timeout = (10, 60)  # (connection timeout, read timeout)

    payload = {
        "query": prompt,
        "focusMode": focus_mode,
        "optimizationMode": optimization_mode,
        "chatModel": {
            "provider": "custom_openai",
            "model": "qwen/qwen-2.5-72b-instruct",
            "customOpenAIKey": "your_api_key",
            "customOpenAIBaseURL": "http://your-custom-endpoint.com"
        },
        "embeddingModel": {
            "provider": "openai",
            "model": "text-embedding-3-small"
        },
        "history": []
    }

    print("Sending payload:", json.dumps(payload, indent=2, ensure_ascii=False))  # Debug print

    try:
        response = requests.post(url, json=payload, timeout=timeout, headers={'Connection': 'close'})
        print("Response status:", response.status_code)  # Debug print
        print("Response headers:", dict(response.headers))  # Debug print
        
        response.raise_for_status()
        
        result = response.json()
        print("Response body:", json.dumps(result, indent=2, ensure_ascii=False))  # Debug print
        
        # Print the main message
        print("\nResult:")
        print(result["message"])
        
        # Print the sources
        if result.get("sources"):
            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source['metadata']['title']}: {source['metadata']['url']}")
                
    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                print("Error response:", json.dumps(error_data, indent=2, ensure_ascii=False))  # Debug print
                print(f"Error: {error_data.get('message', str(e))}")
            except ValueError:
                print(f"Error: {str(e)}")
        else:
            print(f"Error: {str(e)}")

def list_models() -> None:
    """List all available models"""
    chat_models, embedding_models = get_available_models()
    
    print("Available Chat Models:")
    for provider, models in chat_models.items():
        print(f"\n{provider}:")
        for model_key, model_info in models.items():
            print(f"  - {model_key}")
    
    print("\nAvailable Embedding Models:")
    for provider, models in embedding_models.items():
        print(f"\n{provider}:")
        for model_key, model_info in models.items():
            print(f"  - {model_key}")

def main():
    parser = argparse.ArgumentParser(description='Perplexica Search CLI')
    parser.add_argument('-p', '--prompt', help='Search prompt')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='Timeout in seconds (default: 30)')
    parser.add_argument('-f', '--focus', default='webSearch', 
                      choices=['webSearch', 'academicSearch', 'writingAssistant', 
                              'wolframAlphaSearch', 'youtubeSearch', 'redditSearch'],
                      help='Focus mode for the search (default: webSearch)')
    parser.add_argument('-o', '--optimization', default='speed',
                      choices=['speed', 'balanced'],
                      help='Optimization mode (default: speed)')
    parser.add_argument('--chat-provider', help='Chat model provider')
    parser.add_argument('--chat-model', help='Chat model name')
    parser.add_argument('--embedding-provider', help='Embedding model provider')
    parser.add_argument('--embedding-model', help='Embedding model name')
    parser.add_argument('-l', '--list-models', action='store_true',
                      help='List available models and exit')
    
    args = parser.parse_args()

    try:
        if args.list_models:
            list_models()
            return

        if not args.prompt:
            parser.error("the following arguments are required: -p/--prompt")
            
        search(
            prompt=args.prompt,
            focus_mode=args.focus,
            optimization_mode=args.optimization,
            chat_provider=args.chat_provider,
            chat_model=args.chat_model,
            embedding_provider=args.embedding_provider,
            embedding_model=args.embedding_model,
            timeout=args.timeout
        )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```

## File: perplexica_simple.py

```
#!/usr/bin/env python3
import argparse
import json
import sys
import requests
from typing import Optional

def search(prompt: str, show_sources: bool = False, timeout: int = 30) -> None:
    """
    Send a search request to the Perplexica API and print the results
    """
    base_url = "http://100.71.229.63:3001/api"
    url = f"{base_url}/search"
    
    # Increase connection timeout and read timeout
    timeout = (10, 60)  # (connection timeout, read timeout)

    payload = {
        "query": prompt,
        "focusMode": "webSearch",
        "optimizationMode": "speed",
        "chatModel": {
            "provider": "custom_openai",
            "model": "qwen/qwen-2.5-72b-instruct",
            "customOpenAIKey": "your_api_key",
            "customOpenAIBaseURL": "http://your-custom-endpoint.com"
        },
        "embeddingModel": {
            "provider": "openai",
            "model": "text-embedding-3-small"
        },
        "history": []
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout, headers={'Connection': 'close'})
        response.raise_for_status()
        
        result = response.json()
        
        # Print the main message
        print(result["message"])
        
        # Print the sources only if requested
        if show_sources and result.get("sources"):
            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source['metadata']['title']}: {source['metadata']['url']}")
                
    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                print(f"Error: {error_data.get('message', str(e))}")
            except ValueError:
                print(f"Error: {str(e)}")
        else:
            print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Simple Perplexica Search CLI')
    parser.add_argument('-p', '--prompt', required=True, help='Search prompt')
    parser.add_argument('-s', '--sources', action='store_true', help='Show sources')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='Timeout in seconds (default: 30)')
    
    args = parser.parse_args()

    try:
        search(
            prompt=args.prompt,
            show_sources=args.sources,
            timeout=args.timeout
        )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```

## File: setup.py

```
from setuptools import setup, find_packages

setup(
    name="perplexica-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'perplexica-search=perplexica_cli.perplexica_search:main',
            'perplexica-simple=perplexica_cli.perplexica_simple:main',
        ],
    },
    python_requires='>=3.7',
    author="Perplexica Team",
    description="CLI tools for Perplexica Search API",
    long_description="Command line interfaces for interacting with the Perplexica Search API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

```

## File: setup.py

```
from setuptools import setup, find_packages

setup(
    name="perplexica-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'perplexica-search=perplexica_cli.perplexica_search:main',
            'perplexica-simple=perplexica_cli.perplexica_simple:main',
        ],
    },
    python_requires='>=3.7',
    author="Perplexica Team",
    description="CLI tools for Perplexica Search API",
    long_description="Command line interfaces for interacting with the Perplexica Search API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

```

