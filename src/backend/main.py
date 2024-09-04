from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model import base, TableCompany
from connection import create, get_db, base
from schema import Company as com
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
base.metadata.create_all(bind=create)

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

current_company = None

@app.post("/postCompany", response_model=com)
async def PostCompany(company_model:com, db:Session=Depends(get_db)):
    
    if not re.match(EMAIL_REGEX, company_model.mail):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fromato del correo electronico no valido."
        )
    
    existing_company = db.query(TableCompany).filter(
        (TableCompany.company_user == company_model.company_user)|
        (TableCompany.mail == company_model.mail)
    ).first()
    
    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empresa ya registrada con emil o username"
        )
        
        
    new_company = TableCompany(**company_model.dict())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@app.get("/startSession/{company_user}/{pasw}")
async def GetCompany(company_user: str, pasw: str, db: Session = Depends(get_db)):
    existing_company_user = db.query(TableCompany).filter(
        TableCompany.company_user == company_user
    ).first()
    
    print(f"usuario ingresada: {company_user}")
    print(f"Contraseña almacenada: {pasw}")
    
    if not existing_company_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nombre de usuario no registrado"
        )
    
    
    
    if existing_company_user.pasw == pasw:
        global current_company
        current_company = company_user  # Guardar el usuario en la variable global
        return {"message": f"Inicio de sesión exitoso para {company_user}"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña incorrecta"
        )
