import os
from config import LOCAL_DB


def global_init():
   global __factory
   if __factory:
       return

   if 'DATABASE_URL' in os.environ:
       conn_str = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql://')
   else:
       conn_str = LOCAL_DB

   engine = sa.create_engine(conn_str, echo=False)
