def classify_alert_level(value: int, area: str) -> int:
    if area == 'Temperatura interna':
        if value < 18:
            return 1
        elif value >= 18 and value <= 30:
            return 0
        elif value > 30 and value <= 35:
            return 1
        else:
            return 2
    
    elif area == 'Comunicação com a base':
        if value < 30:
            return 2
        elif value >= 30 and value <= 59:
            return 1
        else:
            return 0
        
    elif area == 'Sistema de energia':
        if value < 20:
            return 2
        elif value >= 20 and value <= 49:
            return 1
        else:
            return 0

    elif area == 'Suporte de oxigênio':
        if value < 80:
            return 2
        elif value >= 80 and value <= 89:
            return 1
        else:
            return 0

    elif area == 'Estabilidade operacional':
        if value < 40:
            return 2
        elif value >= 40 and value <= 69:
            return 1
        else:
            return 0


def format_alert_level(alert_level: int) -> str:
    if alert_level == 0:
        return 'NORMAL'
    elif alert_level == 1:
        return 'ATENÇÃO'
    elif alert_level == 2:
        return 'CRÍTICO'


def format_areas(value: int, alert_level: int, area: str, is_avg: bool) -> str:
    if not is_avg:
        if area == 'Temperatura interna':
            return f'Temperatura: {value} °C | {format_alert_level(alert_level)}'

        elif area == 'Comunicação com a base':
            return f'Comunicação: {value}% | {format_alert_level(alert_level)}'
            
        elif area == 'Sistema de energia':
            return f'Bateria: {value}% | {format_alert_level(alert_level)}'
            
        elif area == 'Suporte de oxigênio':
            return f'Oxigênio: {value}% | {format_alert_level(alert_level)}'

        elif area == 'Estabilidade operacional':
            return f'Estabilidade: {value}% | {format_alert_level(alert_level)}'
            
    else:
        if area == 'Temperatura interna':
            return f'Média de Temperatura: {value} °C'

        elif area == 'Comunicação com a base':
            return f'Média de Comunicação: {value}%'
            
        elif area == 'Sistema de energia':
            return f'Média de Bateria: {value}%'
            
        elif area == 'Suporte de oxigênio':
            return f'Média de Oxigênio: {value}%'

        elif area == 'Estabilidade operacional':
            return f'Média de Estabilidade: {value}%'
        

def get_status_description(area: str, alert_level: int) -> str:
    descriptions = {
        'Temperatura interna':       ['Temperatura estável', 'Temperatura elevada', 'Risco de superaquecimento'],
        'Comunicação com a base':    ['Comunicação estável', 'Comunicação instável', 'Comunicação com a base em nível crítico'],
        'Sistema de energia':        ['Energia estável', 'Bateria abaixo do recomendado', 'Bateria em nível crítico'],
        'Suporte de oxigênio':       ['Oxigênio adequado', 'Oxigênio abaixo do ideal', 'Oxigênio em nível crítico'],
        'Estabilidade operacional':  ['Estabilidade operacional adequada', 'Estabilidade operacional reduzida', 'Estabilidade operacional crítica'],
    }
    return descriptions[area][alert_level]


def classify_cycle(alert_level: int) -> str:
    if alert_level <= 2:
        return 'MISSÃO ESTÁVEL'
    elif alert_level <= 5:
        return 'MISSÃO EM ATENÇÃO'
    elif alert_level <= 10:
        return 'MISSÃO CRÍTICA'


def get_recommendation(alert_level: int) -> str:
    if alert_level <= 2:
        return 'Manter operação normal e continuar monitoramento.'
    elif alert_level <= 5:
        return 'Monitorar sistemas em atenção e preparar plano de contingência.'
    else:
        return 'Ativar modo de segurança e priorizar suporte à vida, energia e comunicação.'
    
    
