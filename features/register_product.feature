Feature: Cadastrar produto

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