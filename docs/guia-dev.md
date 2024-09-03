## Padrões de Design

### Repository

   - Abstrai a lógica de acesso a dados, isolando a persistência da lógica de negócios e permitindo a adição de métodos personalizados.
   - **Nota**: No `Flask` com `SQLAlchemy`, criamos manualmente métodos CRUD para nossos modelos, pois não há uma interface de repositório pré-definida como em outras frameworks como o `Spring Data JPA`.

### Singleton

   - Garante que uma classe tenha apenas uma instância em todo aplicativo.
   - **Nota**: No Pyhton meta class como `SingletonMeta` assegura que qualquer classe que a utilize como metaclass terá apenas uma instância compartilhada.

### DTOs (Data Transfer Object)

- São objetos usados para transferir dados entre diferentes camadas ou componentes de uma aplicação(por ex., frequentemente entre `Controller` e `Services`).

   - **Da camada de Controller para a camada de Service**: Usando DTOs, o Controller envia dados validados para o Service, garantindo que os dados sejam processados de forma correta e consistente. Suponha que temos um modelo de domínio `User` e um DTO `UserCreateDTO`. Quando um cliente envia dados para criar um novo usuário:

      - 1. **Desserialização JSON para UserCreateDto**: Converter os dados JSON
         para UserCreateDto, durante esse processo, os dados são validados conforme as regras definidas no DTO. 
         - **Nota**: A desserialização em alguns frameworks ou linguagens é feita automaticamente, enquanto em outros é necessário chamar métodos específicos
      - 2. **Mapemaeno de UserCreateDto pra User**: Após a validação, os dados UserCreateDTO é transformado em um objecto User para manipulação adequada na camada Service.
         - **Nota**: Em alguns frameworks e linguagens, o mapeamento entre DTOs e entidades é feito automaticamente após a desserialização, utilizando bibliotecas externas que facilitam esse processo. Em outros casos, como no Flask com marshmallow, o mapeamento pode ser realizado por callbacks automáticos, como o @post_load, após a desserialização, sem a necessidade de separar explicitamente a desserialização do mapeamento.
      - 3. **Processamento pela service**: O Service realiza a lógica de negócio com o objecto User.
      - 4. **Serialização(Opcional)**: Se necessário, o Service pode retornar uma resposta ao cliente em formato JSON.
      **Nota**: A serialização pode ser feita automaticamente em alguns frameworks ou linguagens, convertendo diretamente o objeto em JSON. Em outros casos, pode-se utilizar bibliotecas externas ou métodos específicos para criar um DTO de resposta (como UserResponseDTO) e mapear o objeto para esse DTO, incluindo apenas os dados relevantes e omitindo informações sensíveis.

## Padrões Arquitecturais

### MSC(Model-Service-Controller)

  Uma variação do padrão Model-View-Controller `(MVC)`, com a adição de uma camada de Services. Útil para implementação do Estilo arquitectural `APIs REST`, organizando o sistema em camadas: `Resource Layer`, `Controllers Layer` , `Services Layer`:

**Model(Resource Layer)**:
   - Objecto que representa uma tabela no banco de dados.
   - **Obs**: No Python-Flask é usado a biblioteca de mapeamento objeto-relacional(ORM) `SQLAlchemy` para mapear classes Python para tabelas de banco de dados, simplificando a interação com o banco.

**Controller(Controllers Layer)**:
   - Responsável por receber as requisições HTTP e chamar os métodos adequados nos serviços.
   - **Obs**: No Python-Flask, as views desempenham o papel de controllers.

**Service(Services Layer)**:
   - Contém a lógica de negócios da aplicação 

## Estilo Arquitecturais

### APIs RESTful

Seguem os princípios e boas práticas de uma API REST, como:

**Interface Uniforme: Para uma comunicação eficiente entre o Cliente e Servidor**

   - Padronização dos métodos HTTP(GET, PUT, POST e DELETE)
   - Identificação do Recurso na Solicitação através de um `URI` específico
   - Representação dos recursos(*JSON*, *XML* ou *texto simples*).
      - **Serialização**: Converte um objecto em uma representação que possa ser facilmente armazenada e transmitida como JSON. 
      - **Desserialização**: Converte o dado em formato, como JSON, de volta em um objeto.

