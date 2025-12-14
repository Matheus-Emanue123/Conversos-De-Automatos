# Sistema de Conversão e Teste de Autômatos

Sistema completo para trabalhar com autômatos finitos (AFD, AFN e AFN-Lambda), incluindo conversões, minimização e testes.

## Estrutura do Projeto

```
trab/
├── src/
│   ├── main.py           # Ponto de entrada e menus
│   ├── automato.py       # Classe Automato
│   ├── conversoes.py     # Funções de conversão entre tipos
│   ├── minimizacao.py    # Funções de minimização de AFD
│   ├── testes.py         # Funções de teste de palavras
│   └── utils.py          # Funções auxiliares
└── automatos/            # Exemplos de autômatos em JSON
    ├── teste.json
    ├── testelambda.json
    └── ...
```

## Módulos

### automato.py
**Classe principal que representa um autômato**
- `__init__`: Construtor
- `carregar_json`: Carrega autômato de arquivo JSON
- `salvar_json`: Salva autômato em arquivo JSON
- `construir_tabela_transicoes`: Constrói tabela de transições
- `fecho_lambda`: Calcula fecho lambda de estados
- `aceita_palavra`: Testa se palavra é aceita

### conversoes.py
**Funções de conversão entre tipos de autômatos**
- `afn_para_afd`: Converte AFN para AFD (construção de subconjuntos)
- `afd_para_afn`: Converte AFD para AFN (trivial)
- `afn_para_afn_lambda`: Adiciona transições lambda
- `afd_para_afn_lambda`: Converte AFD para AFN-Lambda
- `converter_estado_afd_para_nome`: Converte frozenset para string

### minimizacao.py
**Funções de minimização de AFD (algoritmo de Myhill-Nerode)**
- `minimizar_afd`: Função principal de minimização
- `remover_estados_inalcancaveis`: Remove estados não alcançáveis (BFS)
- `remover_estados_equivalentes`: Remove estados equivalentes (particionamento)
- `dividir_particao`: Divide partição de estados
- `construir_afd_minimizado`: Constrói AFD minimizado

### testes.py
**Funções de teste de palavras**
- `testar_palavra_terminal`: Testa palavra digitada no terminal
- `testar_palavras_arquivo`: Testa múltiplas palavras de arquivo

### utils.py
**Funções auxiliares**
- `verificar_nao_determinismo`: Verifica se autômato é não-determinístico
- `detectar_tipo_automato`: Detecta tipo (AFD/AFN/AFN-Lambda)
- `exibir_detalhes`: Exibe informações detalhadas

### main.py
**Ponto de entrada e sistema de menus**
- `menu_principal`: Menu principal do sistema
- `menu_conversao`: Menu de conversões
- `carregar_automato_menu`: Menu auxiliar de carregamento

## Formato JSON

```json
{
    "alfabeto": ["a", "b"],
    "estados": ["q0", "q1", "q2"],
    "estados_iniciais": ["q0"],
    "estados_finais": ["q2"],
    "transicoes": [
        ["q0", "q1", "a"],
        ["q1", "q2", "b"]
    ]
}
```

## Como Usar

```bash
cd "c:\Users\hecla\Desktop\CEFET\6° periodo\Linguagens Formais e Autômatos"
python src/main.py
```

### Menu Principal

1. **Carregar autômato** - Carrega de arquivo JSON
2. **Converter autômato** - AFN↔AFD, AFN-Lambda
3. **Minimizar autômato** - Minimiza AFD (converte se necessário)
4. **Testar palavra** - Teste interativo no terminal
5. **Testar palavras** - Testa múltiplas palavras de arquivo
6. **Salvar autômato** - Salva em arquivo JSON
7. **Exibir detalhes** - Mostra informações completas
0. **Sair**

## Exemplos de Uso

### Carregar e testar
```
1 → automatos/teste.json
4 → digite palavra
```

### Converter AFN para AFD
```
1 → automatos/testeafn.json
2 → 1 (AFN → AFD)
6 → saida.json
```

### Minimizar autômato
```
1 → automatos/teste.json
3
6 → minimizado.json
```

## Algoritmos Implementados

- **Construção de Subconjuntos** (AFN → AFD)
- **BFS** (alcançabilidade)
- **Myhill-Nerode** (minimização)
- **Fecho Lambda** (transições ε)

## Tecnologias

- Python 3.11
- Type hints (typing)
- Sets e frozensets
- JSON para persistência
