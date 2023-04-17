## Flask Web App

O projeto é uma aplicação web desenvolvida em Flask para controle de frequência dos alunos em aulas. Ele permite que os professores cadastrem suas aulas, e que os alunos façam login para marcar sua própria presença nas aulas.

Ao utilizar a aplicação, os professores podem criar aulas e registrar a frequência dos alunos. Os alunos podem fazer login na aplicação e marcar sua presença nas aulas em que estão registrados.

O objetivo do projeto é fornecer uma ferramenta simples e eficiente para professores e alunos controlarem a frequência nas aulas. Além disso, o projeto é uma oportunidade para aprender conceitos fundamentais de programação web, como rotas, templates HTML/CSS, formulários e framework web, utilizando o Flask.

## Instalação

1. Clone o repositório: git clone https://github.com/gabrielccac/flask-web-app ou baixe o repositório.
2. Instale as dependências: pip install -r requirements.txt
3. Execute o arquivo init.py para inicializar o banco de dados.
4. Execute o app.py e o aplicativo pode ser acessado no seu navegador.


## Interfaces

<h3>Interface de Registro</h3>
<img src="https://i.imgur.com/qj7pDwt.png" alt="Captura de tela da interface de registro">

<h3>Interface de Login</h3>
<img src="https://i.imgur.com/ZFVH87M.png" alt="Captura de tela da interface de login">

<h3>Interface do Professor</h3>
<img src="https://i.imgur.com/pLbUq7U.png" alt="Captura de tela da interface do professor">

<h3>Interface do Professor</h3>
<img src="https://i.imgur.com/HcL6aQR.png" alt="Captura de tela da interface do professor">

<h3>Interface do Aluno</h3>
<img src="https://i.imgur.com/SZwKcaY.png" alt="Captura de tela da interface do aluno">


## Uso

1. É necessário primeiro fazer seu cadastro, como professor ou aluno. As autenticações são nativas do Flask-WTF.
2. Uma vez cadastrado, você será redirecionado para a página de login e basta fazer login com os dados usados no cadastro.
3. Como professor, você poderá registrar uma aula com um nome e uma data, que aparecerá na tabela, juntamente com os dados de frequência dos alunos.
4. Como aluno, você poderá ver as aulas disponíveis e marcar sua presença em aulas com data igual ou superior à data atual.

## Testes

Os testes de funcionamento de interface e lógicas de serviço foram feitos manualmente sem nenhum software ou interface de testes utilizada, como é um projeto inicial para prática e aprendizado, acredito que isso pode ser adicionado mais pra frente, junto com outras funcionalidades que quero trazer para a aplicação, mas tenho certeza que acrescentará muito ao projeto.
