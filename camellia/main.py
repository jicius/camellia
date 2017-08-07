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

import sys
import random
import datetime

from camellia.models import (ProductItem, ProductMaItem)


class DoStart:
    def __init__(self, uid, name_cn, name_en):
        self.uid = uid
        self.name_cn = name_cn
        self.name_en = name_en

    def gen_product_item(self, days=30):
        [it.delete() for it in ProductItem.objects()]
        comments_total = 1000

        for day in range(days):
            comments_inc = random.randrange(0, 4)
            date = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime(format="%Y-%m-%d")
            ProductItem(
                uid=self.uid,
                name_cn=self.name_cn,
                name_en=self.name_en,
                stock=random.randrange(100, 500),
                comments_total=comments_total,
                shop_dst=[random.uniform(-0.03, 0.03), random.uniform(-0.03, 0.03), random.uniform(-0.03, 0.03)],
                on_sale=abs(comments_inc % 2),
                date=date
            ).save()
            comments_total -= comments_inc

    def gen_product_item_ma(self, days=30):
        [it.delete() for it in ProductMaItem.objects()]
        month_sales = 20000

        for day in range(days):
            date = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime(format="%Y-%m-%d")
            ProductMaItem(
                uid=self.uid,
                name_cn=self.name_cn,
                name_en=self.name_en,
                month_sales=month_sales + random.randrange(-500, 500),
                date=date
            ).save()


if __name__ == '__main__':
    uid = "98869838013"
    name_cn = u"手机"
    name_en = "phone"
    ds_cls = DoStart(uid=uid, name_cn=name_cn, name_en=name_en)
    ds_cls.gen_product_item()

