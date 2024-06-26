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

ALTER TABLE gameCadastrado
	add constraint fkPlataformaCadastrada foreign key(plataforma)
	references plataforma(id);

ALTER TABLE reviewAboutComments
	add constraint fkIdPostReview foreign key(idPostReview)
	references reviewCompleta(id)

ALTER TABLE reviewAboutComments
	add constraint fkIDSteam foreign key(idSteam)
	references pessoaSteam(id)

ALTER TABLE commentRegistered
	add constraint fkPostIdSteam foreign key(postIDSteamReview)
	references reviewCompleta (id)

ALTER TABLE commentRegistered
	add constraint fkIdSteamComment foreign key(idSteamGame) 
	references gameCadastrado(id);
	
ALTER TABLE commentRegistered
	add constraint fkIdSteamPeoplePosted foreign key(idSteamPeoplePostReview) 
	references pessoaSteam(id);
