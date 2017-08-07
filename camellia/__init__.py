#!/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#   Copyright (C) 2017 Jicius
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime

from mongoengine import (Document, StringField, DictField, DateTimeField, IntField, ListField, connect)

from magnolia.config import config

# 连接mongodb
connect(
    config.mongo_cnf.get('db'),
    host=config.mongo_cnf.get('host'),
    port=config.mongo_cnf.get('port'),
    username=config.mongo_cnf.get('username'),
    password=config.mongo_cnf.get('password')
)


class ProductItem(Document):
    """ 单品数据

    """
    uid = StringField(required=True, unique=True)
    name_cn = StringField(required=True)
    name_en = StringField(required=True)
    shop_dsr = DictField(required=True)
    comments_total = IntField(required=True)
    stock_total = IntField(required=True)
    weekend_check = IntField(default=0)        # 0:非周末; 1:周末
    festival_check = IntField(default=0)       # 0:非假日; 1:假日
    sold_off = IntField(default=0)             # 1:在售; 0:下架
    ps_by_sales = ListField()                  # 1, 2, 3: 第1页第2行第3列
    time = DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'tf_product_item'
    }


class ProductMaItem(Document):
    """ ma 单品数据

    """
    uid = StringField(required=True, unique=True)
    name_cn = StringField(required=True)
    name_en = StringField(required=True)
    month_sale_total = IntField(required=True)
    time = DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'tf_product_item'
    }
