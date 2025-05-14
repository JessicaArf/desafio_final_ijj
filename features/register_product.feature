Feature: Cadastro de produto

  Scenario: Cadastro de produto com sucesso
    Given que o usuário está logado
    And clica no botão Adicionar
    When preenche o nome do produto
    And preenche a descrição do produto
    And seleciona uma categoria
    And preenche o preço
    And faz o upload de uma imagem
    And preenche o frete
    And clica no botão Enviar Novo Produto
    Then o produto deve ser cadastrado com sucesso

Scenario: Campo 'Nome do Produto' é obrigatório
    Given que o usuário está logado
    And clica no botão Adicionar
    When preenche a descrição do produto
    And seleciona uma categoria
    And preenche o preço
    And faz o upload de uma imagem
    And preenche o frete
    And clica no botão Enviar Novo Produto
    Then deve exibir a mensagem 'Preencha o campo Nome'

  Scenario: Campo 'Descrição do Produto' é obrigatório
    Given que o usuário está logado
    And clica no botão Adicionar
    When preenche o nome do produto
    And seleciona uma categoria
    And preenche o preço
    And faz o upload de uma imagem
    And preenche o frete
    And clica no botão Enviar Novo Produto
    Then deve exibir a mensagem 'Descrição do produto necessaria.'

  Scenario: Upload de imagem é obrigatório
    Given que o usuário está logado
    And clica no botão Adicionar
    When preenche o nome do produto
    And preenche a descrição do produto
    And seleciona uma categoria
    And preenche o preço
    And preenche o frete
    And clica no botão Enviar Novo Produto
    Then deve exibir a mensagem 'Image is required'

  Scenario: Campo 'Frete' é obrigatório
    Given que o usuário está logado
    And clica no botão Adicionar
    When preenche o nome do produto
    And preenche a descrição do produto
    And seleciona uma categoria
    And preenche o preço
    And faz o upload de uma imagem
    And clica no botão Enviar Novo Produto
    Then deve exibir a mensagem 'Defina o valor do frete'