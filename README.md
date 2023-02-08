# Flask Async

Aplicação utilizando async no flask e Sqlalchemy


![GitHub repo size](https://img.shields.io/github/repo-size/alehkiz/flask_async?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alehkiz/flask_async?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alehkiz/flask_async?style=for-the-badge)
![Github open issues](https://img.shields.io/github/issues/alehkiz/flask_async?style=for-the-badge)



### Melhorias futuras:

- [x] Modo assíncrono com Flask
- [x] Consultas assíncronas com SqlAlchemy
- [x] Crud para cadastro de usuários

## 💻 Pré-requisitos

* versão mais recente de `python`
* Utilize um ambiente virtual: https://docs.python.org/3/tutorial/venv.html
* No ambiente virtual, instale as bibliotecas necessárias: `pip install -r requirements.txt`

## Use:

`uvicorn --factory asgi:app --log-level critical --workers 12`

## Teste:

`ab -n 50 -c 10 http://127.0.0.1:5000`

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#flask_async)<br>
