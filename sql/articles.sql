CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    url TEXT,
    article TEXT,
    article_embeddings VECTOR(1536)
);