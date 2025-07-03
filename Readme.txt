# Instructions to set up Python virtual environment and install dependencies

1. Create a virtual environment (recommended name: .venv):

    python3 -m venv .venv

2. Activate the virtual environment:
    - On macOS/Linux:
        source .venv/bin/activate
    - On Windows:
        .venv\Scripts\activate

3. Install required packages:

    pip install -r requirements.txt

4. Run the script:

    python sematic_search.py

# Requirements
See requirements.txt for the list of required packages.
 wget -r -np -l 1 -A html http://www.actualno.com/
 


 ## How to build Docker image 
cd images/postgres
docker build --no-cache -t philipapostolov/postgres:17.5-pgvector .


## This is the way how to start Docker compose file 
docker compose up -d


###enable new postgress extension
CREATE EXTENSION IF NOT EXISTS vector;

#Create TABLE articles

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    url TEXT,
    article TEXT,
    article_embeddings VECTOR(1536)
);
#start container with name ollama
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# start a particular model
docker exec -it ollama ollama pull nomic-embed-text

#test if it works

❯ curl http://localhost:11434/api/embeddings -d '{
  "model": "nomic-embed-text",
  "prompt": "Това е Новина от сайта на Актално"
}'
{"embedding":[-0.45627331733703613,0.37343624234199524,...]}
