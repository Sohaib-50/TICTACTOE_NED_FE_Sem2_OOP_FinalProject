#!/usr/bin/python
#-*- coding: utf-8 -*-
EMPTY = None

class Cell:
    def __init__(self, coordinates):
        self.marker = EMPTY
        self.__coordinates = coordinates

    def getCoordinates(self):
        return self.__coordinates

    def setMarker(self, marker):  # TODO: make marker a PROPERTY
        self.marker = marker

    def __repr__(self):
        return f"<Cell; Coordinates={self.__coordinates}, Marker={self.marker}>"


c = Cell((0,0))
print(c)
d = Cell((0,1))
print(d)
print(d.getCoordinates())
d.setMarker("X")
print(d)
