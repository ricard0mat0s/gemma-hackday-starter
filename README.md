# Gemma Hack Day: das anotações às tarefas

Cole anotações ou carregue o exemplo fictício, clique em **Gerar propostas de tarefas**, edite a tabela e baixe o CSV. Gemma extrai propostas; você confirma os compromissos. O aplicativo roda localmente; somente a inferência usa a API externa. Este é um ponto de partida para aprender e criar um projeto próprio no Hack Day LICA/Unimontes.

## Execute primeiro

Pré-requisitos: Git, Python 3.11 e acesso ao [Google AI Studio](https://aistudio.google.com/apikey). Ambiente verificado: Python **3.11.9**. Dentro da pasta deste repositório, no PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Preencha `GEMINI_API_KEY` no `.env` com a chave do projeto **Free Tier** de um membro elegível da equipe. Mantenha `GEMMA_MODEL=gemma-4-26b-a4b-it` e salve. Não publique a chave.

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

No macOS/Linux, os comandos equivalentes são:

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
# Edite .env no seu editor antes de continuar.
.venv/bin/python -m streamlit run app.py
```

Abra o endereço local mostrado no terminal. Confirme cada célula antes de baixar. Edições duram nesta sessão; uma geração bem-sucedida substitui a tabela. Falhas preservam o trabalho. Sem ações combinadas, a tabela pode ficar vazia. Não se calculam prazos relativos.

## Conta, dados e modelo

Fontes consultadas em **22/10/2026**: Gemma 4 tem entrada/saída gratuitas na [tabela de preços](https://ai.google.dev/gemini-api/docs/pricing). O [Free Tier](https://ai.google.dev/gemini-api/docs/billing) permite começar sem cartão nem ativar faturamento. Há [cotas por projeto](https://ai.google.dev/gemini-api/docs/rate-limits), requisitos de conta e [idade mínima de 18 anos; Brasil é atendido](https://ai.google.dev/gemini-api/docs/available-regions). Teste o acesso antes do evento; gratuidade e disponibilidade podem mudar.

Anotações são enviadas ao Google: use dados fictícios. No serviço gratuito, conteúdo pode melhorar produtos e ser revisado por humanos; consulte os [termos da API](https://ai.google.dev/gemini-api/terms).

O [modelo Gemma via Gemini API](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) é `gemma-4-26b-a4b-it`, configurável no `.env`. O código deste projeto usa [MIT](LICENSE); Gemma 4 usa [Apache 2.0](https://ai.google.dev/gemma/apache_2), e o serviço tem os termos acima.

## Onde alterar

- `app.py`: interface, edição e CSV.
- `gemma_client.py`: chamada ao Gemma, prompt e validação JSON em Python, sem pressupor suporte ao modo estruturado de Gemini.
- `examples/notes.txt`: anotações fictícias. [CONTRIBUTING.md](CONTRIBUTING.md): exercício e contribuição.

Verificação offline (respostas simuladas, sem chamar a API):

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Antes de submeter

- [ ] [Open-Source AI](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories): uso relevante de IA aberta/pesos abertos, GitHub público, licença aberta e demonstração com explicação do trabalho original.
- [ ] [Gemma](https://hacktoberfest-handbook.mlh.com/hack-days-partner-modules/partner-challenge-google-gemma): demonstrar integração real pela Gemini API e identificar o modelo no README.
- [ ] Creditar este starter, descrever as mudanças próprias e respeitar o início autorizado pela organização. Apenas renomear não basta.
- [ ] [OrganizerHQ](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day): registrar/check-in; uma pessoa submete uma vez, selecionando ambos os desafios se elegíveis e disponíveis. URL hospedada é opcional; demonstre localmente. Contagem de PRs não determina esses prêmios.

Ideia opcional: uma skill conforme o padrão aceito em Open-Source AI; para Gemma, demonstre também a integração via API.

[DigitalOcean](https://www.mlh.com/partners/digitalocean) é recurso opcional, dispensável aqui; créditos [exigem meio de pagamento para criar recursos](https://docs.digitalocean.com/platform/billing/signup-credit/).
