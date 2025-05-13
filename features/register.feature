Feature: Cadastro de usuário

  Scenario: Cadastro com dados válidos
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail
    And ele preenche a senha
    And ele preenche o confirmar senha
    And ele clica no botão de Criar conta
    Then uma mensagem de sucesso contendo 'Usuário cadastrado com sucesso' deve ser exibida

   Scenario: E-mail já cadastrado
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail 
    And ele preenche a senha 
    And ele preenche o confirmar senha 
    And ele clica no botão de Criar conta
    Then uma mensagem de erro contendo 'Usuario ja existente com email informado' deve ser exibida
   
   Scenario: Senhas não coincidem
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail 
    And ele preenche a senha 
    And ele preenche o confirmar senha diferente
    And ele clica no botão de Criar conta
    Then uma mensagem de erro contendo 'As senhas precisam ser iguais' deve ser exibida
   