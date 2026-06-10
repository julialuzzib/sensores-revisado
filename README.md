# Projeto CEIFA

## Revisão da interface de sensores
### Histórico
- Criado por Sofia em Abril de 2026.
- Revisado por Julia em Junho de 2026.

### Passo a passo
#### Para testar:
```
bash
pip install flask requests apscheduler

python app.py
```
Inicia em:
http://127.0.0.1:5000

É possível cadastrar sensores de temperatura e umidade, tanto externos quanto da estufa. As medições ocorrem dentro de um intervalo determinado, podendo haver erro de detecção, variações, ausência de resposta ou sem falhas. Resultando em um status, que varia entre ok, alerta ou erro. 

Opções de filtros auxiliam na visualização. Entre as ações é permitido o cadastro de irrigações (que resulta no aumento de umidade dos sensores quando atualizados, após isso, ocorre a redução gradativa, simulando a evaporação da umidade presente no solo) e a correção manual de um valor de temperatura.

Na aba Gerenciar há uma lista de sensores cadastrados, ao clicar em um deles é exibida uma lista com histórico de medições, faixa esperada, configuração, total de leituras, último dado cadastrado e log de eventos. Além da possibilidade de excluir ou atualizar os dados do sensor.  

Para gerar o arquivo de leituras csv:
```
bash
python json_para_csv.py
```
