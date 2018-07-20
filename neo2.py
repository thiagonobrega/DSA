#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 08:34:53 2018

@author: thiagonobrega
"""
from py2neo import Graph
graph = Graph(auth=('neo4j', 't0t4l.'))
graph.delete_all()

#from model.mm import Person
#alice = Person()
#alice.name = "Alice Smith"
#graph.push(alice)
#graph.create(alice)
#alice.__ogm__.node

from model.infra import OS,Server

#rw = OS()
#rw.guest_os = "windows"
#rw.virtualization_tech = "VMWare 5"

rw = OS(gos="windows",vtech="VMWare 5")
graph.push(rw)

graph.push(OS(gos="Debian",vtech="Docker 2"))

s1 = Server(name="Server 1",ip="192.168.54.1",ios=rw)
#rw.servers.add(s1)
graph.merge(s1)

#graph.push(s1)


#
#r1 = RunningIn(s1,rw)
#graph.merge(r1)
#r2 = InstalledIn( rw.__ogm__.node, s1.__ogm__.node)
#graph.merge(r2)

#Relationship(s1, "HAS_OS", rw)
#Relationship(rw, "WAS_INSTALLED", s1)

#from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
#from db.types import GraphLabel, GraphRelationship


#class Actor(GraphObject):
#    acted_in_movies = RelatedTo(Movie, ActedIn)
    
#class Movie(GraphObject):
#    name = Property()
#    actors = RelatedFrom(Actor, ActedIn)

#class ActedIn(GraphRelationship):
#   year = Property()