use games;

insert into situacaoFinal(descricao, relevancia, dataCadastro, dataAlterado) 
	   values	 ('Super Negativo', -2, GETDATE(), GETDATE()),
				 ('Negativo', -1, GETDATE(), GETDATE()),
				 ('Normal', 0, GETDATE(), GETDATE()),
				 ('Engraçada', 1, GETDATE(), GETDATE()),
				 ('Super Engraçada', 2, GETDATE(), GETDATE()),
				 ('Positiva', 3, GETDATE(), GETDATE()),
				 ('Super Positiva', 4, GETDATE(), GETDATE());

INSERT INTO Linguagens (lingua, sigla, dataCadastro, dataAlterado) 
		VALUES			('Inglês', 'EN', GETDATE(), GETDATE()),
						('Português Brasil','PT_BR', GETDATE(), GETDATE()),
						('Mandarim (Chinês)', 'ZH', GETDATE(), GETDATE()),
						('Espanhol', 'ES', GETDATE(), GETDATE()),
						('Hindi', 'HI', GETDATE(), GETDATE()),
						('Francês', 'FR', GETDATE(), GETDATE()),
						('Árabe', 'AR', GETDATE(), GETDATE()),
						('Bengali', 'BN', GETDATE(), GETDATE()),
						('Russo', 'RU', GETDATE(), GETDATE()),
						('Português', 'PT', GETDATE(), GETDATE()),
						('Indonésio', 'ID', GETDATE(), GETDATE()),
						('Urdu', 'UR', GETDATE(), GETDATE()),
						('Alemão', 'DE', GETDATE(), GETDATE()),
						('Japonês', 'JA', GETDATE(), GETDATE()),
						('Suaíli', 'SW', GETDATE(), GETDATE()),
						('Marathi', 'MR', GETDATE(), GETDATE()),
						('Telugu', 'TE', GETDATE(), GETDATE()),
						('Turco', 'TR', GETDATE(), GETDATE()),
						('Tâmil', 'TA', GETDATE(), GETDATE()),
						('Vietnamita', 'VI', GETDATE(), GETDATE()),
						('Coreano', 'KO', GETDATE(), GETDATE()),
						('Francês (Canadá)', 'FR_CA', GETDATE(), GETDATE()),
						('Italiano', 'IT', GETDATE(), GETDATE()),
						('Chinês (Cantonês)', 'ZH_HK', GETDATE(), GETDATE()),
						('Tailandês', 'TH', GETDATE(), GETDATE());

INSERT INTO Linguagens (lingua, sigla, dataCadastro, dataAlterado) 
		values	('Gujarati', 'GU', GETDATE(), GETDATE()),
				('Polonês', 'PL', GETDATE(), GETDATE()),
				('Xangai', 'ZH_SH', GETDATE(), GETDATE()),
				('Malayalam', 'ML', GETDATE(), GETDATE()),
				('Oriya', 'OR', GETDATE(), GETDATE()),
				('Húngaro', 'HU', GETDATE(), GETDATE()),
				('Javanês', 'JV', GETDATE(), GETDATE()),
				('Sueco', 'SV', GETDATE(), GETDATE());

INSERT INTO Linguagens (lingua, sigla, dataCadastro, dataAlterado)
		values	('Tagalo', 'TL', GETDATE(), GETDATE()),
				('Hebraico', 'HE', GETDATE(), GETDATE()),
				('Esperanto', 'EO', GETDATE(), GETDATE()),
				('Neerlandês', 'NL', GETDATE(), GETDATE()),
				('Grego', 'EL', GETDATE(), GETDATE()),
				('Cingalês', 'SI', GETDATE(), GETDATE()),
				('Finlandês', 'FI', GETDATE(), GETDATE()),
				('Nepalês', 'NE', GETDATE(), GETDATE()),
				('Haitiano', 'HT', GETDATE(), GETDATE()),
				('Bielorrusso', 'BE', GETDATE(), GETDATE()),
				('Letão', 'LV', GETDATE(), GETDATE()),
				('Punjabi', 'PA', GETDATE(), GETDATE()),
				('Eslovaco', 'SK', GETDATE(), GETDATE()),
				('Esloveno', 'SL', GETDATE(), GETDATE()),
				('Somali', 'SO', GETDATE(), GETDATE()),
				('Lituanês', 'LT', GETDATE(), GETDATE()),
				('Tswana', 'TN', GETDATE(), GETDATE()),
				('Cazaque', 'KK', GETDATE(), GETDATE()),
				('Guarani', 'GN', GETDATE(), GETDATE()),
				('Línguas Kongo', 'KG', GETDATE(), GETDATE()),
				('Kirundi', 'RN', GETDATE(), GETDATE()),
				('Rundi', 'RN', GETDATE(), GETDATE());

insert into plataforma(nome, dataCadastro,dataAlterado)
		values		  ('Steam', GETDATE(),GETDATE()),
					  ('Xbox', GETDATE(),GETDATE()),
					  ('Apple', GETDATE(),GETDATE()),					  
					  ('Google Play', GETDATE(),GETDATE());