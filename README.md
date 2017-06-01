
Requirement
-----
    $ pip install flask  
    $ pip install peewee  


user.tsv
----
#uid	name	price	class  
001	apple	200	fruits  
002	banana	300	fruits  
003	cabbage	100	vegitables  


import.py
----
import to data.db from user.tsv 


api.py
----
    $ flask api application  
    $ python api.py


how to request
----
    $ curl http://localhost:3000/getprice/<productname>
