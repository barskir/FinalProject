#!/usr/bin/python

import xml.sax


class Point(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)
        
class KmlParser( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.coordinates = ""
        #the following variables should be used in class where there is a comment "TODO"
        self.polygonDic = {}
        self.polygon = {}
        self.pointDic = {}
        self.point = {}
        self.pointsList = []
        
    # Call when an element starts
    def startElementNS(self, tag, name, attrs):
        self.CurrentData = tag[1]
 
    #Call when an elements ends
    def endElementNS(self, tag, attrs):
        self.CurrentData = tag[1]
        if self.CurrentData == "Polygon":  
            
            self.splitTofloat(self.coordinates)
            
            self.polygonDic[self.name] = self.pointsList
            
            self.pointsList = []
        
        elif self.CurrentData == "Point":
            
            self.splitTofloat(self.coordinates)
            
            self.pointDic[self.name] = self.pointsList
            
            self.pointsList = []
            
        self.CurrentData = ""
        
 

    def characters(self, content):
        
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "Point":
            self.point = content
        elif self.CurrentData == "coordinates":
            self.coordinates = content
            
  
    def splitTofloat(self, templist):

        templist = self.coordinates.split(' ')
        templist = [k.split(',') for k in templist]
         
        for k in range(templist.__len__()):
            tempoint = []
            for j in range(2):
 
                tempoint.append(float(templist[k][j]))
     
            self.pointsList.append(tempoint)
        
        
              
              
    def parse_kml(self, filename):
    
        #create an XMLReader
        parser = xml.sax.make_parser()
        
        parser.setFeature(xml.sax.handler.feature_namespaces, 1)
    
        
        Handler = KmlParser()
        parser.setContentHandler( Handler )
       
        parser.parse(filename)   
    
    
    
    
    
#         print "***** polygons: *******" 
#         for key in Handler.polygonDic:
#             print key
#             print Handler.polygonDic[key]
#     
#         
#         print "***** points: *******" 
#         for key in Handler.pointDic:
#             print key
#             print Handler.pointDic[key]
#             
        return Handler.pointDic

