import json
from layers import *
from geometry import Envelope
########################################################################
class BaseMap(object):
    """
       Basemaps give the web map a geographic context. In the web map, the
       basemaps are held in an array of baseMapLayer objects. Typically,
       you will use one basemap layer that is drawn beneath all other
       layers, but you can also add a basemap layer on top of all other
       layers to depict boundaries, labels, or a road network.
    """
    _baseMapLayers = None
    _json = None
    _dictionary = None
    _title = None
    #----------------------------------------------------------------------
    def __init__(self, title, baseMapLayers=[]):
        """Constructor"""
        self._baseMapLayers = baseMapLayers
        self._title = title
    #----------------------------------------------------------------------
    @property
    def title(self):
        """ returns the title of the basemap  """
        return self._title
    #----------------------------------------------------------------------
    @title.setter
    def title(self, title):
        """ sets the new title """
        self._title = title
    #----------------------------------------------------------------------
    @property
    def baseMapLayers(self):
        """ returns a list of base map layers """
        return self._baseMapLayers
    #----------------------------------------------------------------------
    def addBaseMapLayer(self, baseMapLayer):
        """ adds a base map layer """
        if isinstance(baseMapLayer, BaseMapLayer):
            self._baseMapLayers.append(baseMapLayer)
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def removeBaseMapLayer(self, index):
        """ removes a basemap layer by index """
        if index > len(self._baseMapLayers):
            return False
        self._baseMapLayers.remove(self._baseMapLayers[index])
        return True
    #----------------------------------------------------------------------
    def __str__(self):
        """ returns the string JSON representation of the basemap """
        template = {
            "title" : self._title,
	    "baseMapLayers" : [ json.loads(str(l)) for l in self._baseMapLayers]
        }
        return json.dumps(template)
    #----------------------------------------------------------------------
    @property
    def asDictionary(self):
        """ returns the value as a dictionary """
        template = {
                    "title" : self._title,
                    "baseMapLayers" : [lyr.asDictionary for lyr in self._baseMapLayers]
                }
        return template
########################################################################
class Bookmark(object):
    """ A bookmark is a saved geographic extent that allows end users to
        quickly navigate to a particular area of interest.
    """
    _extents = None
    #----------------------------------------------------------------------
    @property
    def bookmarks(self):
        """ returns the bookmarks """
        if self._extents is None:
            self._extents = []
        return self._extents
    #----------------------------------------------------------------------
    def add(self, extent, name):
        """ adds an extent to the bookmarks object """
        bm = {}
        if isinstance(extent, Envelope):
            bm['extent'] = extent.asDictionary
            bm['name'] = name
            self._extents.append(
                bm
            )
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def remove(self, index):
        """ removes a bookmark via index location """
        if index <= len(self._extents) - 1:
            self._extents.remove(self._extents[index])
            return True
        else:
            return False
    #----------------------------------------------------------------------
    def __str__(self):
        """ returns string representation of the object """
        return json.dumps(self.__dict__())
    #----------------------------------------------------------------------
    @property
    def asDictionary(self):
        """ returns a dictionary representation of the object """
        return {"bookmarks" : self._extents}











