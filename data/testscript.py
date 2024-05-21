from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# Read text from file
def read_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


# LangChain model setup
llm = ChatOllama(model="phi3")
prompt = ChatPromptTemplate.from_template("{text}")

# Using LangChain Expressive Language chain syntax
chain = prompt | llm | StrOutputParser()

# Path to the file containing text
file_path = "test/cd.txt"
text = read_text_from_file(file_path)

# Invoke LangChain model with the text
print(text)
response = chain.invoke({"text": text})

# Print the response
print(response)
