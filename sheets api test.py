#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:02:19 2020

@author: y4
"""


import getpass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = ServiceAccountCredentials.from_json_keyfile_dict({
  "type": "service_account",
  "project_id": "whatsapp-test-spam",
  "private_key_id": "3138a3ea03a4a1b66a6d367c53dd693976fe2df2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCkxqbKEU5Thlfr\n4u+IKvWPb2ddTxLoeH/5xQ1J/IFr5UTbUwR5GUzwBxRVLpK9sQj2XgpzyXaqXy0q\nuWal2A2x8eJZcUbgXVEvYOTq+ml5ffyOHsOfTsjyu3qP36sbyzxlQ3Ho4GFiLMoE\nEdDqF9NJlzW6pLYF5gE+IFUamn5pNzUQDQk205U2hgvx83zs9oTtWnK+7Dirbw9L\nciq2+EtMOUUQPBXyV+vJpjdKwFrE0oMAxI+GMh/iF35PDKYblZeY1OSGTP65AWgd\nxUEWCh19HiY/UOdJKch35k+ntetOjZkPzcw98lvIQSggruS0Znef8XPqsPKwG9V8\nIhgG++GzAgMBAAECggEARLjJNTt0hGdiYfIa3pq0Iadf382r4CLplP03JqVWQO61\nAhgkpHEF4pHBTCmJb+3XBBGCoHnksPfS+Z+rjP2H8LAmLBGPcuHYiz8JGmtn9BC0\ndX2lLtsH+hxw6HJrhcMEpGM1rd9vHif59SqNDCT1rRqQgRBTDjC4UfXgKKFImY6O\nY5uIhv6FhnGFYqOhwCHRqgTS04W1kq5Hr1R9He1M36XD14Mh75P5xRNlYuTgObcw\nbQHCjxqZBx4Rpe9H0GUjvU489q65jlQ4nQvsZXQNCwT8bIMNT5nfzIwAn3OMghtk\nxsmc8sl3ztc2reYCix34XuLbRJKy41MTwZESSwO3EQKBgQDXTTgRUog0mkda8zev\nBYme/LpxeR6idNJf2wNiC7fEtEuQ4ASXE15+7tNmfryL0glVAqRxNQtiSP7FvFye\nefHNMdiVNOdoQAe4gFcnSa7y2oJwjV7zwd58yRTnTJiDuGYJe3JUvJYH2dmoXD7I\nJYhYoHq2qCnAe7+xgk65MU5LWwKBgQDD7GrjW0xH8NGzg1PUPNQMKfpGjxFqCi5o\nL8JVXrgExbQSCsf/uKiyWYsiLzni6TzxExgYihq0QOMQyBo20ff4f1ZaCvCHmVFv\nsJGv8y7oXsxhaltIWZYipYnGbszuwAMQEc0pq52yXYzO6KGFswGRE6U2N6LD5FZh\nNF1VHKwKiQKBgAdFJ0CGfezwzLoIfnfdgwEoXY9ZXKx1r2jnN10HMkRlJiwVNHJ5\nh/ZXUDIk028RP5lsRmtANEs0Vc4Nhz8etQiNx1d6etntV5VmWAsOlObEdCUi0PMA\nN+gUzizlTD0ea+ukDH9KAvLu60ehHcmaYtlDSgGC+i3yv81ZrhjYzmEDAoGAJCxO\nP9PnbZDk5sPkglcIv4Ywkz5u9KkUkF/g/WoTh64I5RvgeTJa0zL9IT6e7WoqukfQ\nNxeofodMZRjM3jo+Ej9Qbid+6UpBYuGyxE2d54E5MvM0D1ObCKKPoXdrltkUt67R\ntlPdNcVX7gu9ZrX6IBMEedIj1w8dc6z7Xm+AxCECgYEApBX4Be1S3OuMi4IB3BaR\nEzNz8UKHcgtt9+7dCyWfuNpSePidNt2rkzKgbCqujTto3b4wTXmgqR47o3+tcVt0\nXDYTcV5yRmT6Eq2oc/NXpC2mf/nD5YloO2ydf/JcOA6MtPSooEhJMuQkrL136ZiK\nXYo5f8yTTgBd/uq2oSw8ccs=\n-----END PRIVATE KEY-----\n",
  "client_email": "connect@whatsapp-test-spam.iam.gserviceaccount.com",
  "client_id": "104792924967753601676",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/connect%40whatsapp-test-spam.iam.gserviceaccount.com"
})

gc = gspread.authorize(credentials)


sht1 = gc.open_by_key('1hwkWDvdVYsykSlRlRmLnreg6ROzeSRu4UmG3XOyX1wY')
values = sht1.values_get('A1:B1000')['values']
on = None
for x in values:
    if x[0] == getpass.getuser():
        if x[1] == '1':
            on = True
        else:
            on = False
if on == None:
    pos = 'A'+str(len(values)+1)+':B'+str(len(values)+1)
    sht1.values_append(range=pos,params={'valueInputOption':'RAW'}, body={'values':[[getpass.getuser(),'1']]})
    on = True