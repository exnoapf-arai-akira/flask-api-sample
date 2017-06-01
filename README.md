
##Requirement
pip install flask
pip install peewee


##user.tsv

#uid	name	price	class¥n
001	apple	200	fruits¥n
002	banana	300	fruits¥n
003	cabbage	100	vegitables¥n


##import.py

import for user.tsv


##api.py

flask api application


##how to request
curl http://localhost:3000/getprice/<productname>
