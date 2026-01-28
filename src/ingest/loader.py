import os
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter


class VaultLoader():

    def __init__(self, vault_path: str):
        self.vault_path=vault_path

    def gather(self):
        results=[]
        for path, subdirs, files in os.walk(self.vault_path):
            for name in files:
                if name.endswith(".md"):
                    results.append(os.path.join(path, name))
        return results
    
    def load(self) -> list[Document]:
        """Load all markdown files from the vault into LangChain documents."""
        documents = []
        markdown_files = self.gather()
        
        for file_path in markdown_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Create metadata from file path
                relative_path = Path(file_path).relative_to(self.vault_path)
                metadata = {
                    "source": str(relative_path),
                    "file_path": file_path
                }
                
                doc = Document(page_content=content, metadata=metadata)
                documents.append(doc)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        return documents

    def split(self):
        splits=[]
        documents=self.load()
        headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"), ("####", "Header 4")]
        text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        for doc in documents:
            sections = text_splitter.split_text(doc.page_content)
            splits.extend(sections)
        return splits
        