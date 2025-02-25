import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

list_of_files = [
    'Embedding_Models_Comparison/.gitignore',
    'Embedding_Models_Comparison/README.md',
    'Embedding_Models_Comparison/requirements.txt',
    'Embedding_Models_Comparison/.env',
    'Embedding_Models_Comparison/config.yml',
    'Embedding_Models_Comparison/src/__init__.py',
    'Embedding_Models_Comparison/src/pipeline.py',
    'Embedding_Models_Comparison/src/utils/__init__.py',
    'Embedding_Models_Comparison/src/utils/embeddings.py',
    'Embedding_Models_Comparison/src/utils/retrieval.py',
    'Embedding_Models_Comparison/src/utils/evalutation.py',
    'Embedding_Models_Comparison/src/tests/__init__.py',
    'Embedding_Models_Comparison/src/tests/test_embeddings.py',
    'Embedding_Models_Comparison/src/tests/test_retrieval.py',
    'Embedding_Models_Comparison/notebooks/exploration.ipynb',
    'Embedding_Models_Comparison/notebooks/evaluation.ipynb',
    'Embedding_Models_Comparison/data/raw/',
    'Embedding_Models_Comparison/data/processed/',
    'Embedding_Models_Comparison/logs/athina_logs',
    'Embedding_Models_Comparison/logs/wandb_logs',
    'Embedding_Models_Comparison/docs/architecture.md',
    'Embedding_Models_Comparison/docs/setup.md'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory;{filedir} for the file {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f'Creting empty file: {filepath}')
    else:
        logging.info(f'{filename} is already exist')