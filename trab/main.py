import json
from typing import List, Set, Dict, Tuple

class Automato:
    
    def __init__(self, alfabeto: List[str], estados: List[str],
                 estados_iniciais: List[str], estados_finais: List[str],
                 transicoes: List[List[str]]):
        self.alfabeto = set(alfabeto)
        self.estados = set(estados)
        self.estados_iniciais = set(estados_iniciais)
        self.estados_finais = set(estados_finais)
        self.transicoes = transicoes
        
    @classmethod
    def carregar_json(cls, caminho: str):
        
        with open(caminho, 'r', encoding='utf-8') as f:
            dados =json.load(f)
        return cls(
            dados['alfabeto'],
            dados['estados'],
            dados['estados_iniciais'],
            dados['estados_finais'],
            dados['transicoes']
        )
     
    def salvar_json(self, caminho: str):
        
        dados = {
            'alfabeto': sorted(list(self.alfabeto)),
            'estados': sorted(list(self.estados)),
            'estados_iniciais': sorted(list(self.estados_iniciais)),
            'estados_finais': sorted(list(self.estados_finais)),
            'transicoes': self.alfabeto
        }   
        with open(caminho, 'r', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)     
        
    def construir_tabela_transicoes(self) -> Dict[Tuple[str, str], Set[str]]:
        
        tabela = {}
        for origem, destino, simbolo in self.transicoes:
            chave = (origem, simbolo)
            if chave not in tabela:
                tabela[chave] = set()
            tabela[chave].add(destino)
        return tabela
    
    def fecho_lambda(self, estados: Set[str], tabela: Dict) -> Set[str]:
        
        fecho = set(estados)
        pilha = list(estados)
        
        while pilha:
            estado = pilha.pop()
            if (estado, '&') in tabela:
                for proximo in tabela[(estado, '&')]:
                    if proximo not in fecho:
                        fecho.add(proximo)
                        pilha.append(proximo) 
        return fecho
    
    def aceita_palavras(self, palavra: str, eh_afd: bool = False) -> bool:
        
        tabela = self.construir_tabela_transicoes()
        
        estados_atuais = self.fecho_lambda(self.estados_iniciais, tabela)
        
        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False
            
            proximos_estados = set()
            
            for estado in estados_atuais:
                if (estado, simbolo) in tabela:
                    proximos_estados.update(tabela[(estado, simbolo)])
                    
                    if not proximos_estados:
                        return False
                    
                    estados_atuais = self.fecho_lambda(proximos_estados, tabela)
                    
                    return bool(estados_atuais & self.estados_finais)                   
                
def afn_para_afd(afn: Automato) -> Automato:
    
    tabela_afn = afn.construir_tabela_transicoes() 
    estado_inicial_afd = frozenset(afn.fecho_lambda(afn.estados_iniciais, tabela_afn))
    
    estados_afd = set()
    transicoes_afd = []
    estados_finais_afd = set()
    
    fila = [estado_inicial_afd]
    processados = set()
    
    while fila:
        estado_atual = fila.pop(0)
        
        if estado_atual in processados:
            continue
        
        processados.add(estado_atual)
        estados_afd.add(estado_atual)
        
        if estado_atual & afn.estados_finais:
            estados_finais_afd.add(estado_atual)
            
        for simbolo in afn.alfabeto:
            if simbolo == '&':
                continue
            
        proximo_estado = afn.fecho_lambda(proximo_estado, tabela_afn)
        
        if proximo_estado:
            proximo_estado = frozenset(proximo_estado)
            
            transicoes_afd.append([
                converter_estado_afd_para_nome(estado_atual),
                converter_estado_afd_para_nome(proximo_estado),
                simbolo
            ])                       
            
            if proximo_estado not in processados:
                fila.append(proximo_estado)
                
    estados_afd_nomes = {converter_estado_afd_para_nome(e) for e in estados_afd}
    estados_finais_afd_nomes = {converter_estado_afd_para_nome(e) for e in estados_finais_afd}
    estado_inicial_afd_nome = converter_estado_afd_para_nome(estado_inicial_afd)

    alfabeto_afd = afn.alfabeto - {'&'}
    
    return Automato(
        alfabeto=list(alfabeto_afd),
        estados=list(estados_afd_nomes),
        estados_iniciais=[estado_inicial_afd_nome],
        estados_finais=list(estados_finais_afd_nomes),
        transicoes=transicoes_afd
    )


def converter_estado_afd_para_nome(estado_frozenset) -> str:

    if not estado_frozenset:
        return '{}'
    return '{' + ','.join(sorted(estado_frozenset)) + '}'           