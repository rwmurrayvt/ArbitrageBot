import cexapi
import time
import re
import json

username = 'rwmurrayVT'
api_key = 'Xb9RAbsur42NvaSbHvEu13nZ8'
api_secret = 'QZbPY0SmfBbi3r2LMrqc86apu7A'
api = cexapi.api(username,api_key,api_secret)

x = 1
while x == 1:
    ghsbtc = api.order_book('GHS/BTC/?depth=1')
    nmcbtc = api.order_book('NMC/BTC/?depth=1')
    ghsnmc = api.order_book('GHS/NMC/?depth=1')
    r = re.compile('\d+.\d+')
    ghsbtcdata = r.findall(ghsbtc)
    nmcbtcdata = r.findall(nmcbtc)
    ghsnmcdata = r.findall(ghsnmc)
    print ghsbtcdata
    print nmcbtcdata
    print ghsnmcdata
    time.sleep(5)
