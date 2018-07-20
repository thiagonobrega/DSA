#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:55:37 2018

@author: Thiago Nobrega
"""


from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
from py2neo.data import Relationship


class OS(GraphObject):
    __primarykey__ = "guest_os"
    #StringProperty(unique_index=True)
    guest_os = Property()
    virtualization_tech = Property()
    #server = RelatedFrom("Server", "ACTED_IN")
    #servers = RelatedTo(Server,"RUNNING_ON")
    
    def __init__(self,gos,vtech):
        self.guest_os = gos
        self.virtualization_tech = vtech

class Server(GraphObject):
    __primarykey__ = "name"

    name = Property()
    ip = Property()
    os = RelatedTo(OS,"INSTALED_OS")
    cpu_type = Property()
    cpu_count = Property()
    memory = Property()
    
    def __init__(self,name,ip,ios):
        self.name = name
        self.ip = ip
        self.os.add(ios)

    #RelatedTo(OS,relationship_type="HAS_OS")
    #Relationship(alice, "KNOWS", bob, since=1999)

    #acted_in = RelatedTo(Movie)
    #directed = RelatedTo(Movie)
    #produced = RelatedTo(Movie)
    #actors = RelatedFrom("Person", "ACTED_IN")
    #directors = RelatedFrom("Person", "DIRECTED")
    #producers = RelatedFrom("Person", "PRODUCED")
    #comments = RelatedTo("Comment", "COMMENT")

    def __lt__(self, other):
        return self.name < other.name