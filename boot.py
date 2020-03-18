import network
import gc
gc.collect()

ssid = 'ssid'
password = 'pass'

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        pass

print('Connection successful')
print(sta_if.ifconfig())