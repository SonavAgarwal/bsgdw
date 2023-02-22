from gpiozero import CPUTemperature

cpu = CPUTemperature()
print("CPU Temperature: " + str(cpu.temperature))

import subprocess

clockOutput = subprocess.check_output(['vcgencmd', 'measure_clock', 'arm'])
voltsOutput = subprocess.check_output(['vcgencmd', 'measure_volts', 'core'])
topOutput = subprocess.check_output(['mpstat'])

import json

outputObject = {
    "temp": str(cpu.temperature),
    "c": str(clockOutput),
    "v": str(voltsOutput),
    "top": str(topOutput),
}

outputJSON = json.dumps(outputObject)
print(outputJSON)