
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from prompts import LLM_TEMPLATE
from model import Planta

import sys
import os

# Agregar la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitomanager.settings')

import django
django.setup()

from plantas.models import Planta as PlantaDB

llm=ChatOpenAI(temperature=0, model_name="gpt-5-nano")

prompt = PromptTemplate(
    input_variables=["question"],
    template=LLM_TEMPLATE
)

parser = PydanticOutputParser(pydantic_object=Planta)

chain = prompt | llm | parser
    

resultado = chain.invoke({"question": "Cola de caballo","format_instructions": parser.get_format_instructions()})
pydantic_planta = resultado
planta_db = PlantaDB.objects.create(**pydantic_planta.model_dump())