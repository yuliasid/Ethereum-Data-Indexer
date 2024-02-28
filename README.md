# Ethereum-Data-Indexer
## Description
This Ethereum Blockchain Explorer is a simple Python tool designed to connect to the Ethereum blockchain via the Alchemy API, fetch the latest block's information, and display details such as the block number, timestamp, miner address, and the number of transactions it contains. This project serves as a foundational tool for those interested in exploring Ethereum blockchain data, with potential for expansion into a more comprehensive explorer.

## Methodology
The project utilizes the web3.py library to interface with the Ethereum blockchain. It connects to an Ethereum node provided by Alchemy, fetches data for the latest block, and processes this data to display relevant information. The tool can be extended to include more detailed explorations of blocks, transactions, and accounts on the Ethereum blockchain.

## Features
Connect to the Ethereum blockchain using an Alchemy node.
Fetch and display the latest block information:
+ Block Number
+ Timestamp
+ Miner Address
+ Number of Transactions

## Installation
Ensure you have Python 3.x installed on your system. Then, follow these steps:

### Clone the Repository:
```
git clone (https://github.com/yuliasid/Ethereum-Data-Indexer)
```
### Navigate to the Project Directory:
```
cd ethereum_data_indexer
```

### Create and Activate a Virtual Environment (optional but recommended):

+ On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
+ On macOS and Linux:
```
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies:
```
pip install -r requirements.txt
```
## Usage
Before running the script, ensure you have set up your ALCHEMY_API_KEY environment variable:

+ On Windows:
```
setx ALCHEMY_API_KEY "YourAlchemyApiKeyHere"
```

+ On macOS/Linux:
```
export ALCHEMY_API_KEY="YourAlchemyApiKeyHere"
```


## To run the Ethereum Blockchain Explorer and fetch the latest block information:

```
python blockchain_explorer.py
```

## Expansion Ideas
+ Implement functionality to view detailed transaction data within blocks.
+ Add capability to explore historical blocks based on block number or hash.
+ Integrate functionality to view account balances and transaction history.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
