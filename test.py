#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import sys
import bottle
from bottle.ext.mongo import MongoPlugin
import pymongo


class RedisTest(unittest.TestCase):
    def setUp(self):
        self.app = bottle.Bottle(catchall=False)
        plugin = MongoPlugin(uri="mongodb://127.0.0.1",
                             db="bottle", json_mongo=True)
        self.plugin = self.app.install(plugin)

    def test_with_keyword(self):
        @self.app.get('/')
        def test(mongodb):
            self.assertEqual(type(mongodb), pymongo.database.Database)
            self.assertTrue(mongodb)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x, y: None)

    def test_save(self):
        @self.app.get('/')
        def test(mongodb):
            mongodb.drop_collection("bottle")
            insert = {"lang": "python", "framework": "bottle"}
            collection = mongodb['bottle'].insert(insert)

            self.assertTrue(collection)
            self.assertEqual(mongodb['bottle'].count(), 1)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x,y: None)

    def test_get(self):
        @self.app.get('/')
        def test(mongodb):
            mongodb.drop_collection("bottle")
            insert = {"lang": "python", "framework": "bottle"}
            collection = mongodb['bottle'].insert(insert)

            try:
                connection = pymongo.MongoClient()
            except AttributeError:
                connection = pymongo.Connection()
            db = connection.bottle
            get = db.bottle.find_one({})

            self.assertTrue(get)
            self.assertEqual(get, mongodb['bottle'].find_one())
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET'}, lambda x,y: None)


class ReplicaSetTest(RedisTest):

    def setUp(self):
        self.app = bottle.Bottle(catchall=False)
        read_pref = pymongo.ReadPreference.SECONDARY
        plugin = MongoPlugin(uri="mongodb://127.0.0.1:27017,127.0.0.1:27018/?replicaSet=testReplSet",
                             db="bottle", json_mongo=True, read_preference=read_pref, w=2)
        self.plugin = self.app.install(plugin)
 

if __name__ == '__main__':
    unittest.main()
