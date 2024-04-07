--Tabela
CREATE TABLE tb_usuario(
	cod_usuario SERIAL PRIMARY KEY,
	login VARCHAR(200) NOT NULL,
	senha VARCHAR(200) NOT NULL
);

-- pop tb_usuarios
INSERT INTO tb_usuario (login, senha) VALUES ('admin', 'admin');
INSERT INTO tb_usuario (login, senha) VALUES ('William', '123456');

--busca 
SELECT * FROM tb_usuario;