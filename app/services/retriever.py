def retrieve_snipets(vectorstore,query,k):
    results = vectorstore.similarity_search(query,k=k)
    return "\n\n".join([doc.page_content[:1000] for doc in results])