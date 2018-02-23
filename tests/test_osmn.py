#!/usr/bin/python
# coding: utf8
import geocoder

location = 'Rapperswil-Jona, Switzerland'


def test_osmn():
    g = geocoder.osmn(location, key='')
    assert g.ok


if __name__ == "__main__":
    test_osmn()
