from sqlalchemy import String, ForeignKey, Column
from connection import base
from sqlalchemy.orm import relationship


class TableCompany(base):
    __tablename__= "company"
    company_user = Column(String(30), primary_key=True, nullable=False)
    mail = Column(String(200), nullable=False)
    pasw = Column(String(50), nullable=False)