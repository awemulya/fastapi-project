from sqlalchemy import MetaData, Table, Integer, String, DateTime, func, Column

metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("username", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$MKEr/nYM83CUD0GbdD0Qde9asArbSMvlpz85jwHnBnX5dqE3XWGjG",
        "disabled": False,
    }
}