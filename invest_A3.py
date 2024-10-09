investimentos = ['Ações da Empresa X', 'Ações da Empresa Y', 'Imóvel Z', 'Títulos Públicos P', 'Fundo de Investimento F']
custo = [30000, 50000, 40000, 10000, 20000]
retorno = [40000, 60000, 45000, 15000, 25000]

limite = 100000

ratio = [(retorno[i] / custo[i], investimentos[i], custo[i], retorno[i]) for i in range(len(investimentos))]

ratio.sort(reverse=True, key=lambda x: x[0])

selected_investimentos = []
total_custo = 0
total_retorno = 0

for r in ratio:
    if total_custo + r[2] <= limite:
        selected_investimentos.append(r[1])
        total_custo += r[2]
        total_retorno += r[3]

resultado = f"""
Seleção de Investimentos Otimizada:
----------------------------------"""

for investimentos in selected_investimentos:
    idx = investimentos.index(investimentos)
    resultado += f"\n{investimentos} -> Custo: R$ {custo[idx]:,.2f}, Retorno: R$ {retorno[idx]:,.2f}"

resultado += f"""
Custo total dos investimentos: R$ {total_custo:,.2f}
Retorno total esperado: R$ {total_retorno:,.2f}
"""

print(resultado)
