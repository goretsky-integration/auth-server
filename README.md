# Dodo Auth (Goretsky Integration)
You can see visualization [here](docs/schema.png)

This service provides regular cookies and tokens update, which are stored in redis and used later.

### Usage
Set up .env file. All required variables are listed in [.env.dist](.env.dist).

Run `update_cookies.py` in `src` folder to update cookies.

Run `update_tokens.py` in `src` folder to update tokens.
