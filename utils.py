from core import db, engine, async_session
from model import User

async def create_all():
    async with engine.begin() as session:
        await session.run_sync(db.metadata.drop_all)
        await session.run_sync(db.metadata.create_all)

async def create():
    async with async_session() as session:
            async with session.begin():
                    session.add(User(name='José', username='jose', _password='secret'))
            await session.commit()
