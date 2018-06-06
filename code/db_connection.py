import pymongo
from pymongo import errors
from pymongo import MongoClient
import errno
import ast


class DBConnection:
    mongo_info = 'mongodb://localhost:27017/'
    db_name = 'verificacion'
    query_result = []
    indice = 0

    def __init__(self):
        self.client = MongoClient(
            self.mongo_info, serverSelectionTimeoutMS=5000)
        self.db = self.client[self.db_name]

    def save_in_database(self, word, times):
        try:
            output_id = None
            if not self.is_in_database(word):
                # output_id = self.db.verificacion.insert_one(
                  #  {word: times}).inserted_id
                output_id = self.db.verificacion.insert_one(
                    {"name": word, "time": times}).inserted_id

            else:
                item = self.db.verificacion.find_one({'name': word})

                id = item.get("_id")
                new_times = item.get("time")

                self.db.verificacion.update_one(
                    {'_id': id}, {"$set": {"name": word, "time": new_times + times}}, upsert=True)
                output_id = id
                # mostrar en el html
                # db.verificacion.find().sort({time: -1})

            return output_id

        except errors.ConnectionFailure as e:
            print "Something went wrong: " % e
            return e

    def delete_database(self):
        return self.db.verificacion.remove()

    def is_in_database(self, name):
        if type(name) is str:
            element = self.db.verificacion.find(
                {'name': name}).count()

            # db.verificacion.find({'name':{'vaca':{'$exists': true}}}).count()
            print element
            return (element is not 0)
        else:
            return errno.EINVAL

    def get_all_data_from_database(self):
        print "a"
        # db.verificacion.find().sort({time: -1})
        cursor = self.db.verificacion.find().sort("time",  -1)
        # dictWords = dict()
        listWords = list()
        for element in cursor:
            # dictWords[element.get("name").encode("ascii")
            #           ] = element.get("time")
            # print element
            listWords.append(
                (element.get("name"), element.get("time")))
        return listWords

    def mongodb_conn(self):
        try:
            self.client.server_info()  # force connection on a request as the
            # connect=True parameter of MongoClient seems
            # to be useless here
            return 1
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print "Could not connect to server: %s" % err
            # do whatever you need
            return None
