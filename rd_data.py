#!/usr/bin/python3


def rd_data(nm):
    with open(nm) as f:
        conts = f.read()
        conts_int = [int(xe) for xe in conts.split()]
        return (conts_int)
