from pymongo import MongoClient
from pymongo.database import Database

from conf.mongodb import mongodb_config


def get_mongo_clien():
    return MongoClient(mongodb_config.host, int(mongodb_config.port))


def get_mongo_db() -> Database:
    return get_mongo_clien()[mongodb_config.database]