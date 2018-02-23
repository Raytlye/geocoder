#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging
import json

from geocoder.base import OneResult, MultipleResultsQuery


class OsmnResult(OneResult):

    def __init__(self, json_content):

        # proceed with super.__init__
        super(OsmnResult, self).__init__(json_content)

    # ============================ #
    # Geometry - Points & Polygons #
    # ============================ #

    @property
    def lat(self):
        lat = self.raw.get('lat')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.raw.get('lon')
        if lng:
            return float(lng)

    @property
    def bbox(self):
        _boundingbox = self.raw.get('boundingbox')
        if _boundingbox:
            south = float(_boundingbox[1])
            west = float(_boundingbox[0])
            north = float(_boundingbox[3])
            east = float(_boundingbox[2])
            return self._get_bbox(south, west, north, east)

    # ========================== #
    # Tags for individual houses #
    # ========================== #

    @property
    def address(self):
        print(self.raw.get('display_name'))
        return self.raw.get('display_name')

    @property
    def housenumber(self):
        try:
            return self.raw['housenumbers'][0]
        except IndexError:
            print('')

    @property
    def street(self):
        return self.raw.get('street')

    @property
    def city(self):
        return self.raw.get('city')

    @property
    def state(self):
        return self.raw.get('state')

    @property
    def country(self):
        return self.raw.get('country')


class OsmnQuery(MultipleResultsQuery):
    """
   OSMNames
    =========
    OSMNames is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://osmnames.org/api/
    """
    provider = 'osm'
    method = 'geocode'

    _URL = 'https://search.osmnames.org/q/'
    _RESULT_CLASS = OsmnResult
    _KEY_MANDATORY = True

    def _connect(self):
        self.url += self.location + '.js'
        return super()._connect()

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'key': provider_key,
            'format': 'json'
        }

    def _adapt_results(self, json_response):
        return json_response['results']

    def _before_initialize(self, location, **kwargs):
        """ Check if specific URL has not been provided, otherwise, use cls._URL"""
        url = kwargs.get('url', '')
        if url.lower() == 'localhost':
            self.url = 'http://localhost/osmnames'
        elif url:
            self.url = url
