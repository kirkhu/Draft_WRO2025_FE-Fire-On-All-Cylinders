#!/bin/bash

echo -n "Are You AP Name : "
read apname

if [[ "$apname" != "" ]]; then
    setapname="$apname"
else
    setapname="Linux-AP"
fi

echo -n "Are You AP Password : "
read appass

if [[ "$appass" != "" ]]; then
    setappass="$appass"
else
    setappass="1234567890"
fi

sudo nmcli dev wifi hotspot ifname wlan0 ssid "$setapname" password "$setappass"

sudo nmcli connection modify Hotspot connection.autoconnect yes

sudo systemctl enable NetworkManager.service

sudo systemctl status NetworkManager

echo -n "Are You Reboot Jetson Orin Nano ? (y/n) : "
read userinput

if [[ "$userinput" == "y" ||  "$userinput" == "Y" ]]; then
    echo "Rebooting Jetson Orin Nano......"
    sudo reboot
else 
    echo "Reboot cancelled."
fi