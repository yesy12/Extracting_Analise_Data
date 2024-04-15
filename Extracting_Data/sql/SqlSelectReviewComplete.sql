select 
	rc.id, rc.horasJogadas, rc.dataPublicada, rc.horaPublicada,
	ps.relevancia, l.lingua, l.sigla,
	rc.pessoasAcharamUtil, rc.pessoasAcharamEngracada, rc.pessoasReagiramEmoticon,
	rc.quantidadeJogosNaConta, rc.quantidadesComentarios,
	rc.recomendado, rc.analiseFinal,

	gc.titulo, gc.link, p.nome as plataforma,
	rc.descricao, rc.linkSteamReview

from reviewCompleta rc, pessoaSteam ps, linguagens l, gameCadastrado gc, plataforma p

where 
	ps.id = rc.idSteam and
	l.id = rc.linguagemPublicacao and
	gc.id = rc.gameCadastrado and
	p.id  = gc.plataforma and 
	l.id = rc.linguagemPublicacao	and
	l.sigla = 'EN'
	order by l.sigla
;