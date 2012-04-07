# coding: utf-8

from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

faces = Table('faces', metadata,
		Column('id', Integer, primary_key=True)
