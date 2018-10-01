import blocksmith
import json
import qrcode

paper_wallet = {}

kg = blocksmith.KeyGenerator()
kg.seed_input('kaoka tony pipo jake cortazar androide18 frambuesa cambur aguacate lechoza gelato nueve')
index = 0
desired = 10
while index < desired: 
    key = kg.generate_key()
    address = blocksmith.EthereumWallet.generate_address(key)
    print(address)
    checksum_address = blocksmith.EthereumWallet.checksum_address(address)
    paper_wallet[checksum_address] = "{}".format(key)
    index += 1

json_data = json.dumps(paper_wallet)
file = open('CTOK000001.json', "w")
file.write(json_data)
file.close()