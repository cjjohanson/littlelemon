# littlelemon

API endpoints to test:
1. To view all restaurant bookings: /restaurant/bookings/
2. To add a table reservation: /restaurant/bookings/tables/
3. To view all menu items or create a new menu item: /restaurant/menu/items
4. To view, create, update, or delete a particular menu item: /restaurant/menu/items/{itemID}
5. To register a new user: POST /auth/users/
6. To login as a user: POST /auth/token/login/ (this endpoint gives you a bearer token)
7. To logout from a user: POST /auth/token/logout/