# -*- coding: utf-8 -*-
# @Date     : 2017/12/05 22:40
# @Author   : Veev
# @File     : SQLHelper.py


class SQLHelper(object):
    """
    SQL 帮助类
    """

    def __init__(self):
        pass

    def insert(self, table=None, columns=None, values=None):
        print('Sql insert')


if __name__ == '__main__':
    helper = SQLHelper()
    helper.insert()