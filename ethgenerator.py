import blocksmith
import json

paper_wallet = {}

kg = blocksmith.KeyGenerator()
kg.seed_input('kaoka tony pipo jake cortazar androide18 frambuesa cambur aguacate lechoza gelato nueve')
index = 0
desired = 10
while index < desired: 
    key = kg.generate_key()
    #file.write(key + "\n")
    address = blocksmith.EthereumWallet.generate_address(key)
    print(address)
    checksum_address = blocksmith.EthereumWallet.checksum_address(address)
    #file.write(checksum_address + "\n")
    paper_wallet[checksum_address] = "{}".format(key)
    index += 1

json_data = json.dumps(paper_wallet)
file = open('CTOK000001.txt', "w")
file.write(json_data)
file.close()