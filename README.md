# Langchain Projects

I will keep track of my Langchain projects in this repository. I hope to create several projects leading, eventually leading to a large, scalable LLM project.

## ChatBot
I am using the Groq API for faster inference. I don't want to download Ollama or pay for OpenAI so this was an option I found helpful. I created a LLM project using Groq before and this allowed me to implement this
into this project. 
- ChatPromptTemplate creates a reponse based on the user-input prompt
- Streamlit allows for easy web deployment
- StrOutputParser outputs LLM result into top-likely string
- langchain allows for model chaining
