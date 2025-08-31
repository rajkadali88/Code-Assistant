import os 
from langchain.docstore.document import Document 

def load_codebase(repo_path,extensions={'.py','.js','.ts'}):
    docs=[]
    for root,_,files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                with open(os.path.join(root,file),'r',encoding='utf-8') as f:
                    content = f.read()
                    docs.append(Document(page_content=content,metadata={'source':os.path.join(root,file)}))
    return docs 