**Cacheable(Cacheável)**

   - Significa que uma resposta do servidor é armazenado em `Cache`, evitando solicitações repetidas para um mesmo recurso.

   - **Cache**: É um Armazenamento temporário que melhora a eficiência
   ao guardar dados acessados frequentemente, podem incluir:

      - **Cache em Memória**: Armazenamento local na mesma máquina.
      - **Cache Distribuído**: Armazenamento em várias máquinas, ideal para ambientes escaláveis e microserviços, onde várias instâncias precisam acessar o cache de forma eficiente.
      - **Cache de Disco**: Armazenamento em disco para maior persistência
      - **Obs**: A criação e gerenciamento de caches podem ser feitos utilizando `Redis`, uma solução popular para cache distribuído e em memória

      - Estratégias de Cache e TTL:
         - **Stale-While-Revalidate**: Serve dados desatualizados enquanto atualiza o cache em segundo plano.
         - **Cache-Control**: Define políticas de cache, como max-age e s-maxage.
         - **Time-to-Live (TTL)**: Tempo que os dados permanecem válidos no cache.
         - **Revalidação**: Verifica a atualização dos dados após o TTL expirar.
         - **Cache Invalidation**: Atualiza ou remove dados do cache quando necessário antes do TTL expirar.


**Interacções Stateless(Sem Estado) ou  Statefull(Com Estado)**

   - **Stateless**: O servidor não armazena o estado do cliente entre solicitações. Cada solicitação é independente, sem necessidade de dados de sessão no servidor.
      - **Exemplo**: Autenticação por `Tokens (ex.: JWT)`. O cliente envia um token(acess token) com cada solicitação, e o servidor valida sem armazenar estado.

      - **Uso**: Ideal para ambientes escaláveis e microserviços, pois facilita a distribuição de carga e a escalabilidade.
     
  
   - **Statefull**: O servidor mantém o estado do cliente entre solicitações, incluindo dados de sessão ou outras informações persistentes.
      - **Exemplo**: Autenticação por `Sessões`. O servidor usa um identificador de sessão armazenado em um cookie para manter o estado.
      - **Uso**: Comum em ambientes tradicionais e monolíticos, onde o gerenciamento do estado é mais centralizado.

   - **Obs**: Ambos podem ser combinados conforme os requisitos do sistema, dependendo das necessidades específicas de escalabilidade e gestão de estado. 
O uso de refresh tokens é uma técnica de gerenciamento de sessão, mas de uma maneira mais moderna e segura, comparada às sessões tradicionais baseadas em cookies.

- **HATEOAS(Hypermedia As the Engine Of Application State)**

   - Facilita na navegação de recursos da API, através de links fornecidos dinamicamente.

## Segurança

### Token 

#### Refresh Token(Renovação de Sessão com Refresh Tokens)

   - **Autenticação Stateless com Refresh Tokens**: Em sistemas de autenticação sem estado (stateless), os refresh tokens ajudam a prolongar sessões sem armazenar dados do usuário no servidor. Eles são emitidos junto com o access token (como JWT) e permitem obter um novo access token quando o anterior expira.

   - **Uso no Front-End**:
      - **Interceptores**: Aplicações front-end podem usar interceptores para monitorar a expiração do access token.
      - **Solicitação de Novo Token**: Quando o access token expira, o refresh token é usado em segundo plano para solicitar um novo access token sem interromper a experiência do usuário.
   - **Segurança e Gerenciamento**:
      - **Access Tokens de Curta Duração**: Access tokens têm um tempo de vida curto para minimizar riscos de sequestro.
      - **Refresh Tokens para Renovação**: O refresh token, com uma duração mais longa, permite renovar o access token de forma segura e conveniente.
   - **Benefícios**:
      - **Sessões Longas e Sem Interrupções**: Os usuários mantêm a sessão ativa sem precisar fazer login novamente frequentemente.
      - **Melhor Gestão de Tokens**: O uso de refresh tokens reduz o risco de ataques e melhora a segurança e a gestão dos tokens expiratórios.

### Criptografia

#### Criptografia Simétrica

   - Utiliza uma única chave para criptografar e descriptografar dados. É ideal para sistemas monolíticos ou ambientes confiáveis.

   - **Exemplo**: AES (Advanced Encryption Standard).

#### Criptografia Assimétrica

   - Utiliza um par de chaves (pública e privada). Adequada para sistemas distribuídos onde a chave pública pode ser compartilhada amplamente e a chave privada mantida segura.

   - **Exemplo**: RSA (Rivest–Shamir–Adleman), ECC (Elliptic Curve Cryptography). Ilustração com JWT (JSON Web Tokens)**:

      1. **Servidor Gera e Assina o Token**: O servidor cria um token JWT com informações do usuário e o assina usando sua chave privada.

      2. **Distribuição da Chave Pública**: O servidor envia o token para o cliente e disponibiliza sua chave pública através de um endpoint, como /auth/public-key.

      3. **Cliente Obtém a Chave Pública**: O cliente requisita a chave pública ao servidor para utilizá-la na verificação.

      4. **Verificação do Token**: O cliente usa a chave pública para verificar a assinatura do token JWT, garantindo sua autenticidade e que não foi alterado.


## Ferramentas e Instalação

### Redis

```bash
   sudo apt update
   sudo apt install redis-server
   redis-cli ping # Verificar a instalação do Redis
   # Links: [Redis Desktop Manager](https://redisdesktop.com/)
```

### Docker

```bash
```