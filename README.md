<h1 align='center'><em>Fast Zero</em> em: Listas To-do's :zap::spiral_notepad:</h1>

<div align='center'>
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi">
<img alt="Postgres" src="https://img.shields.io/badge/postgres-%23316192.svg?logo=postgresql&logoColor=white">
<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white">
<img alt="Creative Commons License" src="https://img.shields.io/badge/License-Creative%20Commons-white">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/amanmdest/fast_zero_sync?color=orange">
</div>
<br>
<p align='center'>>>> <q>O simples bem feito!</q> <<<</p>
<p align='center'>API desenvolvida no curso <a href="https://fastapidozero.dunossauro.com/">FastAPI do Zero</a> do maravilhoso @Dunossauro, professor de Python e também em muito mais do que se permeia o mundo computacional.</p>

## Proposta do Curso | Fast-Zero 

Tendo como foco o FastAPI, o curso traz em sua bagagem um panorama abrangente - e também pontual - atráves de conceitos, práticas e ferramentas de desenvolvimento e produção: cobertura completa de testes, deploy com a plataforma Fly.io e também um workflow automatizado de Integração Contínua(CI) com GitHub Actions.

Fast-zero como foi apelidada nossa API, lida com o cadastro, autenticação e autorizações de usuários que podem criar, editar e deletar suas respectivas notas 'To-do'(que possuem 5 estados possíveis: 'draft'= rascunho, 'todo'= para fazer, 'doing'= fazendo, 'done'= feito, 'trash'= descarte).

O conteúdo do curso se encontra gratuito em texto/livro e também em vídeo-aulas disponíveis no [canal do Duno](https://www.youtube.com/playlist?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP).
## Bibliotecas | Ferramentas
- [Python 3.12.4](https://www.python.org/downloads/release/python-3124/) -> Versão Python utilizada.
- [Fastapi 0.111.0](https://fastapi.tiangolo.com/) -> Web Framework de alto desempenho para construir API's com Python.
- [Uvicorn 0.31.1](https://www.uvicorn.org/) -> Servidor ASGI.
- [SQLAlchemy 2.0.35](https://docs.sqlalchemy.org/en/20/) -> Biblioteca open-source com Toolkit de SQL e Object Relational Mapper(ORM).
- [Pydantic 2.9.2](https://github.com/pydantic/pydantic/releases/tag/v2.9.2) -> Validação de dados e alguns gerenciamentos de configuração.
- [Alembic 1.13.3](https://alembic.sqlalchemy.org/en/latest/) -> Ferramenta de migração de banco de dados.
### 🛠️ Dependências Desenvolvimento:
- [Poetry 1.8.4](https://python-poetry.org/docs/#zsh) -> Gerenciador de pacotes do Python (usado para configurar o ambiente).
- [Taskipy 1.13.0](https://pypi.org/project/taskipy/) -> Executor de tarefas para projetos python.
- [Ruff 0.5.7](https://docs.astral.sh/ruff/) -> Formatador e Linter Python extremamente rápido, escrito em Rust.
- [ignr 2.2](https://pypi.org/project/ignr/) -> Plugin para gerar um arquivo .gitignore baseado na linguagem que voce definir.
- [PyJWT 2.9.0](https://pyjwt.readthedocs.io/en/stable/) -> Autenticador entre duas partes, por meio de um token assinado que segue o padrão(RFC-7519)
- [pwdlib 0.2.1](https://pypi.org/project/pwdlib/) -> auxiliar moderno p/ hashing de passwords
- [psycopg-binary 3.2.3](https://pypi.org/project/psycopg-binary/)  -> Adaptador de PostgreSQL para Python.
### 🧪 Dependências Testes:
- [Pytest 8.3.3](https://docs.pytest.org/en/stable/index.html) -> Testes simples e poderosos com Python.
- [Pytest-Cov 5.0.0](https://pytest-cov.readthedocs.io/en/latest/) -> Um plugin para produzir relatórios de cobertura de testes.
- [Factory-boy 3.3.1](https://factoryboy.readthedocs.io/en/latest/) -> Uma biblioteca que permite criar objetos de modelo de teste de forma rápida e fácil.
- [Freezegun 1.5.1](https://github.com/spulec/freezegun) -> Uma biblioteca que permite "congelar" o tempo em um ponto específico ou avançá-lo conforme necessário durante os testes.
- [Testcontainers 4.8.2](https://github.com/testcontainers) -> Facilita o uso de contêineres Docker para testes funcionais e de integração.
## Rode localmente
1. Clone o Repositório:
```bash
  git clone https://github.com/amanmdest/fast_zero_sync
```
2. Ative a máquina virtual e instale dependências:
```bash
  poetry shell
  poetry install
```
3. Para rodar o projeto junto ao banco de dados postgres é necessário criar um arquivo .env na raiz do projeto como o do exemplo abaixo:
```bash
  .env
  DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
  SECRET_KEY="8bf15dc4b43e98a24f62891ebf090e6839d99bce6c669de759706a243ef73737" # token_hex
  ALGORITHM="HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES=30
  
  POSTGRES_USER=app_user
  POSTGRES_DB=app_db
  POSTGRES_PASSWORD=app_password
```
4. Buildar a imagem e criar/iniciar o conteiner da aplicação junto ao banco de dados (necessário instalar [docker-compose](https://docs.docker.com/compose/install/)):
```bash
  docker compose up --build
```
Ou para rodar o projeto de forma limitada no servidor local Uvicorn sem banco de dados:
```bash
  task run
```
e acesse: http://127.0.0.1:8000/docs
## Imagens
![DER](imagens/fast_zero_DER.png)
*Diagrama Entidade-Relacionamento*

![HTML_COV](imagens/fast_zero_coverage.png)
*Coverage - cobertura de testes do projeto*

![endpoints/ rotas](imagens/fast_zero_endpoints.png)
*Endpoints/ rotas da API*
