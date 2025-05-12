Feature: Login de usuário

  Scenario: Login com dados válidos
    Given que o usuário está na página de login
    When ele preenche o e-mail e a senha válidos
    And clica no botão de Iniciar sessão
    Then ele deve ser redirecionado para a página inicial

  Scenario: Login com dados inválidos
    Given que o usuário está na página de login
    When ele preenche e-mail e senha inválidos
    And clica no botão de Iniciar sessão
    Then o sistema não deve realizar o login