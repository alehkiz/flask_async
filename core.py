from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from config import BaseConfig

db = SQLAlchemy()

engine = create_async_engine(
        BaseConfig.SQLALCHEMY_DATABASE_URI,
        echo=False,
        poolclass=NullPool
    )
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession, 
)