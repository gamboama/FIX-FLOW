from pydantic import BaseModel as bm

class Company(bm):
    company_user:str
    mail:str
    pasw:str