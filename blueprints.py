from sqlalchemy import select
from flask import Blueprint, make_response, render_template
from core import async_session, engine
from model import User

main_bp = Blueprint('main', __name__, url_prefix='/')

@main_bp.route('/')
async def main() -> str:
    async with async_session() as session:
        stmt = select(User)
        query = await session.execute(stmt)
        result = query.all()
        print([x[0].name for x in result])
    return render_template('index.html', users=result)

@main_bp.get('/person/<string:name>')
async def person_get(name: str):
    async with async_session() as session:
        stmt = select(User).where(User.username == name)
        query = await session.execute(stmt)
        result = query.scalar()
        if result is None:
            return 'not found', 404
    return {'name': result.name, 'id': result.id}

@main_bp.post('/person/')
async def person_post():
    req = resquest.get_json()
    async with async_session() as session:
        session.add(User(name=req.get('name', None)))
        await session.commit()

    return 'created', 201