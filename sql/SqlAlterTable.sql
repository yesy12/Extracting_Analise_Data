ALTER TABLE reviewCompleta
	add constraint fkReviewIDSteam foreign key(idSteam) 
	references pessoaSteam(id);

ALTER TABLE reviewCompleta
	add constraint fkLinguagemPublicacaoFromLinguagens foreign key(linguagemPublicacao)
	references linguagens(id);

 Alter table reviewCompleta
	add constraint fkAnaliseSituacao foreign key(analiseFinal)
	references situacaoFinal(id);

ALTER TABLE reviewCompleta
	add constraint fkGameCadastrado foreign key(gameCadastrado)
	references gameCadastrado(id);