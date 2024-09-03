```python
# Criar e ativar o ambiente virtual
deactivate  # se o ambiente actual estiver activado
rm -r env
virtualenv env
source env/bin/activate # Comando 'deactivate' para desativar o ambiente
which pip # Verifica o caminho do pip para garantir que está usando o ambiente virtual
# Util para instalar as dependências do projeto listadas no arquivo requirements.txt
pip install -r requirements.txt
export FLASK_APP=run.py
```