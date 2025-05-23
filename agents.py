from crewai import Agent ,LLM
from tools import tool
import os
from dotenv import load_dotenv
load_dotenv()
#call gemini models
llm=LLM(model="gemini/gemini-1.5-flash",
                            verbose=True,
                           temperature=0.5,
                           api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher=Agent(
    role="Senior Researcher",
    goal="unncover ground breaking technologies in {topic}",
    verebose=True,
    memory=True,
    backstory=(
        "Driven by the curosity,you are at the forefront of"
        "innovtion,eager to explore and share knowledge that could change"
        "the world"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
       "with a flair for simplifying complex topics,you craft"
       "engaging narratives that captivate and educate,bringing new "
       "discoveries to light in an accesible manner." 
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
    
    
    
) 