Views to test
admin user name:littlelemonadmin
admin password: lladmin123!
admin token mysql database: af34b65bfee08962dc4e75647e5f5c2058428cd0
admin token sqllite database:2830aa32fcac0e3c4e0059b3700230f690d92581
http://127.0.0.1:8000/restaurant/api/menu/ - URL for list of all menu items, need to have admin token to create menu items
http://127.0.0.1:8000/restaurant/api/menu/1 - URL for single menu item, need to have admin token to update or delete menu items


127.0.0.1:8000/auth/token/login/ - URL to generate token

http://127.0.0.1:8000/restaurant/api/booking/tables/ - URL for booking a table

Database is connected to MySQL on local host, which will not work when you open on another computer, left an option in settings.py to comment mysql database and use sqllite database that is included instead