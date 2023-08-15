<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary>
  <p>
    Nesse projeto foram desenvolvidas funções com o intuito de ser um cardapio virutal de um restaurante fictisio chamado "Chapa Quente".</br>
    Com todas as funções implementadas, o projeto é capaz de gera seu cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque
  </p>

🚵 Habilidades exercitadas: </br>
  - Praticar o conceito de `Hashmaps` através das estruturas de dados `Dict` e `Set`do Python; </br>
  - Praticar a ferramenta `Pandas` junto a sua estrutura de dados `DataFrame`; </br>
  - Praticar os conhecimentos de testes de software; </br>
  - Praticar os conhecimentos de orientação a objetos. </br>

</details>


# Orientações
<details>
  <summary><strong>Como iniciar</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-023-a-restaurant-orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-023-a-restaurant-orders`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
.
├── data
│   ├──🔸 inventory_base_data.csv
│   └──🔸 menu_base_data.csv
├── src
│   ├──🔸 __init__.py
│   ├──🔸 app.py
│   ├── models
│   │   ├──🔸 __init__.py
│   │   ├──🔸 dish.py
│   │   └──🔸 ingredient.py
│   └── services
│       ├──🔸 __init__.py
│       ├──🔹 inventory_control.py
│       ├──🔹 menu_builder.py
│       └──🔹 menu_data.py
├── tests
│   ├──🔸 __init__.py
│   ├──🔸 conftest.py
│   ├── dish
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_dish.py
│   ├── ingredient
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_ingredient.py
│   ├──🔸 ingredients.py
│   ├── mocks
│   │   ├──🔸 inventory_base_data.csv
│   │   ├──🔸 inventory_base_data_2.csv
│   │   └──🔸 menu_base_data.csv
│   ├──🔸 test_app.py
│   ├──🔸 test_inventory_control.py
│   ├──🔸 test_menu_builder.py
│   └──🔸 test_menu_data.py
├──🔸 README.md
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 requirements.txt
├──🔸 setup.cfg
├──🔸 setup.py
├──🔸 trybe-filter-repo.sh
└──🔸 trybe.yml

Legenda:
  🔸 Arquivos que não podem ser alterados.
  🔹 Arquivos a serem alterados para realizar os requisitos.

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

  ```bash
  pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```
</details>

## 3 - Mapeamento Pratos <> Ingredientes

> A classe `MenuData` fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.

### Implementação

A classe `MenuData` no arquivo `src/services/menu_data.py`.  
O teste utiliza o [arquivo de mock `tests/mocks/menu_base_data.csv`](./tests/mocks/menu_base_data.csv).

requisitos:

- a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro `source_path`;

- a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;

- a classe contenha o atributo `dishes` que deverá ser um _set_ com todos os pratos devidamente instanciados;

- cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.


---

## 4 - Geração dos cardápios

### Implementação

O método `get_main_menu` dentro da classe `MenuBuilder` que se encontra no arquivo `src/services/menu_builder.py`. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.

Seguindo a assinatura do método que foi deixada pela equipe anterior, o retorno deste método deve ser do tipo `DataFrame` original do pacote `pandas`. Assim, é necessário que o método retorne um `DataFrame` que contenham as colunas `dish_name`, `ingredients`, `price` e `restrictions` que se referem, respectivamente, ao **nome** do prato, **ingredientes** que o compõem, seu **preço** no cardápio e **restrições** daquele mesmo prato.

requisitos:

- a classe possa ser instanciada corretamente;

- o método `get_main_menu` retorna um `DataFrame` com o cardápio completo quando não é passado nenhum parâmetro;

- o método `get_main_menu` retorna um `DataFrame` com os cardápios corretos respeitando a restrição alimentar passada como parâmetro;

## 5 - Estoque de ingredientes

### Implementação

A classe `InventoryMapping` se encontra no arquivo `src/services/inventory_control.py`, nela foram implementados os métodos `check_recipe_availability` e `consume_recipe`.

requisitos:

- A classe possa ser devidamente instanciada;

- o método `check_recipe_availability` retorna `True` caso a receita esteja disponível para consumo e `False` caso contrário;

- o método `consume_recipe` subtrai os ingredientes da receita do total disponível em estoque caso a receita esteja disponível para consumo e levanta uma exceção `ValueError` caso contrário.

## 6 - Cardápios baseados no estoque 

### Implementação

método `get_main_menu`, feito no requisito 4. O método agora precisa considerar também a disponibilidade em estoque dos ingredientes dos pratos.

Ao longo de sua implementação você deve garantir que:

- o método `get_main_menu` retorna um `DataFrame` com o cardápio completo caso não exista restrição e todos os ingredientes estiverem disponíveis;

- o método `get_main_menu` retorna um `DataFrame` com os cardápios corretos respeitando a restrição alimentar passada como parâmetro e também a disponibilidade de ingredientes no estoque;
