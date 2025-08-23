from sqlalchemy.orm import declarative_base, DeclarativeMeta
from typing import Type

Base: Type[DeclarativeMeta] = declarative_base()
