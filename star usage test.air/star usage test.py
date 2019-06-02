# -*- encoding=utf8 -*-
__author__ = "Tina"

from airtest.core.api import *

auto_setup(__file__)

start_app("dk.tactile.lilysgarden")

wait(Template(r"1.png", record_pos=(-0.015, 0.174), resolution=(2960, 1440)))
sleep(2)
touch(Template(r"2.png", record_pos=(-0.005, 0.183), resolution=(2960, 1440)))
sleep(4)
while not exists(Template(r"3.png", record_pos=(-0.004, -0.154), resolution=(2960, 1440))):
    if exists(Template(r"110.png", record_pos=(-0.005, -0.171), resolution=(2960, 1440))):
        touch(Template(r"333.png", record_pos=(-0.005, 0.167), resolution=(2960, 1440)))
        sleep(2)
    if exists(Template(r"77.png", record_pos=(-0.002, 0.209), resolution=(2960, 1440))):
        touch(Template(r"78.png", record_pos=(-0.01, 0.208), resolution=(2960, 1440)))
        sleep(2)
    touch(Template(r"6.png", record_pos=(-0.429, 0.171), resolution=(2960, 1440)))
    sleep(3)
    if exists(Template(r"7.png", record_pos=(0.199, -0.082), resolution=(2960, 1440))):
        assert_exists(Template(r"8.png", record_pos=(0.202, -0.08), resolution=(2960, 1440)), "Action exists.")
        touch(Template(r"9.png", record_pos=(0.201, -0.082), resolution=(2960, 1440)))
        if exists(Template(r"23.png", record_pos=(-0.004, -0.154), resolution=(2960, 1440))):
            assert_exists(Template(r"24.png", record_pos=(-0.004, -0.154), resolution=(2960, 1440)),"Stars depleted.")
            home()
            b


        while exists(Template(r"10.png", record_pos=(0.449, -0.214), resolution=(2960, 1440))):
            touch(Template(r"11.png", record_pos=(0.449, -0.214), resolution=(2960, 1440)))
            sleep(3)
        while exists(Template(r"12.png", record_pos=(0.445, -0.215), resolution=(2960, 1440))):
            touch(Template(r"13.png", record_pos=(0.445, -0.215), resolution=(2960, 1440)))
            sleep(3)
        if exists(Template(r"14.png", record_pos=(0.002, 0.206), resolution=(2960, 1440))):
            assert_exists(Template(r"15 .png", record_pos=(0.002, 0.206), resolution=(2960, 1440)), "Star choice exists.")
            touch(Template(r"16.png", record_pos=(-0.151, 0.166), resolution=(2960, 1440)))
            sleep(2)
            assert_exists(Template(r"17.png", record_pos=(0.439, 0.183), resolution=(2960, 1440)), "Choice selected.")

            touch(Template(r"18.png", record_pos=(0.439, 0.184), resolution=(2960, 1440)))
            while exists(Template(r"19.png", record_pos=(0.449, -0.214), resolution=(2960, 1440))):
                touch(Template(r"20.png", record_pos=(0.449, -0.214), resolution=(2960, 1440)))
                sleep(3)
            while exists(Template(r"21.png", record_pos=(0.445, -0.215), resolution=(2960, 1440))):
                touch(Template(r"22.png", record_pos=(0.445, -0.215), resolution=(2960, 1440)))
                sleep(3)
if exists(Template(r"23.png", record_pos=(-0.004, -0.154), resolution=(2960, 1440))):
    assert_exists(Template(r"24.png", record_pos=(-0.004, -0.154), resolution=(2960, 1440)),"Stars depleted.")
    home()
