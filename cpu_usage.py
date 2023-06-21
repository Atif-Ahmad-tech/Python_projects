import psutil
import os
def check_usage(percent):
    usage=psutill.cpu_percent()
    return usage < percent
if not check_usage(75):
    print("ohh cpu is overloaded")
else:
    print("everything i fine")
