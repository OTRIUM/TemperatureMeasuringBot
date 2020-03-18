""" DS18B20 Temperature Measuring Telegram Bot """

import sys, gc, api
from machine import Pin, Timer
from time import sleep

import onewire, ds18x20, time
ow = onewire.OneWire(Pin(2)) 
ds = ds18x20.DS18X20(ow)


telegram = api.TelegramBot('tgToken')

welcome_message = 'Welcome to Temperature Measuring Bot!\r\n' +\
                  'It uses DS18B20 sensor to measure the temperature\r\n' +\
                  'Use /temp command to make a request'

def message_handler(message):
    if message[2] == '/start':
        telegram.send(message[0], welcome_message)
    elif message[2] == '/temp':
        roms = ds.scan()
        ds.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            telegram.send(message[0], str(ds.read_temp(rom)) + ' degrees')
    elif message[2] == '/halt':
        telegram.send(message[0], 'Halt engaged!')
        telegram.update()
        sys.exit()
    gc.collect()   

sleep(5)

print('Bot Started!')
while True:
    telegram.listen(message_handler)