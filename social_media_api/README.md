This Social Media API uses Django REST Framework with Token Authentication to handle user registration
login and profile access. Users can register via POST /api/accounts/register/, which creates an account 
and returns an authentication token, and log in via POST /api/accounts/login/ to receive a token for 
future requests. Authenticated users can access their profile using GET /api/accounts/profile/, providing 
the token in the Authorization header (Authorization: Token <your_token>). All requests with JSON 
payloads should include the Content-Type: application/json header, ensuring secure and authenticated 
access to user-specific operations.

The Social Media API provides endpoints for user registration, login, profile management, posts and 
comments. Users can register and obtain an authentication token, which must be included in the 
Authorization header for all protected endpoints. Authenticated users can create, view, update and delete 
their own posts and comments, while being prevented from modifying others’ content.
The API supports pagination and filtering for posts and comments, ensuring efficient data retrieval. All 
endpoints follow RESTful conventions and the included serializers validate input and enforce data 
integrity.
This setup enables a secure and maintainable backend ready for integration with front-end clients or 
mobile applications.

Users can manage their social connections with the follow system by sending POST requests to '/api/
accounts/follow/<user_id>/' to follow a user and '/api/accounts/unfollow/<user_id>/' to unfollow.
The feed endpoint at '/api/posts/feed/' returns posts from all users the current user follows, ordered
from newest to oldest. All endpoints require authentication via token in the Authorization header.
This setup ensures users can only interact with accounts they follow and provides a dynamic, personalized 
feed, while maintaining secure access control and efficient database queries.