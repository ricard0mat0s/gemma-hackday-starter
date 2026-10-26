# Uma contribuição pequena e verificável

Faça um **fork** pelo GitHub. Troque `SEU-USUARIO` pelo seu usuário:

```sh
git clone https://github.com/SEU-USUARIO/gemma-hackday-starter.git
cd gemma-hackday-starter
git switch -c exemplo-sem-prazo
```

Siga a instalação no README. Exercício: acrescente ao `examples/notes.txt` uma tarefa fictícia com responsável e sem prazo. Antes de executar, preveja a linha que deveria aparecer. Carregue o exemplo, gere com sua chave local e explique por que o prazo fica vazio. Edite o responsável, confirme a célula, baixe o CSV e confira a alteração. Rode também os testes offline:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Revise somente sua mudança; não inclua chaves ou dados reais:

```sh
git diff
git add examples/notes.txt
git commit -m "docs: acrescenta tarefa fictícia sem prazo"
git push -u origin exemplo-sem-prazo
```

No GitHub, abra um **pull request** do seu fork para o repositório de ensino. Explique o que mudou, sua previsão e o que verificou.

Para o projeto do hackathon, a equipe pode copiar o starter para um repositório próprio, manter a licença e dar crédito à base. Criar esse projeto e contribuir por PR ao repositório de ensino são atividades separadas. Siga as regras anunciadas sobre quando começar o trabalho do projeto.
