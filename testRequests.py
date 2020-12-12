#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:10:03 2020

@author: y4
"""

import requests
import time
import random

for x in range(1):
    x = requests.post("https://pagead2.googlesyndication.com/pcs/activeview?xai=AKAOjsuGRTt_6bncT8b4q8oyKfrq281KRAA1B89SPphM13YPBxITGkHGbm_IxGc6ksS3VD_3etslgBA1hEKnDu-0nNokQO57I73A8mc-xqbUB6lb0C3CuE304Ro&sai=AMfl-YSRyEyN_z0o7iuGaiek948RaXoQ_a4mQSaUDAs0P82fnVSLhLvc0uMs1cLA2y8JP9Kv4oLREN6yA1VQ8rjGCvPS03JDWTvojc7FTlWntVm4YHHIQM2UhsORkphAkNbO0uzz&sig=Cg0ArKJSzMpJdTikRcIQEAE&adk=3205039840&tt=-1&bs=0%2C0&mtos=0,0,0,1019,8786&tos=0,0,0,1019,7767&p=872,418,1122,1388&mcvt=1019&rs=3&ht=0&tfs=568&tls=9354&mc=0.31&lte=-1&bas=0&bac=0&if=1&met=mue&la=1&avms=nio&niot_obs=466&niot_cbk=468&md=2&btr=0&cpmav=0&lm=2&rst=1606591869449&dlt=27&rpt=3862&isd=0&msd=0&xdi=0&postrxl=1&ps=-12245933%2C-12245933&scs=1920%2C1080&pt=-1&bin=4&deb=1-0-0-88-3-87-87-0-0-0&tvt=9353&is=970%2C250&iframe_loc=https%3A%2F%2Fad7d7422533ddd250cce73001f120697.safeframe.googlesyndication.com%2Fsafeframe%2F1-0-37%2Fhtml%2Fcontainer.html&r=v&id=osdim&vs=4&uc=88&upc=1&tgt=DIV&cl=1&cec=1&wf=0&cac=1&cd=968x248&itpl=21&v=20201118",data={
        "authority": "pagead2.googlesyndication.com",
        "method": "GET",
        "path": '/pcs/activeview?xai=AKAOjsuGRTt_6bncT8b4q8oyKfrq281KRAA1B89SPphM13YPBxITGkHGbm_IxGc6ksS3VD_3etslgBA1hEKnDu-0nNokQO57I73A8mc-xqbUB6lb0C3CuE304Ro&sai=AMfl-YSRyEyN_z0o7iuGaiek948RaXoQ_a4mQSaUDAs0P82fnVSLhLvc0uMs1cLA2y8JP9Kv4oLREN6yA1VQ8rjGCvPS03JDWTvojc7FTlWntVm4YHHIQM2UhsORkphAkNbO0uzz&sig=Cg0ArKJSzMpJdTikRcIQEAE&adk=3205039840&tt=-1&bs=0%2C0&mtos=0,0,0,1019,8786&tos=0,0,0,1019,7767&p=872,418,1122,1388&mcvt=1019&rs=3&ht=0&tfs=568&tls=9354&mc=0.31&lte=-1&bas=0&bac=0&if=1&met=mue&la=1&avms=nio&niot_obs=466&niot_cbk=468&md=2&btr=0&cpmav=0&lm=2&rst=1606591869449&dlt=27&rpt=3862&isd=0&msd=0&xdi=0&postrxl=1&ps=-12245933%2C-12245933&scs=1920%2C1080&pt=-1&bin=4&deb=1-0-0-88-3-87-87-0-0-0&tvt=9353&is=970%2C250&iframe_loc=https%3A%2F%2Fad7d7422533ddd250cce73001f120697.safeframe.googlesyndication.com%2Fsafeframe%2F1-0-37%2Fhtml%2Fcontainer.html&r=v&id=osdim&vs=4&uc=88&upc=1&tgt=DIV&cl=1&cec=1&wf=0&cac=1&cd=968x248&itpl=21&v=20201118',
        "scheme": "https",
        "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "referer": "https://ad7d7422533ddd250cce73001f120697.safeframe.googlesyndication.com/safeframe/1-0-37/html/container.html",
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400"
    })
    time.sleep(1)

print(x)