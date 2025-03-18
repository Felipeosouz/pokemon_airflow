# Pokémon Airflow Project

## Visão Geral

Bem-vindo ao projeto Pokémon Airflow! Este projeto foi gerado após a execução do comando `astro dev init` usando o Astronomer CLI. Este README descreve o conteúdo do projeto, bem como como executar o Apache Airflow em sua máquina local.

## Conteúdo do Projeto

Seu projeto Astro contém os seguintes arquivos e pastas:

- **dags**: Esta pasta contém os arquivos Python para seus DAGs do Airflow. Por padrão, este diretório inclui um DAG de exemplo:
    - `pokemon_dag.py`: Este DAG captura dados de Pokémon da API PokeAPI e armazena no PostgreSQL.
- **Dockerfile**: Este arquivo contém uma imagem Docker do Astro Runtime versionada que fornece uma experiência diferenciada do Airflow. Se você quiser executar outros comandos ou substituições em tempo de execução, especifique-os aqui.
- **include**: Esta pasta contém quaisquer arquivos adicionais que você deseja incluir como parte do seu projeto. Está vazia por padrão.
- **packages.txt**: Instale pacotes de nível de sistema operacional necessários para o seu projeto adicionando-os a este arquivo. Está vazio por padrão.
- **requirements.txt**: Instale pacotes Python necessários para o seu projeto adicionando-os a este arquivo. Está vazio por padrão.
- **plugins**: Adicione plugins personalizados ou da comunidade para o seu projeto neste arquivo. Está vazio por padrão.
- **airflow_settings.yaml**: Use este arquivo apenas localmente para especificar Conexões, Variáveis e Pools do Airflow em vez de inseri-los na interface do Airflow enquanto você desenvolve DAGs neste projeto.

## Executar o Projeto Localmente

1. Inicie o Airflow em sua máquina local executando `astro dev start`.

Este comando irá iniciar 4 contêineres Docker em sua máquina, cada um para um componente diferente do Airflow:

- **Postgres**: Banco de Dados de Metadados do Airflow
- **Webserver**: O componente do Airflow responsável por renderizar a interface do Airflow
- **Scheduler**: O componente do Airflow responsável por monitorar e acionar tarefas
- **Triggerer**: O componente do Airflow responsável por acionar tarefas diferidas

2. Verifique se todos os 4 contêineres Docker foram criados executando `docker ps`.

Nota: Executar `astro dev start` iniciará seu projeto com o Webserver do Airflow exposto na porta 8080 e o Postgres exposto na porta 5432. Se você já tiver alguma dessas portas alocadas, você pode [parar seus contêineres Docker existentes ou alterar a porta](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Acesse a interface do Airflow para o seu projeto local do Airflow. Para fazer isso, vá para [http://localhost:8080/](http://localhost:8080/) e faça login com 'admin' para ambos o Nome de Usuário e a Senha.

Você também deve conseguir acessar seu Banco de Dados Postgres em 'localhost:5432/postgres'.

## Estrutura do DAG

O DAG principal do projeto é `capture_pokemon_dag` localizado em [dags/pokemon_dag.py](dags/pokemon_dag.py). Este DAG captura dados de Pokémon da API PokeAPI e os armazena no banco de dados PostgreSQL.

## Testes

Os testes para os DAGs estão localizados na pasta `tests/dags`. Por exemplo, o arquivo [tests/dags/test_dag_example.py](tests/dags/test_dag_example.py) contém testes de exemplo para garantir que todos os DAGs tenham tags, tentativas de reexecução definidas para dois e sem erros de importação.

## Contato

O Astronomer CLI é mantido com carinho pela equipe da Astronomer. Para relatar um bug ou sugerir uma alteração, entre em contato com nosso suporte.

---

Para mais informações, consulte a [documentação do Astronomer](https://www.astronomer.io/docs/astro/cli/develop-project#configure-airflow_settingsyaml-local-development-only).