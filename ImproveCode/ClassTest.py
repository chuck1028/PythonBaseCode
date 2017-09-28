# -*- coding:utf-8 -*-
# Author: Jason Lee


class SaveDataToServer(object):
    def getServerId(self):
        print('--- Get Server Id ---')


class Operation(object):
    def __init__(self):
        self.save_data_to_server = SaveDataToServer()

    def save_data(self):
        self.save_data_to_server.getServerId()

obj = Operation()
obj.save_data()