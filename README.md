# 🛰️ FloodWatch Orbital — Mission Control AI

> Sistema de monitoramento inteligente de missões espaciais com análise de risco em tempo real.

---

## 👨‍🚀 Equipe

**Os Ciêntistas do Espaço**

| Nome | RM |
|------|----|
| Arthur Domingos Micarelli | 571476 |
| Enzo Yudi de Oliveira Hino | 570173 |
| Inaldo Pereira Freitas | 569672 |

---

## 🔗 Links

- 📁 [Repositório GitHub](https://github.com/EnzoHino/2026_GS1_Python)
- 🎬 [Vídeo Pitch no YouTube](LINK)

---

## 🚀 Funcionalidades

- **Monitoramento por ciclo** — analisa 5 sistemas críticos por ciclo de missão
- **Classificação de alerta** — níveis `NORMAL`, `ATENÇÃO` e `CRÍTICO` por área
- **Pontuação de risco** — cálculo acumulado por ciclo e classificação da missão
- **Relatório final** — médias, tendência, área mais afetada e classificação geral
- **Recomendações automáticas** — orientações operacionais baseadas no risco total

---

## 🛸 Áreas Monitoradas

| Área | Unidade | Normal | Atenção | Crítico |
|------|---------|--------|---------|---------|
| Temperatura interna | °C | 18–30 | < 18 ou 31–35 | > 35 |
| Comunicação com a base | % | ≥ 60 | 30–59 | < 30 |
| Sistema de energia | % | ≥ 50 | 20–49 | < 20 |
| Suporte de oxigênio | % | ≥ 90 | 80–89 | < 80 |
| Estabilidade operacional | % | ≥ 70 | 40–69 | < 40 |

---

## 🚦 Classificação da Missão

| Pontuação de risco (ciclo) | Classificação |
|----------------------------|---------------|
| 0 – 2 | ✅ MISSÃO ESTÁVEL |
| 3 – 5 | ⚠️ MISSÃO EM ATENÇÃO |
| 6 – 10 | 🚨 MISSÃO CRÍTICA |

---

## 🗂️ Estrutura do Projeto

```
2026_GS1_Python/
│
└── main.py        # Script principal com toda a lógica de monitoramento
```

---

## ▶️ Como Executar

**Pré-requisitos:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/EnzoHino/2026_GS1_Python.git
cd 2026_GS1_Python

# Execute o script
python main.py
```

A saída será impressa diretamente no terminal, exibindo os dados de cada ciclo seguidos do relatório final da missão.

---

## 📊 Exemplo de Saída

```
============================================================
MISSION CONTROL AI
============================================================
Missão: FloodWatch Orbital
Equipe: Os ciêntistas do espaço
Quantidade de ciclos analisados: 10
============================================================

CICLO 1
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Temperatura: 22 °C | NORMAL | Temperatura estável
Comunicação: 98% | NORMAL | Comunicação estável
...

============================================================
RELATÓRIO FINAL DA MISSÃO
============================================================
...
============================================================
```

---

## 🧠 Lógica Principal

O sistema é composto pelas seguintes funções:

- `classify_alert_level(value, area)` — retorna o nível de alerta (0, 1 ou 2) com base no valor e na área
- `format_alert_level(alert_level)` — converte o nível numérico para texto legível
- `format_areas(value, alert_level, area, is_avg)` — formata a linha de exibição de cada área
- `get_status_description(area, alert_level)` — retorna a descrição textual do status
- `classify_cycle(alert_level)` — classifica o ciclo com base na pontuação total de risco
- `get_recommendation(alert_level)` — retorna a recomendação operacional adequada

---
