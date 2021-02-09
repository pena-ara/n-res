#!/usr/bin/env python

from os import system as s
from os import popen as po

c_res = po("xrandr | grep '*' | awk '{print$1}'").read().strip().split("x")
c_x_res = c_res[0]
c_y_res = c_res[1]

m = po("xrandr --listmonitors | grep '*'").read().strip().split(" ")
m = m[4]

xr = f"xrandr --output {m} --mode"
pn = "--panning"
sc = "--scale"

while True:
    s("clear")
    print("""
 ███╗   ██╗      ██████╗ ███████╗███████╗
 ████╗  ██║      ██╔══██╗██╔════╝██╔════╝
 ██╔██╗ ██║█████╗██████╔╝█████╗  ███████╗
 ██║╚██╗██║╚════╝██╔══██╗██╔══╝  ╚════██║
 ██║ ╚████║      ██║  ██║███████╗███████║
 ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚══════╝╚══════╝ by Nestero
 Tool sederhana untuk mengganti resolusi dengan skala xrandr""")

    print(f"""
 Resolusi :
 [0] Normal     ({c_x_res} x {c_y_res})
 [1] HD+        (1600 x 900)
 [2] Full HD    (1920 x 1080)
 [3] QHD / WQHD (2560 x 1440)
 [4] QHD+       (3200 x 1800)
 [5] UHD        (3840 x 2160)
 [6] Exit""")

    res = int(input("\nPilih Resolusi > "))

    if res == 0:
        s(f"{xr} {c_x_res}x{c_y_res} {pn} {c_x_res}x{c_y_res} {sc} 1x1")
    elif res == 1:
        s_x = 1600 / int(c_x_res)
        s_y = 900 / int(c_y_res)
        s(f"{xr} {c_x_res}x{c_y_res} {pn} 1600x900 {sc} {s_x}x{s_y}")
    elif res == 2:
        s_x = 1920 / int(c_x_res)
        s_y = 1080 / int(c_y_res)
        s(f"{xr} {c_x_res}x{c_y_res} {pn} 1920x1080 {sc} {s_x}x{s_y}")
    elif res == 3:
        s_x = 2560 / int(c_x_res)
        s_y = 1440 / int(c_y_res)
        s(f"{xr} {c_x_res}x{c_y_res} {pn} 2560x1440 {sc} {s_x}x{s_y}")
    elif res == 4:
        s_x = 3200 / int(c_x_res)
        s_y = 1800 / int(c_y_res)
        s(f"{xr} {c_x_res}x{c_y_res} {pn} 3200x1800 {sc} {s_x}x{s_y}")
    elif res == 5:
        s_x = 3840 / int(c_x_res)
        s_y = 2160 / int(c_y_res)
        s(f"{xr} {c_x_res}x{c_y_res} {pn} 3840x2160 {sc} {s_x}x{s_y}")
    elif res == 6:
        exit()
    else:
        print("Tak ada resolusi........")
