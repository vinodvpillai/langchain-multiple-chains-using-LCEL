from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain.schema import StrOutputParser

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
llm = ChatOpenAI(api_key=os.environ.get('OPENAI_API_KEY'), temperature=0.5)

# Chain
chain1 = prompt1|llm|StrOutputParser()
chain2 = ({'country':chain1, 'entity': itemgetter('entity')}|prompt2|llm|StrOutputParser())

print(chain2.invoke({'game':'Cricket','entity':'food'}))