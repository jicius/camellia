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

from mongoengine import (Document, StringField, ListField, DateTimeField, IntField, connect)

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
    uid = StringField(required=True)
    name_cn = StringField(required=True)
    name_en = StringField(required=True)
    stock = IntField(required=True)
    comments_total = IntField(required=True)
    shop_dst = ListField(required=True)
    on_sale = IntField(default=1)               # 1:在售; 0:下架
    date = DateTimeField(default=datetime.date.today())

    meta = {
        'collection': 'tf_product_item'
    }


class ProductMaItem(Document):
    """ Ma 单品数据

    """
    uid = StringField(required=True)
    name_cn = StringField(required=True)
    name_en = StringField(required=True)
    month_sales = IntField(required=True)
    date = DateTimeField(default=datetime.date.today())

    meta = {
        'collection': 'tf_product_item_ma'
    }
