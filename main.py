import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('')
address = web3.toChecksumAddress()

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated Greeting: {}'.format(
    contract.functions.greet().call()
))




