import functools

TAREFAS_DB = [
    {'id': 101, 'titulo': 'Atividade Parcial N704', 'aluno': 'Ana', 'prioridade': 5, 'concluida': False, 'prazo': '2025-09-29'},
    {'id': 102, 'titulo': 'Revisão P3 - Estruturas', 'aluno': 'Beto', 'prioridade': 2, 'concluida': False, 'prazo': '2025-10-15'},
    {'id': 103, 'titulo': 'Entrega de Relatório', 'aluno': 'Ana', 'prioridade': 4, 'concluida': True, 'prazo': '2025-09-20'},
    {'id': 104, 'titulo': 'Estudar Closures PF', 'aluno': 'Carlos', 'prioridade': 5, 'concluida': False, 'prazo': '2025-09-27'},
    {'id': 105, 'titulo': 'Preparar Casos de Teste', 'aluno': 'Beto', 'prioridade': 3, 'concluida': False, 'prazo': '2025-09-30'},
]

# FUNÇÃO DE ALTA ORDEM (HO Function)
def processar_tarefas(lista_tarefas: list, processador: callable) -> list:
    return [processador(t) for t in lista_tarefas]

# CLOSURE
def criar_filtro_por_prazo(prazo_limite: str) -> callable:
    def filtro_prazo(tarefa: dict) -> bool:
        return tarefa['prazo'] <= prazo_limite and tarefa['concluida'] == False
    return filtro_prazo

# LIST COMPREHENSION
def listar_ids_pendentes(lista_tarefas: list) -> list:
    return [t['id'] for t in lista_tarefas if t['concluida'] is False]

# FUNÇÃO LAMBDA
def ordenar_tarefas(lista_tarefas: list, chave_ordenacao: str) -> list:
    return sorted(lista_tarefas, key=lambda t: t.get(chave_ordenacao, 0), reverse=True)


# FUNÇÃO AUXILIAR para o HO Function
def adicionar_campo_urgencia(tarefa: dict) -> dict:
    if tarefa['prioridade'] >= 4:
        tarefa['status'] = 'ALTA_URGENCIA'
    else:
        tarefa['status'] = 'NORMAL'
    return tarefa

def marcar_como_concluida(tarefa_id: int, lista_tarefas: list) -> list:
    return [
        {**t, 'concluida': True} if t['id'] == tarefa_id else t
        for t in lista_tarefas
    ]

# CASOS DE TESTE (Melhoria para atender ao requisito de 1,0 ponto)
def executar_testes():
    print("--- 🔬 EXECUTANDO CASOS DE TESTE ---")

    tarefas_priorizadas = ordenar_tarefas(TAREFAS_DB, 'prioridade')
    print("\n[TESTE 1: LAMBDA] Tarefas Ordenadas (2 mais prioritárias):")
    print(tarefas_priorizadas[0:2])

    pendentes_ids = listar_ids_pendentes(TAREFAS_DB)
    print("\n[TESTE 2: LIST COMP.] IDs Pendentes:")
    print(pendentes_ids)

    filtro_recente = criar_filtro_por_prazo('2025-09-27')
    tarefas_com_prazo_apertado = list(filter(filtro_recente, TAREFAS_DB))
    print("\n[TESTE 3: CLOSURE] Tarefas com Prazo Apertado:")
    print(tarefas_com_prazo_apertado)

    tarefas_analisadas = processar_tarefas(TAREFAS_DB, adicionar_campo_urgencia)
    print("\n[TESTE 4: HO FUNC] Tarefas Processadas com Status 'ALTA_URGENCIA':")
    print([t for t in tarefas_analisadas if t.get('status') == 'ALTA_URGENCIA'])

    tarefas_apos_conclusao = marcar_como_concluida(102, TAREFAS_DB)
    print("\n[TESTE 5: IMUTABILIDADE] Status da Tarefa 102 (deve ser 'True' na nova lista):")
    print([t for t in tarefas_apos_conclusao if t['id'] == 102 and t['concluida'] is True])

if __name__ == '__main__':
    executar_testes()