data = [
    [22, 98, 95, 98, 95],
    [15, 85, 75, 92, 88],
    [32, 70, 60, 95, 78],
    [38, 55, 52, 91, 72],
    [28, 15, 45, 85, 65],
    [33, 40, 12, 82, 45],
    [25, 62, 50, 75, 50],
    [37, 25, 18, 72, 28],
    [30, 60, 50, 90, 70],
    [26, 65, 40, 88, 68] 
]

alerts_cycles = []
alerts_cycles_total = []

areas = [
 "Temperatura interna",
 "Comunicação com a base",
 "Sistema de energia",
 "Suporte de oxigênio",
 "Estabilidade operacional"
]


print(f"""
============================================================
MISSION CONTROL AI
============================================================
Missão: FloodWatch Orbital
Equipe: Os ciêntistas do espaço
Quantidade de ciclos analisados: {len(data)}      
============================================================""")
for i, cycle in enumerate(data):
    alert_level_cycle = 0
    alerts_cycle = []
    print(f'\nCICLO {i+1}')
    print('=-'*30 + '=')
    
    for idx in range(len(cycle)):
        alert_level = classify_alert_level(cycle[idx], areas[idx])
        print(f'{format_areas(cycle[idx], alert_level, areas[idx], False)} | {get_status_description(areas[idx], alert_level)}')
        
        alert_level_cycle += alert_level
        alerts_cycle.append(alert_level)
        
    alerts_cycles.append(alerts_cycle)
    alerts_cycles_total.append(alert_level_cycle)
    
    print(f'\nPontuação de risco do ciclo: {alert_level_cycle}')
    print(f'Classificação do ciclo: {classify_cycle(alert_level_cycle)}')
    print(f'Recomendação: {get_recommendation(alert_level_cycle)}')


alerts_cycles_total = [sum(cycle) for cycle in alerts_cycles]

area_scores = [0] * len(areas)
averages = [0] * len(areas)
total_risk = 0
critical_cycles = 0
first_half = 0
second_half = 0
half = len(alerts_cycles_total) // 2

for i, cycle in enumerate(alerts_cycles):
    for idx, value in enumerate(cycle):
        area_scores[idx] += value
        averages[idx] += data[i][idx]
    
    total_risk += alerts_cycles_total[i]
    
    if alerts_cycles_total[i] >= 6:
        critical_cycles += 1
    
    if i < half:
        first_half += alerts_cycles_total[i]
    else:
        second_half += alerts_cycles_total[i]

for idx in range(len(averages)):
    averages[idx] = round(averages[idx] / len(data), 2)

average_risk = round(total_risk / len(alerts_cycles_total), 2)
most_critical_cycle = alerts_cycles_total.index(max(alerts_cycles_total)) + 1
highest_risk_score = max(alerts_cycles_total)
most_affected_area = areas[area_scores.index(max(area_scores))]
final_classification = classify_cycle(round(average_risk))

area_scores_str = ''
for idx in range(len(areas)):
    area_scores_str += f'{areas[idx]}: {area_scores[idx]} pontos\n'
area_scores_str = area_scores_str.strip()

if first_half < second_half:
    trend = 'A missão apresentou tendência de piora.'
elif first_half > second_half:
    trend = 'A missão apresentou tendência de melhora.'
else:
    trend = 'A missão apresentou tendência estável.'


print(f"""
============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
Missão: FloodWatch Orbital
Equipe: Os ciêntistas do espaço

Quantidade de ciclos analisados: {len(data)}

Média de temperatura: {averages[0]} °C
Média de comunicação: {averages[1]}%
Média de bateria: {averages[2]}%
Média de oxigênio: {averages[3]}%
Média de estabilidade: {averages[4]}%

Ciclo mais crítico: Ciclo {most_critical_cycle}
Maior pontuação de risco: {highest_risk_score}
Risco médio da missão: {average_risk}
Quantidade de ciclos críticos: {critical_cycles}

Tendência da missão:
{trend}

Pontuação acumulada por área:
{area_scores_str}

Área mais afetada:
{most_affected_area}

Classificação final da missão:
{final_classification}
============================================================""")