import json
from web3 import Web3

BASE_RPC_URL = "https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"

web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

if not web3.isConnected():
    raise Exception("Failed to connect to the Base network")

with open('contracts/BaseCheckers.json') as f:
    contract_abi = json.load(f)["abi"]

contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

def join_game(account, private_key):
    nonce = web3.eth.getTransactionCount(account)
    txn = contract.functions.joinGame().buildTransaction({
        'from': account,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

def make_move(account, private_key, from_x, from_y, to_x, to_y):
    nonce = web3.eth.getTransactionCount(account)
    txn = contract.functions.makeMove(from_x, from_y, to_x, to_y).buildTransaction({
        'from': account,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)
