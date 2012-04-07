#!/usr/bin/env python3
# coding: utf-8

import clintonfaces
import pymongo
import bottle

clintonfaces.app.db = pymongo.Connection().clintonfaces
bottle.run(clintonfaces.app, host="0.0.0.0", port=8080)
