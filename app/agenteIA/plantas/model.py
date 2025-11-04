from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

# Creación del modelo para obtener una respuesta tipo instancia de planta por parte del LLM

class EmbarazoChoices(str, Enum):
    SI = "Su empleo es seguro"
    NO = "Su empleo no está recomendado"
    BPM = "Bajo prescripción médica"
    
class LactanciaChoices(str, Enum):
    SI = "Su empleo es seguro"
    NO = "Su empleo no está recomendado"
    BPM = "Bajo prescripción médica"
    

class EdadChoices(str, Enum):
    _0 = "Cero meses"
    _2 = "Dos años"
    _3 = "Tres años"
    _4 = "Cuatro años"
    _6 = "Seis años"
    _10 = "Diez años"
    _12 = "Doce años"
    _16 = "Dieciséis años"
    _18 = "Dieciocho años"
    

class Planta(BaseModel):
    """ Modelo de datos para una planta medicinal."""
    nombre: str = Field(..., description="Nombre común de la planta")
    droga: str = Field(..., description="Parte empleada de la planta para usos medicinales")
    especie: str = Field(..., description="Nombre científico de la planta")
    posologia: str = Field(..., description="Cantidad de droga diaria recomendada")
    dosis_efectiva: int = Field(..., description="Dosis efectiva de la droga en mg")
    activos: str = Field(..., description="Principios activos presentes en la planta")
    mecanismo: str = Field(..., description="Mecanismo de acción de la planta")
    contraindicaciones: Optional[str] = None
    interacciones: Optional[str] = None
    embarazo: EmbarazoChoices = EmbarazoChoices.NO
    lactancia: LactanciaChoices = LactanciaChoices.NO
    edad: EdadChoices = EdadChoices._12
    descripcion: str = Field(..., description="Descripción de la planta")
    usos: str = Field(..., description="Usos de la planta")
    