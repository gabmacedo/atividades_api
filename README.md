# 📚 API de Reserva de Salas

Este repositório contém a **API de Atividades**, desenvolvida com **Flask** e **SQLite**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Atividades é um **microsserviço** que faz parte de um sistema maior de [Gerenciamento Escolar](https://github.com/gabmacedo/schoolSystem_API.git)
, sendo responsável exclusivamente pelo gerenciamento de atividades realizadas por professores.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se o **Professor** existe (`GET /professores/<id>`)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/gabmacedo/atividades_api.git
cd atividade-service
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5001`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /atividades` – Lista todas as atividades
- `POST /atividades` – Cria uma nova atividade (com verificação de professor)
- `GET /atividades/<id>` – Detalha uma atividade
- `DELETE /atividades/<id>` – Remove uma atividade
- `GET /atividades/professor/<id>` – Lista atividades de um professor

### Exemplo de corpo JSON para criação:

```json
{
  "titulo": "Titulo da atividade",
  "descricao": "Descrição da atividade",
  "professor_id": 1
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5050
```

E que o endpoint de `GET /professores/<id>` esteja funcionando corretamente para que a verificação do professor ocorra com sucesso.

---

## 📦 Estrutura do Projeto

```
atividade-service/
├── controller/
│   └──atividade_controller.py
├── database/
│   └──db.py
├── models/
│   └──atividade_model.py
├── services/
│   └──pessoa_service_client.py
├── app.py
├── config.py
├── database.db
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Futuras Melhorias

- Validação de atividades duplicadas para o mesmo professor e disciplina
- Filtros por data ou período letivo
- Autenticação de usuários

---

## 🧑‍💻 Autores

- [Gabriel Aparecido de Macedo](https://github.com/gabmacedo) | RA: 2401541  
- [Guilherme Eduardo Moraes Pecorari](https://github.com/GuilhermePecorari) | RA: 2400086  
- [Davi de Moraes Bizerra](https://github.com/Davibizerra) | RA: 2401072
