Feature: Login de usuário

  Scenario: Login com dados válidos
    Given que o usuário está na página de login
    When ele preenche o campo e-mail
    And ele preenche o campo senha 
    And clica no botão de Iniciar sessão
    Then ele deve ser redirecionado para a página inicial

  Scenario: Login com dados inválidos
    Given que o usuário está na página de login
    When ele preenche o e-mail inválido 
    And ele preenche a senha inválida
    And clica no botão de Iniciar sessão
    Then o sistema não deve realizar o login