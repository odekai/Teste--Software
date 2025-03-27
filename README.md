# Teste--Software

#Integrantes: João Vitor, Taila Camargo


# Gerador de Senhas Automáticas para Controle de Ponto

## Descrição
Este projeto tem como objetivo implementar um sistema de **geração automática de senhas** para o controle de ponto de funcionários, visando evitar fraudes, como o compartilhamento de senhas ou cartões de acesso entre colegas. O sistema gera uma nova senha a cada 5 minutos, garantindo que apenas o funcionário possa registrar seu ponto no horário correto. A senha é composta por caracteres alfanuméricos e símbolos, para aumentar a segurança.

### Funcionalidades
- Geração de **senhas fortes** e temporárias a cada 5 minutos.
- **Validação de senhas** para garantir que atendem aos critérios de segurança (mínimo de 8 caracteres, letras maiúsculas, minúsculas, números e símbolos).
- O sistema **não utiliza biometria**, devido a questões de acessibilidade e custos.
- **Flexibilidade** para funcionários com compromissos legítimos, permitindo que saiam mais cedo sem serem penalizados.

## Como Rodar o Projeto

### Pré-requisitos
- **Python 3.7+**
- **Pytest** para execução dos testes automatizados.

### Instalação
1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/Teste--Software.git
   cd Teste--Software
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Como Usar
O sistema pode ser utilizado da seguinte forma:

1. **Gerar uma nova senha**:
   ```python
   from passaword_utils import gerar_senha
   
   senha = gerar_senha(12)  # Gera uma senha de 12 caracteres
   print(senha)
   ```

2. **Validar uma senha**:
   ```python
   from password_utils import validar_senha
   
   senha = "Aa1@5678"
   if validar_senha(senha):
       print("Senha válida!")
   else:
       print("Senha inválida!")
   ```

### Como Rodar os Testes
Para garantir que o sistema funcione corretamente, você pode rodar os testes automatizados usando o Pytest.

1. Certifique-se de ter o **Pytest** instalado:
   ```bash
   pip install pytest
   ```

2. Execute os testes:
   ```bash
   pytest
   ```

Os testes estão localizados na pasta `tests/` e cobrem os seguintes tipos:
- **Teste de Unidade**: Verifica a funcionalidade isolada das funções `gerar_senha()` e `validar_senha()`.
- **Teste de Integração**: Testa a integração das funções do sistema.
- **Teste de Sistema**: Simula o uso real do sistema para validar a integração geral.
- **Teste de Aceitação**: Valida se o sistema atende aos requisitos do usuário final.
- **Teste de Regressão**: Garantia de que novas alterações não quebraram funcionalidades existentes.
- **Teste de Desempenho**: Mede o tempo de execução da geração de senhas para múltiplos usuários.

### Exemplos de Testes
Os exemplos de testes incluem a verificação do tamanho da senha, se ela contém letras maiúsculas, minúsculas, números e símbolos. Também são testadas as funcionalidades de **geração de senhas temporárias** e a **validação da segurança**.

### Dependências
- **Python 3.7+**
- **Pytest**

Dependências podem ser instaladas automaticamente com:
```bash
pip install -r requirements.txt
```

## Arquitetura do Projeto
O projeto é composto pelas seguintes partes principais:

1. **gerador_senha.py**: Contém as funções principais do sistema, incluindo a geração e validação de senhas.
2. **tests/**: Pasta contendo os testes automatizados escritos com Pytest.

## Justificativas para Não Usar Biometria
Embora a biometria seja uma tecnologia comum para controle de acesso, ela apresenta algumas desvantagens para esse cenário específico:
- **Acessibilidade**: Algumas pessoas podem ter dificuldades com a biometria, como desgaste das digitais ou condições genéticas que dificultam a leitura correta.
- **Custo**: A implementação e manutenção de sistemas biométricos são caras.
- **Privacidade**: O armazenamento de dados biométricos envolve questões de privacidade e segurança de dados sensíveis.

## Conclusão
Este projeto oferece uma solução eficiente para o controle de ponto dos funcionários, garantindo a segurança no registro de horas trabalhadas, evitando fraudes e permitindo flexibilidade para compromissos legítimos. Ele também pode ser facilmente adaptado e expandido para outros tipos de sistemas de controle de acesso.

---

### Dicas Adicionais
1. **Melhorias Futuras**: O sistema pode ser expandido para incluir uma **interface web** ou **integração com sistemas de RH** para facilitar o gerenciamento de senhas e registros de ponto.
2. **Segurança**: Pode-se adicionar criptografia de senhas ou outras medidas de segurança para proteger ainda mais o sistema.


