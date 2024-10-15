# FastAPI em: **Listas To-do's** :spiral_notepad: - _"O simples bem feito!"_ 

<div align='center'>
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi">
<img alt="Postgres" src="https://img.shields.io/badge/postgres-%23316192.svg?logo=postgresql&logoColor=white">
<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white">
<img alt="MIT License" src="https://img.shields.io/badge/License-MIT-green.svg">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/amanmdest/fast_zero_sync?color=orange">
</div>
<br>
<p align='center'>API desenvolvida no curso <a href="https://fastapidozer.dunossauro.com/">FastAPI do Zero</a> do maravilhoso @Dunossauro, professor de todos nós em Python e também em muito mais do que se permeia o mundo computacional.</p>

## Proposta do Curso | Fast-Zero 

O curso traz em sua bagagem um panorama pontual - e também abrangente - que caminha por conceitos, práticas e ferramentas de desenvolvimento, testes e deploy com Python e FastAPI.

Fast-zero como foi apelidada nossa API, lida com o cadastro, autenticação e autorizações de usuários que podem criar, editar e deletar suas respectivas notas 'To-do'.

O conteúdo do curso se encontra _gratuito_ em texto/livro e também em vídeo-aulas disponíveis no [canal do Duno](https://www.youtube.com/playlist?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP).

## 🧰 Tools/ Ferramentas usadas neste Projeto
- Python 3.12
- Fastapi 0.111.0 -> Web Framework de alto desempenho para construir API's com Python.
- Uvicorn 0.31.1 -> Servidor ASGI.
- SQLAlchemy 2.0.35 -> Biblioteca open-source com Toolkit de SQL e Object Relational Mapper(ORM).
- Pydantic 2.8.2 -> Validação de dados e alguns gerenciamentos de configuração.
- Alembic 1.13.2 -> Ferramenta de migração de banco de dados.
### 🛠️ Dependências de Desenvolvimento:
- Poetry 1.8.4 -> Gerenciador de pacotes do Python (usado para configurar o ambiente).
- Taskipy 1.13.0 -> Executor de tarefas para projetos python.
- [Ruff 0.5.7](https://docs.astral.sh/ruff/) -> Formatador e Linter Python extremamente rápido, escrito em Rust.
- ignr 2.2 -> Plugin para gerar um arquivo .gitignore baseado na linguagem que voce definir.
- PyJWT 2.9.0 -> Autenticador entre duas partes, por meio de um token assinado que segue o padrão(RFC-7519)
- [pwdlib 0.2.1](https://pypi.org/project/pwdlib/) -> auxiliar moderno p/ hashing de passwords
- psycopg-binary 3.2.3  -> Adaptador de PostgreSQL para Python.
### 🧪 Dependências TDD:
- Pytest 8.3.3 (Criar testes simples e poderosos com Python)
- Pytest-Cov 5.0.0 (Um plugin para produzir relatórios de cobertura de testes)
- Factory-boy 3.3.1 (Uma biblioteca que permite criar objetos de modelo de teste de forma rápida e fácil.)
- Freezegun 1.5.1 (Um biblioteca que permite "congelar" o tempo em um ponto específico ou avançá-lo conforme necessário durante os testes)
- Testcontainers 4.8.2 (Facilita o uso de contêineres Docker para testes funcionais e de integração)
