#!/usr/env/python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

""" 
    Calculate the amount of cycles needed to encrypt a message with a specific length
    Taken from MBGHs PhD thesis
    https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/124591/eth-50525-02.pdf

    @input msg_len message length in bits
"""
def aegis_128l_cycles(msg_len):
    return 17 + math.ceil(msg_len/32)

def aegis_128_cycles(msg_len):
    return 17 + math.ceil(msg_len/16)

def aes_gcm_cycles(msg_len):
    return 12 + math.ceil(msg_len/16)

min_len = 0
max_len = 32*128
ran = range(min_len, max_len)
msg_lengths = [x for x in ran]

aegis_128_clocks = [aegis_128_cycles(x) for x in msg_lengths]
aegis_128l_clocks = [aegis_128l_cycles(x) for x in msg_lengths]
aes_gcm_clocks = [aes_gcm_cycles(x) for x in msg_lengths]

aegis_freq =  0.7246 #  724.6 MHz
aes_freq =  0.7937 #  793.7 MHz

# latencies are in ns
aegis_128_latency = [x/aegis_freq for x in aegis_128_clocks]
aegis_128l_latency = [x/aegis_freq for x in aegis_128l_clocks]
aes_gcm_latency = [x/aes_freq for x in aes_gcm_clocks]

# throughput in gbit/s
aegis_128_tp = [msg_lengths[x]/aegis_128_clocks[x]*aegis_freq for x in ran]
aegis_128l_tp = [msg_lengths[x]/aegis_128l_clocks[x]*aegis_freq for x in ran]
aes_gcm_tp = [msg_lengths[x]/aes_gcm_clocks[x]*aes_freq for x in ran]

plt.subplot(2, 1, 1)
plt.title('AEGIS latency and throughput vs message length')
plt.plot(ran, aegis_128l_latency)
plt.plot(ran, aes_gcm_latency)
# plt.xlabel('message len [bits]')
plt.ylabel('latency [ns]')
plt.legend(['AEGIS 128l', 'AES GCM'])
plt.subplot(2, 1, 2)
plt.plot(ran, aegis_128l_tp)
plt.plot(ran, aes_gcm_tp)
plt.xlabel('message len [B]')
plt.ylabel('throughput [gB/s]')
plt.savefig("aegis.pdf", bbox_inches='tight')
