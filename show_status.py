# !/usr/bin/python3
# coding=utf-8

import os

def get_CPU_temp():
	with open("/sys/class/thermal/thermal_zone0/temp") as f:
	    temp = float(f.read().strip("\n"))/1000
	return "%3.1f " % temp


def get_CPU_use():
	return os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").read().strip("\n")


def get_GPU_temp():
	status = os.popen("/opt/vc/bin/vcgencmd measure_temp").read().strip("\n")
	return status.split("=")[1].replace("\'C", "")


def get_RAM_info():
	p = os.popen('free')
	i = 0
	while 1:
		i = i + 1
		line = p.readline()
		if i==2:
			return(line.split()[1:4])


def get_disk_space():
	p = os.popen("df -h /")
	i = 0
	while 1:
		i = i +1
		line = p.readline()
		if i==2:
			return(line.split()[1:5])


if __name__ == '__main__':
	(RAM_total, RAM_used, RAM_free) = get_RAM_info()
        (DISK_total, DISK_used, DISK_free, DISK_perc) = get_disk_space()
	print("""Current status:
\tCPU Temperature : %s\'C
\tCPU Use : %s%c\n
\tGPU Temperature : %s\'C\n
\tRAM Total : %.1fMB
\tRAM Used  : %.1fMB
\tRAM Free  : %.1fMB\n
\tDISK Total : %s
\tDISK Used  : %s
\tDISK Used  Percentage : %s """ % (get_CPU_temp(), get_CPU_use(), 0x25, get_GPU_temp(), float(RAM_total)/1000, float(RAM_used)/1000, float(RAM_free)/1000, DISK_total, DISK_used, DISK_perc))

