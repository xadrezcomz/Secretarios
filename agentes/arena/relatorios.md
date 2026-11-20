# Relatórios de xadrez do 1º ano (Colégio Arena)

Tarefa recorrente. Sempre que o Fhellipe pedir "fazer os relatórios" (de um bimestre, semestre ou
fechamento), siga exatamente este método.

## 1. O que é

Relatórios pedagógicos individuais das aulas de xadrez, um por aluno, organizados por turma, entregues em
Word (.docx). A coordenação lê e repassa às famílias, então o tom valoriza o aluno e soa humano e acolhedor.

Público: 1º ano do Fundamental, turmas A, B e C (19 alunos cada, 57 no total).

## 2. Regras de estilo (inegociáveis)

1. Não pode parecer escrito por IA. Linguagem humana, fluida, com o olhar de um professor que acompanhou
   aquele aluno de perto.
2. Cada relatório é único e individualizado. Nada de texto modelo preenchido. Nenhuma frase se repete
   entre alunos.
3. Não repetir nada dos bimestres anteriores: nem característica, nem elogio, nem a mesma construção de
   frase. Sempre comparar com os relatórios anteriores antes de escrever.
4. Sem travessões. Usar vírgula, ponto ou dois-pontos.
5. Concordância de gênero correta para cada aluno.
6. Parágrafo corrido, sem listas ou tópicos dentro do relatório.

## 3. Estrutura de cada relatório

1. Abertura: evolução e participação no período (variada em cada um).
2. Conteúdos do bimestre, integrados naturalmente ao texto.
3. Ponto em desenvolvimento, sempre em tom positivo ("ainda está sendo aprofundado", "requer mais
   prática"), nunca algo que soe negativo para a família.
4. Fechamento com uma característica individual de elogio, específica daquele aluno (concentração,
   memória visual, generosidade com os colegas, criatividade nas jogadas, liderança, calma, curiosidade
   etc.). Única para cada aluno e diferente a cada bimestre.

## 4. Turmas e alunos

- A cada pedido o Fhellipe envia a lista oficial atualizada (com matrícula). Ela é a fonte da verdade
  para nomes e grafia.
- Alunas que entraram no 2º semestre, em adaptação (1º A): Alice Mariano Bittar, Dália Duarte Siqueira e
  Liz Duarte Siqueira. O relatório delas foca na adaptação, nos primeiros movimentos das peças e nas
  partidas lúdicas sem exigência de regras rígidas.
- Betina Fagundes Abreu (1º B): a abordagem foi adaptada para o lúdico, o que despertou o interesse dela.
  O texto deve refletir essa reconexão positiva.
- Nomes parecidos, nunca trocar os perfis:
  - 1º A: Théo Alves Verano e Theo Jandre Barreto Andrade.
  - 1º C: Pedro Gouvea Albanell e Pedro Vieira Aurione.
  - Olívia De Castro Fontes (1º B) e Olivia Cintra Santana (1º C).
- Grafias que costumam variar (manter exatamente): Clarice Caiado Fleury Sotkeviciene Moura,
  João Gabriel Stefanine Fernandes Ferreira, Theo Martins Thibes.

## 5. Conteúdos do ano (para coerência da retrospectiva)

- 1º bimestre: regras básicas, movimentos das peças, introdução a xeque e xeque-mate.
- 2º bimestre: capturas elaboradas e início do cálculo, ataques de xeque-mate, segurança do rei com e sem
  roque, uso das peças no ataque e na defesa, tática (garfo, cravada, ataque descoberto).
- 3º bimestre: retorno lúdico com protojogos (xadrez australiano em duplas, xadrez perde e ganha), finais
  básicos de peão, revisão de garfo e cravada, reforço das regras básicas.
- 4º bimestre: relatório de fechamento de ano. Balanço das aprendizagens e conquistas do ano todo,
  incorporando o que cada aluno mais gostou de aprender (pelas anotações de aula; quem ficar sem anotação,
  complementar pelo perfil nos bimestres anteriores).

Em bimestres novos, o Fhellipe informa os conteúdos do período. Integrar ao texto com gradação realista de
domínio (um tema mais novo aparece como "ainda em desenvolvimento").

## 6. O que o Fhellipe envia a cada pedido

- A lista oficial de alunos (com matrícula) de cada turma.
- As anotações de aula (conteúdos do bimestre, como cada aluno evoluiu, o que mais gostou). Faltando
  anotação de algum aluno, complementar pelo perfil dele.
- Os relatórios do bimestre anterior, para comparar e não repetir.

Guarde o que ele enviar em `agentes/arena/arquivos/relatorios/` (listas, anotações, relatórios antigos),
para que o próximo bimestre já tenha a base de comparação.

## 7. Padrão visual do .docx (manter idêntico)

- Fonte Arial em todo o documento.
- Título de cada turma (ex.: "1º ANO A") em negrito, cor azul #1a3f6f, com borda inferior azul #2C5F9E.
- Nome do aluno em negrito, acima do parágrafo.
- Parágrafo do relatório justificado.
- Página A4, margens de cerca de 2 cm.
- Nome do arquivo: `Relatorios_Xo_Bimestre_1o_Ano_Arena_2026.docx` (X = número do bimestre).

O script `agentes/arena/ferramentas/relatorios_docx.py` gera o arquivo nesse padrão a partir de um JSON e
faz a conferência automática (ver o cabeçalho do script).

## 8. Conferência final obrigatória

Antes de entregar, cruzar lista oficial com os relatórios gerados e confirmar:

- Nenhum aluno ficou de fora.
- Nenhum nome sobrou.
- Nenhuma grafia de nome está errada.
- Nenhuma frase se repetiu entre alunos ou em relação ao bimestre anterior.
- Nenhum travessão no texto.

O script faz a parte mecânica. A leitura humana (gênero, tom, perfis trocados entre homônimos, construções
parecidas que não são idênticas) continua sendo sua.

Resumo: relatórios individuais, um por aluno, em .docx, humanos e únicos, sem repetir os bimestres
anteriores, sem travessões, no padrão visual acima, conferindo a lista oficial no fim.
