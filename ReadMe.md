# Simply's Discord bot
Create a .env with correct information.

## Additional requirements:
- Python3
- Postgresql database
- Discord server

## Install requirements
`pip3 install -r requirements.txt`

## Setup database
`psql -U simply -h localhost simply_discord_bot < src/database/create_db.sql`

## Run script in the background
`nohup python3 src/main.py &`
