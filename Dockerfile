# Use a imagem oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos necessários para o container
COPY calculadora.py .
COPY teste_calc.py .

# Comando para executar a aplicação
CMD ["python", "calculadora.py"]
