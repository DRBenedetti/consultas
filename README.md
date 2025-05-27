# 🩺 Consultas

**Consultas** é uma aplicação web desenvolvida com Django para gerenciamento de pacientes e agendamentos médicos.  
O sistema permite o cadastro de pacientes, agendamento de consultas e visualização de informações de forma organizada e eficiente.

## ⚙️ Tecnologias Utilizadas

- Python 3.x  
- Django 4.x  
- SQLite (banco de dados padrão do Django)  
- HTML5 e CSS3  

## 🚀 Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/DRBenedetti/consultas.git
   cd consultas
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

6. Acesse a aplicação:

   Abra o navegador e vá para: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🗂️ Estrutura do Projeto

```
consultas/
├── core/               # Configurações do projeto Django
├── pacientes/          # Aplicação para gerenciamento de pacientes
├── templates/          # Templates HTML usados nas views
├── manage.py           # Script de gerenciamento do Django
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.  
Consulte o arquivo `LICENSE` para mais informações.
