# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os
import json
s = socket.socket()
host = '10.102.13.145'
port = 5000
s.bind((host, port))
s.listen(5)

# Gets the Core Temperature from Pi
core_temperature = os.popen('vcgencmd measure_temp').readline()
# Initialising JSON object string
ini_string = f'{{"Temperature": "{core_temperature.strip()}"}}'
# Converting string to JSON
f_dict = eval(ini_string)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Fetching additional vcgencmd values
    cpu_clock_freq = os.popen('vcgencmd measure_clock arm').readline()
    gpu_clock_freq = os.popen('vcgencmd measure_clock core').readline()
    memory_usage = os.popen('vcgencmd get_mem arm').readline()
    core_voltage = os.popen('vcgencmd measure_volts core').readline()

    # Adding new values to the JSON object
    f_dict["CPU Clock Frequency"] = cpu_clock_freq.strip()
    f_dict["GPU Clock Frequency"] = gpu_clock_freq.strip()
    f_dict["Memory Usage"] = memory_usage.strip()
    f_dict["Core Voltage"] = core_voltage.strip()

    # Converting dictionary to JSON string
    res_json = json.dumps(f_dict)
    res_bytes = bytes(res_json, 'utf-8')  # Needs to be a byte
    c.send(res_bytes)  # Sends data as a byte type
    c.close()

