# SPDX-License-Identifier: MIT
"""
This file is part of the Ethereum Blockchain Explorer project, which is released under the MIT License.
See file LICENSE or go to https://opensource.org/licenses/MIT for full license details.
"""

import os
from web3 import Web3

def get_web3_instance():
    alchemy_api_key = os.getenv('ALCHEMY_API_KEY')
    if not alchemy_api_key:
        raise ValueError("ALCHEMY_API_KEY environment variable not set")
    alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_api_key}"
    return Web3(Web3.HTTPProvider(alchemy_url))

def get_latest_block(web3):
    latest_block = web3.eth.get_block('latest')
    return latest_block

def display_block_info(block):
    print(f"Block Number: {block['number']}")
    print(f"Timestamp: {block['timestamp']}")
    print(f"Miner: {block['miner']}")
    print(f"Number of Transactions: {len(block['transactions'])}")

def main():
    web3 = get_web3_instance()
    if not web3.is_connected():
        print("Failed to connect to Ethereum network")
        return
    
    latest_block = get_latest_block(web3)
    display_block_info(latest_block)

if __name__ == "__main__":
    main()
