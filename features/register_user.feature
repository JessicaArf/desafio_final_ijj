Feature: Cadastro de usuário

  Scenario: Cadastro de usuário com dados válidos
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail
    And ele preenche a senha 
    And ele preenche o confirmar senha
    And ele clica no botão de Criar conta
    Then uma mensagem de sucesso contendo 'Usuário cadastrado com sucesso' deve ser exibida

   Scenario: Cadastro de usuário com e-mail já cadastrado
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail 
    And ele preenche a senha
    And ele preenche o confirmar senha 
    And ele clica no botão de Criar conta
    Then uma mensagem de erro contendo 'Usuario ja existente com email informado' deve ser exibida
   
   Scenario: Cadastro de usuário com senhas que não coincidem
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    And ele preenche o e-mail 
    And ele preenche a senha 
    And ele preenche o confirmar senha com uma senha diferente
    And ele clica no botão de Criar conta
    Then uma mensagem de erro contendo 'As senhas precisam ser iguais' deve ser exibida
   
   Scenario: Cadastro de usuário com e-mail sem o "@" no formato
    Given que o usuário não possui conta e está na página de login
    When ele clica no 'Clique aqui e registre-se'
    When ele preenche o e-mail sem @
    And ele clica no botão de Criar conta
    Then uma mensagem de erro contendo 'Digite um e-mail válido' deve ser exibida