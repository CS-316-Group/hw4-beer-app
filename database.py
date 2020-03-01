from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_string =  "postgres://vcm:example@vcm-13360:5432/production"
db = create_engine(db_string)



# for the code above once we have created our
# hardcoded database we can ran different commands 
# on it like the code below.

#result = db.execute("SELECT * FROM artists WHERE artist_name = 'Justin Beiber'")
#for r in result:
#    print(r)
#    print(r)