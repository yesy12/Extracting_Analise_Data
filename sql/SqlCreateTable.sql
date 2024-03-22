--CREATE DATABASE GAMES;

if not exists (select * from information_schema.tables  where table_name = 'linguagens')
	begin
		create table linguagens(
			id int not null identity(1,1),
			lingua varchar(50),
			sigla varchar(5) UNIQUE ,
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		);
	end;

if not exists (select * from information_schema.tables  where table_name = 'situacaoFinal')
	begin
		create table situacaoFinal(
			id int not null identity(1,1),
			descricao  varchar(50) not null UNIQUE,
			relevancia int not null,
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		);
	end;

if not exists (select * from information_schema.tables  where table_name = 'gameCadastrado')
	begin
		create table gameCadastrado(
			id int not null,
			plataforma int,
			titulo  varchar(50) not null,
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		);
	end;

if not exists (select * from information_schema.tables  where table_name = 'plataforma')
	begin
		create table plataforma(
			id int not null identity(1,1),
			nome varchar(50),
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		);
	end;

if not exists (select * from information_schema.tables  where table_name = 'pessoaSteam')
	begin
		create table pessoaSteam(
			id int not null identity(1,1),
			Nickname varchar(30) not null,
			link varchar(100) unique not null,
			relevancia int DEFAULT 0,
			primary key(id)
		);
	end;

-- descricao self.player.getReviewAboutTheGame()
-- horasJogadas float not null, self.vote.getHoursPlayers()
-- dataPublicada date, self.player.getPublishDay()
-- recomendado int not null, self.vote.getRecomend()

-- pessoasAcharamUtil int, self.likes.getLikesUtil()
-- pessoasAcharamEngracada int,self.likes.getLikesFunny()
-- pessoasReagiramEmoticon int, self.likes.getLikesEmoticon()
	 
-- quantidadesComentarios int, self.playerInfo.getQuantifyCommentAboutFromReview()
-- quantidadeJogosNaConta int null, self.playerInfo.getQuantifyGameFromPlayerReview()
if not exists (select * from information_schema.tables  where table_name = 'reviewCompleta')
	begin
		create table reviewCompleta(
			id int not null identity(1,1),
			descricao text, 
			horasJogadas float not null, 
			dataPublicada date, 
			recomendado int not null,

			pessoasAcharamUtil int, 
			pessoasAcharamEngracada int,
			pessoasReagiramEmoticon int,
			
			quantidadesComentarios int, 
			quantidadeJogosNaConta int null, 

			idSteam int null, --ok
			linguagemPublicacao int null, --ok
			analiseFinal int null, --ok
			gameCadastrado int null --ok
			primary key(id)
		);  
	end;