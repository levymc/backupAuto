# backupAuto

# Script de Backup Automático de Arquivos .db

Este script em Python permite que você faça backups automáticos de arquivos .db de duas pastas para uma pasta específica. As bibliotecas utilizadas são **os**, **shutil** e **datetime**.

## Instruções

Para usar o script, siga estas etapas:

1. Edite o código-fonte para especificar o caminho para as pastas de origem e a pasta de destino.
2. Salve o arquivo com a extensão .py.
3. Configure o agendador de tarefas do sistema operacional para executar o script automaticamente em intervalos regulares.

## Como Funciona

O script faz o seguinte:

1. Obtém a data atual.
2. Cria uma nova pasta na pasta de destino com a data atual como nome.
3. Copia os arquivos .db das pastas de origem para a nova pasta na pasta de destino.

## Exemplo de Uso

```python
import os
import shutil
import datetime

# Especifica as pastas de origem e a pasta de destino
pasta_origem_1 = '/caminho/para/pasta/origem/1'
pasta_origem_2 = '/caminho/para/pasta/origem/2'
pasta_destino = '/caminho/para/pasta/de/destino'

# Obtém a data atual
data_atual = datetime.date.today()

# Cria uma nova pasta na pasta de destino com a data atual como nome
pasta_backup = os.path.join(pasta_destino, data_atual.strftime('%Y-%m-%d'))
os.makedirs(pasta_backup)

# Copia os arquivos .db das pastas de origem para a nova pasta na pasta de destino
for arquivo in os.listdir(pasta_origem_1):
    if arquivo.endswith('.db'):
        shutil.copy(os.path.join(pasta_origem_1, arquivo), pasta_backup)
for arquivo in os.listdir(pasta_origem_2):
    if arquivo.endswith('.db'):
        shutil.copy(os.path.join(pasta_origem_2, arquivo), pasta_backup)
