--CREATE DATABASE GAMES;

if not exists (select * from information_schema.tables  where table_name = 'linguagens')
	begin
		create table linguagens(
			id int identity(1,1) not null ,
			lingua varchar(50) not null,
			sigla varchar(10) not null,
			linkReference varchar(50),
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
			link varchar(100) unique not null,
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		);
	end;

if not exists (select * from information_schema.tables  where table_name = 'plataforma')
	begin
		create table plataforma(
			id int not null identity(1,1),
			nome varchar(50) unique,
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

if not exists (select * from information_schema.tables  where table_name = 'reviewCompleta')
	begin
		create table reviewCompleta(
			id int not null identity(1,1),
			descricao text, 
			horasJogadas decimal(10,2) not null, 
			dataPublicada date, 
			horaPublicada time(0) null,
			recomendado int not null,

			pessoasAcharamUtil int, 
			pessoasAcharamEngracada int,
			pessoasReagiramEmoticon int,
			
			quantidadesComentarios int, 
			quantidadeJogosNaConta int null, 
			linkSteamReview varchar(500) unique not null,

			idSteam int null, 
			linguagemPublicacao int null,
			analiseFinal int null, 
			gameCadastrado int null 
			primary key(id)
		);  
	end;

if not exists (select * from information_schema.tables where table_name = 'reviewAboutComments')
	begin
		create table reviewAboutComments(
			id int not null identity(1,1),
			dataPublicada date not null,
			horaPublicada time(0) null,
			comments text not null,

			idPostReview int not null,
			idSteam int null, 
			dataCadastro date not null,
			dataAlterado date
			primary key(id)
		)
	end;

if not exists(select * from information_schema.tables where table_name = 'commentRegistered')
	begin
		create table commentRegistered(
			id int not null identity(1,1), 
			linkSteamReviewComment varchar(200) unique not null,
			postIDSteamReview int not null,
			idSteamGame int not null,
			idSteamPeoplePostReview int not null
		);
	end;
