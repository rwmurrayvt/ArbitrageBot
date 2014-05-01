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
    GBdata = r.findall(ghsbtc)
    NBdata = r.findall(nmcbtc)
    GNdata = r.findall(ghsnmc)
    GHSbuy = float(GNdata[4])
    NMCneed = float(GNdata[4])*float(GNdata[3])
    NMCavailable = float(NBdata[4])
    if NMCavailable<NMCneed:
        print 'BAD TRADE'
    BTCneed = NMCneed*float(NBdata[3])
    BTCavailable = float(GBdata[2])
    if BTCavailable>BTCneed:
        print 'BAD TRADE 2'
    GHSsell = BTCneed/float(GBdata[1])
    print GHSsell-GHSbuy
#This while identify possible profit. Use place_order API to place orders.
    time.sleep(5)
