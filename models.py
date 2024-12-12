from pydantic import BaseModel

class PatientModel(BaseModel):
    id: str
    name: str
    current_city: str