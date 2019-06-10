# Sawtooth Django G-KYC (Global-Know Your Customer)

steps: [setup dev environment Ubuntu 16.04](https://sawtooth.hyperledger.org/docs/core/releases/latest/app_developers_guide/ubuntu.html)
## 1. Generate a user key
`$ sawset keygen`
## 2. Create the genesis block
`$ sawtooth genesis`  
`$ sudo -u sawtooth sawadm genesis config-genesis.batch`
## 3. Generate the root key for the validator
`$ sudo sawadm keygen`     

## Do following steps in different terminal window_ 
## 4. Strart the validator  
`$ sudo -u sawtooth sawtooth-validator -vv`  

in the new terminal window, start dev-mode consensus engine  
## 5. Start the Devmod Consensus Engine
`$ sudo -u sawtooth devmode-engine-rust -vv --connect tcp://localhost:5050`  

open new terminal
## 6. Start the rest api  
`$ sudo -u sawtooth sawtooth-rest-api -v`  

open new terminal  
## 7. Start the Transaction Processors
1. Settings transaction processor  
`$ sudo -u sawtooth settings-tp -v`  

## 8. Start G-KYC Transaction Processor  
`$ cd ~/peace/gkyc/ && python3 processor/main.py`  

## 9. Start Django Client
activate virtualenv and run django server   
`$ source ~/env/ekyc/bin/activate && python manage.py runserver`  


## dependencies
1. google protocol buffer

## decript data
`$ import base64`  
`$ bData = '-------'`  
`$ d = base64.b64decode(bData)`  
`$ import cbor`  
`$ cbor.loads(d)`
