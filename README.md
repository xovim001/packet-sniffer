# packet-sniffer

  Overview:
  ========
packet-sniffer is a comprehensive network packet sniffer and monitoring tool.It captures all the http packet (URL,USERNAME AND PASSWORD) sent through the network. Unfortunately,it does not work with https protocol yet. Once we able to bypass https, we will update the tool. To capture the packet, you have to be man in the middle or the target computer's network traffic has to flow through your device. 

Dependencies
========
 Python 2 and scapy module

 USAGE: 
========
Navigate to the folder and run the following command:

python sniffer.py -i(interface)
                OR
python sniffer.py --interface

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --targets TARGETS                   

Examples
========
python sniffer.py -i eth0
        OR
python sniffer.py --interface wlan0

Bugs & Contact
==============
Feel free to mail me with any problem, bug, suggestions or fixes at:
Sazzad Ovi <ovisecret@gmail.com>
