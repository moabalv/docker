# Docker 

Este projeto é um exemplo simples de uma aplicação web containerizada com Docker, utilizando **Flask** como backend e **HTML/CSS** para o frontend. Ele permite o cadastro de usuários e demonstra o uso de containers para isolamento de dependências e execução do sistema.

---

## 👥 Integrantes

- Anny Alves
- Erik Diniz
- Iorran Lira
- Moab Alves

---

## 🧰 Pré-requisitos

- [Docker](https://www.docker.com/) 

---

## 🛠️ Como executar o projeto

1. Detro do repositório, construa a imagem Docker:
```bash
docker build -t flask-cadastro .
```

2. Rode o container:
```bash
docker run -d --name meu-cadastro -p 5000:5000 flask-cadastro
```

3. Acesse a aplicação no navegador:
```
http://localhost:5000
```
