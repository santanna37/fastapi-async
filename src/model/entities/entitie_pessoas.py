from src.model.settings.db_metadada import metadata
from sqlalchemy import Table, Column, Integer, String

#Descrever tabelas 

Pessoas = Table(
    "pessoas", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)
