# Sawtooth Django G-KYC (Global-Know Your Customer)

steps: 
## 1. Generate a user key
`$ sawset keygen`
## 2. Create the genesis block
`$ sawtooth genesis`  
`$ sudo -u sawtooth sawadm genesis config-genesis.batch`
## 3. Generate the root key for the validator
`$ sudo sawadm keygen`  
## 4. Strart the validator  
`$ sudo -u sawtooth sawtooth-validator -vv`  

in the new terminal window, start devmode consensus engine  
## 5. Start the Devmod Consensus Engine
`$ sudo -u sawtooth devmode-engine-rust -vv --connect tcp://localhost:5050`  

open new terminal
## 6. Start the rest api  
`$ sudo -u sawtooth sawtooth-rest-api -v`  

open new terminal  
## 7. Start the Transaction Processors
1. Settings transaction processor  
`$ sudo -u sawtooth settings-tp -v`

## dependencies
1. cbor
`$ pip install cbor`

## decript data
`$ import base64`  
`$ bData = '-------'`
`$ d = base64.b64decode(bData)`  
`$ import cbor`  
`$ cbor.loads(d)`