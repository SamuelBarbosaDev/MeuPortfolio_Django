<h1>Meu portfólio</h1>
<h3>Objetivo:</h3>
    <p>
        Nesse projeto busquei uma forma de condensar aquilo que 
        havia estudado sobre django e python, durante a criação 
        do Portfólio passei por todas as etapas, desde a ideia, 
        desenvolvimento, até que enfim ele fosse ao ar, no dia 3 
        de setembro, resumindo aprendi muito com essa experiência 
        desde como fazer um deploy, testar, montar a regra de 
        negócios, etc. 
    <a href="https://samuelbarbosa-portfolio.herokuapp.com/">Link para o site</a>: 
    </p>
    
<h3>Como Funciona:</h3>
    <p>
        Para rodando o projeto localmente, você precisara realizar os seguintes passos:
    </p>
    
   * Crie um ambiente virtual dentro da pasta /Meu-Portfolio `python3 -m venv venv`
   * Acesse a pasta /apps `cd apps/`
   * Execute o comando `pip install -r requirements.txt` para instalar as dependências
   * Execute o comando `python manage.py migrate` para gerar o banco de dados sqlite3
   * Execute o comando `python manage.py createsuperuser` e informe usuário e senha para criar um administrador
   * Acesse a pasta /apps/apps `cd apps/apps` e crie um arquivo .env
   * Dentro arquivo .env defina `DEBUG=True` e configure a SECRET_KEY `SECRET_KEY='COLOQUE_AQUI_SUA_SECRET_KEY'`.
   * Execute o comando `python manage.py runserver` para inicar o projeto
   * Acesse o endereço `localhost:8000` para ver o projeto rodando.
   * Acesse o endereço `localhost:8000/samueloficial@protonmail.com` para fazer as configurações no site.
   

<h3> O que aprendi:</h3>
    <p>
    De antemão digo que aprendi muita coisa, por exemplo, aprendi que é necessário estudar sobre AWS, 
    para aumentar a qualidade dos meus projetos no    futuro, durante o desenvolvimento do projeto precisei 
    mudar o design dos formulários, foi aí que descobrir o django-crispy-forms que deu outra cara para os 
    meus formulários, a utilização de bootstrap ajudou muito no desenvolvimento do portfólio, pois, economizou 
    muito tempo, além de tirar a necessidade de ter que fazer tudo na mão com css. 
    O pillow foi outro achado, pois, ele foi uma mão na roda, durante o desenvolvimento do projeto, tive a 
    necessidade de fazer o uploard de imagem, porém até onde sabia não tinha uma forma pronta de fazer isso 
    dentro do django "OBS: tinha uma forma de fazer isso com o formulário, porém no meu caso precisava ser 
    feito na área de administração do site", foi aí que descobrir um tutorial de um americano, 
    <a href="https://www.youtube.com/watch?v=-0nYBqY9i5w&list=PL9UTba6pPW3LM_D8GG8bjLX8EIaksgGpM&index=10">aqui está o link</a>, 
    tive muitos outros conhecimentos que adquiri, porém, são muitos para serem listados.
    </p>

<h3>Tecnologias utilizadas:</h3>

  - Linguagens:
    - python==3.10.4
  
  - Libs:
    - asgiref==3.5.2
    - autopep8==1.7.0
    - dj-database-url==1.0.0
    - Django==4.1
    - django-crispy-forms==1.14.0
    - django-filter==22.1
    - django-on-heroku==1.1.2
    - gunicorn==20.1.0
    - Pillow==9.2.0
    - psycopg2-binary==2.9.3
    - pycodestyle==2.9.1
    - python-decouple==3.6
    - sqlparse==0.4.2
    - toml==0.10.2  
    - whitenoise==6.2.0
  - Framework:
    - Django==4.1
