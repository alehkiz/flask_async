from flask import Flask
import asyncio
import time
from flask.cli import with_appcontext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from core import db
from model import User

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+asyncpg://alexandre:contato@localhost:5433/async'
engine = create_async_engine(
        app.config['SQLALCHEMY_DATABASE_URI'],
        echo=True,
        poolclass=NullPool
    )
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession, 
)


@app.route('/')
async def main():
    return ''

@app.get('/person/<string:name>')
async def person_get(name):
    async with async_session() as session:
        stmt = select(User).where(User.name == name)
        query = await session.execute(stmt)
        result = query.scalar()
        if result is None:
            return 'not found', 404
    return {'name': result.name, 'id': result.id}

@app.post('/person/')
async def person_post():
    req = resquest.get_json()
    async with async_session() as session:
        session.add(User(name=req.get('name', None)))
        await session.commit()

    return 'created', 201

app.run(host='0.0.0.0')

