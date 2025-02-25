import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

list_of_files = [
    'src/__init__.py',
    'src/pipeline.py',
    'src/utils/__init__.py',
    'src/utils/embeddings.py',
    'src/utils/retrieval.py',
    'src/utils/evalutation.py',
    'src/tests/__init__.py',
    'src/tests/test_embeddings.py',
    'src/tests/test_retrieval.py',
    '.env',
    'notebooks/exploration.ipynb',
    'notebooks/evaluation.ipynb',
    'data/raw/',
    'data/processed/',
    'logs/athina_logs',
    'logs/wandb_logs',
    'docs/architecture.md',
    'docs/setup.md',
    'config.yml'
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