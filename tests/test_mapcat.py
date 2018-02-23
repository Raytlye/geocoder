#!/usr/bin/python
# coding: utf8
import geocoder

location = 'Ottawa'


def test_mapcat():
    g = geocoder.mapcat(location, key='')
    assert g.ok


if __name__ == "__main__":
    test_mapcat()
