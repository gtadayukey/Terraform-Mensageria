# Terraform Mensageria

Projeto desenvolvido para a disciplina de Computação em Nuvem, com foco em sistemas distribuídos, infraestrutura como código e comunicação entre processos.

## 📌 Descrição

Este projeto tem como objetivo a criação de uma arquitetura em nuvem escalável e automatizada, utilizando tecnologias modernas para provisionamento de infraestrutura e comunicação entre componentes distribuídos. A proposta envolve a construção de uma aplicação baseada em micro-serviços ou cliente-servidor, com ênfase em desempenho, escalabilidade e monitoramento.

## 🧰 Tecnologias Utilizadas

- **Provisionamento de Infraestrutura**: AWS CloudFormation e/ou Terraform  
- **Comunicação**: gRPC, Middleware de mensageria ou Sockets (TCP/UDP)  
- **Orquestração de Serviços**: _[especificar, se aplicável]_  
- **Monitoramento/Logs**: _[CloudWatch, Prometheus, etc., se aplicável]_  

## 🎯 Objetivos

- Projetar uma arquitetura de nuvem com suporte a sistemas distribuídos.
- Automatizar a criação da infraestrutura utilizando ferramentas IaC.
- Implementar comunicação entre serviços de forma eficiente e paralela.
- Documentar, testar e demonstrar aspectos de escalabilidade e tolerância a falhas.

## 📦 Estrutura do Projeto

```
/api/
    /painel/
        /static/
            scripts.js
            style.css
        /templates/
            index.html
        app.py
        init.py
    Dockerfile
/proto/
    /terraform/
        main.tf
        vars.tf
    messaging.proto
/server/
    Dockerfile
    client.py
    consumer.py
    messaging_pb2.py
    messaging_pb2_grpc.py
    poetry.lock
    pyproject.toml
    server.py
.gitignore
docker-compose.yml
README.md
```

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```

2. Configure as variáveis de ambiente e credenciais (AWS CLI ou similar).

3. Provisione a infraestrutura:
   ```bash
   terraform init
   terraform apply
   # ou
   aws cloudformation deploy --template-file template.yaml --stack-name nome-do-stack --capabilities CAPABILITY_NAMED_IAM
   ```

4. Execute os serviços localmente ou por meio de containers (se aplicável).

## ✅ Testes

- Testes automatizados e manuais foram realizados para validar:
  - Comunicação entre os serviços
  - Resiliência à falhas
  - Escalabilidade básica

## 👥 Autores

- Guilherme Yokokura - [@github](https://github.com/gtadayukey)
- Carlos Egger - [@github](https://github.com/Carlos-Egger)