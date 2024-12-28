from web3 import Web3


# Replace with your private key
private_key = "0xxxxxxxxx"

# Create a Web3 instance (even though we are not connecting to any provider, Web3 works offline here)
w3 = Web3()

# Derive the account (address) from the private key using the updated method
account = w3.eth.account.from_key(private_key)

# Print the derived address
print("Ethereum Address:", account.address)

