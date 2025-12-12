This Social Media API uses Django REST Framework with Token Authentication to handle user registration
login and profile access. Users can register via POST /api/accounts/register/, which creates an account 
and returns an authentication token, and log in via POST /api/accounts/login/ to receive a token for 
future requests. Authenticated users can access their profile using GET /api/accounts/profile/, providing 
the token in the Authorization header (Authorization: Token <your_token>). All requests with JSON 
payloads should include the Content-Type: application/json header, ensuring secure and authenticated 
access to user-specific operations.