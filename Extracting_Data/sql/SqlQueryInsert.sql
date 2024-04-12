use games;

insert into situacaoFinal(descricao, relevancia, dataCadastro, dataAlterado) 
	   values	 ('Super Negativo', -2, GETDATE(), GETDATE()),
				 ('Negativo', -1, GETDATE(), GETDATE()),
				 ('Normal', 0, GETDATE(), GETDATE()),
				 ('Engraçada', 1, GETDATE(), GETDATE()),
				 ('Super Engraçada', 2, GETDATE(), GETDATE()),
				 ('Positiva', 3, GETDATE(), GETDATE()),
				 ('Super Positiva', 4, GETDATE(), GETDATE());

INSERT INTO Linguagens (lingua, linkReference, sigla, dataCadastro, dataAlterado)  
VALUES 
('Todos os Idiomas', 'all','al', GETDATE(), GETDATE()),
('Chinês simplificado', 'schinese', 'SC', GETDATE(), GETDATE()),
('Chinês tradicional', 'tchinese', 'TC', GETDATE(), GETDATE()),
( 'Japonês', 'japanese', 'JA', GETDATE(), GETDATE()),
('Coreano', 'koreana', 'KO', GETDATE(), GETDATE()),
('Tailandês', 'thai', 'TH', GETDATE(), GETDATE()),
('Búlgaro', 'bulgarian', 'BG', GETDATE(), GETDATE()),
('Tcheco', 'czech', 'CZ', GETDATE(), GETDATE()),
('Dinamarquês', 'danish', 'DK', GETDATE(), GETDATE()),
('Alemão', 'german', 'DE', GETDATE(), GETDATE()),
('Inglês', 'english', 'EN', GETDATE(), GETDATE()),
('Espanhol (Espanha)', 'spanish', 'ES', GETDATE(), GETDATE()),
('Espanhol (América Latina)', 'latam', 'ES_LATAM', GETDATE(), GETDATE()),
('Grego', 'greek', 'EL', GETDATE(), GETDATE()), 
('Francês', 'french', 'FR', GETDATE(), GETDATE()),
('Italiano', 'italian', 'IT', GETDATE(), GETDATE()),
('Indonésio', 'indonesian', 'ID', GETDATE(), GETDATE()),
('Húngaro', 'hungarian', 'HU', GETDATE(), GETDATE()),
('Holandês', 'dutch', 'NL', GETDATE(), GETDATE()),
('Norueguês', 'norwegian', 'NO', GETDATE(), GETDATE()),
('Polonês', 'polish', 'PL', GETDATE(), GETDATE()),
('Português (Portugal)', 'portuguese', 'PT', GETDATE(), GETDATE()),
('Português (Brasil)', 'brazilian', 'PT_BR', GETDATE(), GETDATE()),
('Romeno', 'romanian', 'RO', GETDATE(), GETDATE()),
('Russo', 'russian', 'RU', GETDATE(), GETDATE()),
('Finlandês', 'finnish', 'FI', GETDATE(), GETDATE()),
('Sueco', 'swedish', 'SV', GETDATE(), GETDATE()),
('Turco', 'turkish', 'TR', GETDATE(), GETDATE()),
('Vietnamita', 'vietnamese', 'VI', GETDATE(), GETDATE()),
('Ucraniano', 'ukrainian', 'UK', GETDATE(), GETDATE());
		 


insert into plataforma(nome, dataCadastro,dataAlterado)
		values		  ('Steam', GETDATE(),GETDATE()),
					  ('Xbox', GETDATE(),GETDATE()),
					  ('Apple', GETDATE(),GETDATE()),					  
					  ('Google Play', GETDATE(),GETDATE());