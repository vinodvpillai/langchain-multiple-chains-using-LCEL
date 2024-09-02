from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Loading the environment variables
dotenv_path  = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Prompt
prompt1 = ChatPromptTemplate.from_template('Which country won the {game} world cup?')
prompt2 = ChatPromptTemplate.from_template('Suggest me the best {entity} of that {country}')

# Model 
llm = ChatOpenAI(api_key=os.environ.get('OPENAI_API_KEY'), model=os.environ.get('OPENAI_MODEL'), temperature=0.5) # type: ignore

# Parser
parser = StrOutputParser()

# Chain
chain1 = prompt1|llm|parser
chain2 = ({'country':chain1, 'entity': itemgetter('entity')}|prompt2|llm|parser)

print(chain2.invoke({'game':'Cricket','entity':'food'}))