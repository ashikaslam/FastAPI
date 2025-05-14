from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id :int
    name: str
    origin:str

teas:List[Tea]=[]

@app.get("/")
def read_root():
    return {"message":"wellcome to my fast project"}

@app.get("/teas")
def get_teas():
 return teas

@app.post("/teas")
def add_tea(tea:Tea):
   teas.append(tea)
   return {"message":"suceesfully added"}

@app.put("/teas/{tea_id}")
def  update_tea(tea_id:int,updatee_tea:Tea):
   for index,tea in enumerate(teas):
      if tea.id == tea_id:
         teas[index]=update_tea
         return teas[index]
   return {'message': "not found"}

@app.delete("teas/{tea_id}")
def delete_tea(tea_id:int):
   for index,tea in enumerate(teas):
      if tea.id == tea_id:
         return teas.pop(index)
   return {'message': "not found"}