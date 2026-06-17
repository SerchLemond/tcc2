db_context = """
-- Inserções para a tabela tipo_entrada
INSERT INTO tipo_entrada (id, nome) VALUES (1, 'Caso Novo');
INSERT INTO tipo_entrada (id, nome) VALUES (2, 'Recidiva');
INSERT INTO tipo_entrada (id, nome) VALUES (3, 'Reingresso após Abandono');
INSERT INTO tipo_entrada (id, nome) VALUES (4, 'Não Sabe');
INSERT INTO tipo_entrada (id, nome) VALUES (5, 'Transferência');
INSERT INTO tipo_entrada (id, nome) VALUES (6, 'Pós-óbito');

-- Inserções para a tabela ppl
INSERT INTO ppl (id, nome) VALUES (1, 'Sim');
INSERT INTO ppl (id, nome) VALUES (2, 'Não');
INSERT INTO ppl (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela pop_sit_rua
INSERT INTO pop_sit_rua (id, nome) VALUES (1, 'Sim');
INSERT INTO pop_sit_rua (id, nome) VALUES (2, 'Não');
INSERT INTO pop_sit_rua (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela forma
INSERT INTO forma (id, nome) VALUES (1, 'Pulmonar');
INSERT INTO forma (id, nome) VALUES (2, 'Extrapulmonar');
INSERT INTO forma (id, nome) VALUES (3, 'Pulmonar + Extrapulmonar');
INSERT INTO forma (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela extra_pulm1
INSERT INTO extra_pulm1 (id, nome) VALUES (1, 'Pleural');
INSERT INTO extra_pulm1 (id, nome) VALUES (2, 'Gang. Perif.');
INSERT INTO extra_pulm1 (id, nome) VALUES (3, 'Geniturinária');
INSERT INTO extra_pulm1 (id, nome) VALUES (4, 'Óssea');
INSERT INTO extra_pulm1 (id, nome) VALUES (5, 'Ocular');
INSERT INTO extra_pulm1 (id, nome) VALUES (6, 'Miliar');
INSERT INTO extra_pulm1 (id, nome) VALUES (7, 'Meningoencefálico');
INSERT INTO extra_pulm1 (id, nome) VALUES (8, 'Cutânea');
INSERT INTO extra_pulm1 (id, nome) VALUES (9, 'Laringea');
INSERT INTO extra_pulm1 (id, nome) VALUES (10, 'Outra');

-- Inserções para a tabela aids
INSERT INTO aids (id, nome) VALUES (1, 'Sim');
INSERT INTO aids (id, nome) VALUES (2, 'Não');
INSERT INTO aids (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela alcoolismo
INSERT INTO alcoolismo (id, nome) VALUES (1, 'Sim');
INSERT INTO alcoolismo (id, nome) VALUES (2, 'Não');
INSERT INTO alcoolismo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela diabetes
INSERT INTO diabetes (id, nome) VALUES (1, 'Sim');
INSERT INTO diabetes (id, nome) VALUES (2, 'Não');
INSERT INTO diabetes (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela doenca_mental
INSERT INTO doenca_mental (id, nome) VALUES (1, 'Sim');
INSERT INTO doenca_mental (id, nome) VALUES (2, 'Não');
INSERT INTO doenca_mental (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela droga_ilicita
INSERT INTO droga_ilicita (id, nome) VALUES (1, 'Sim');
INSERT INTO droga_ilicita (id, nome) VALUES (2, 'Não');
INSERT INTO droga_ilicita (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela tabagismo
INSERT INTO tabagismo (id, nome) VALUES (1, 'Sim');
INSERT INTO tabagismo (id, nome) VALUES (2, 'Não');
INSERT INTO tabagismo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela outra_doenca
INSERT INTO outra_doenca (id, nome) VALUES (1, 'Sim');
INSERT INTO outra_doenca (id, nome) VALUES (2, 'Não');
INSERT INTO outra_doenca (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela raio_x
INSERT INTO raio_x (id, nome) VALUES (1, 'Suspeito');
INSERT INTO raio_x (id, nome) VALUES (2, 'Normal');
INSERT INTO raio_x (id, nome) VALUES (3, 'Outra patologia');
INSERT INTO raio_x (id, nome) VALUES (4, 'Não realizado');
INSERT INTO raio_x (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela hiv
INSERT INTO hiv (id, nome) VALUES (1, 'Positivo');
INSERT INTO hiv (id, nome) VALUES (2, 'Negativo');
INSERT INTO hiv (id, nome) VALUES (3, 'Em andamento');
INSERT INTO hiv (id, nome) VALUES (4, 'Não realizado');
INSERT INTO hiv (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela cultura_escarro
INSERT INTO cultura_escarro (id, nome) VALUES (1, 'Positiva');
INSERT INTO cultura_escarro (id, nome) VALUES (2, 'Negativa');
INSERT INTO cultura_escarro (id, nome) VALUES (3, 'Em andamento');
INSERT INTO cultura_escarro (id, nome) VALUES (4, 'Não realizada');
INSERT INTO cultura_escarro (id, nome) VALUES (9, 'Ignorado');

INSERT INTO situacao_encerra (id, nome) VALUES (1, 'Cura');
INSERT INTO situacao_encerra (id, nome) VALUES (2, 'Abandono');
INSERT INTO situacao_encerra (id, nome) VALUES (3, 'Falência');
INSERT INTO situacao_encerra (id, nome) VALUES (4, 'Óbito por tuberculose');
INSERT INTO situacao_encerra (id, nome) VALUES (5, 'Óbito por outras causas');
INSERT INTO situacao_encerra (id, nome) VALUES (7, 'Transferência');
INSERT INTO situacao_encerra (id, nome) VALUES (8, 'Mudança de diagnóstico');
INSERT INTO situacao_encerra (id, nome) VALUES (9, 'Drogas resistentes');
INSERT INTO situacao_encerra (id, nome) VALUES (10, 'Não encerrado');
INSERT INTO situacao_encerra (id, nome) VALUES (99, 'Ignorado');

-- Inserções para a tabela sexo
INSERT INTO sexo (id, nome) VALUES (1, 'Masculino');
INSERT INTO sexo (id, nome) VALUES (2, 'Feminino');
INSERT INTO sexo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela raca
INSERT INTO raca (id, nome) VALUES (1, 'Branca');
INSERT INTO raca (id, nome) VALUES (2, 'Preta');
INSERT INTO raca (id, nome) VALUES (3, 'Amarela');
INSERT INTO raca (id, nome) VALUES (4, 'Parda');
INSERT INTO raca (id, nome) VALUES (5, 'Indígena');
INSERT INTO raca (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela faixa_etar
INSERT INTO faixa_etar (id, nome) VALUES (1, 'Ignorado');
INSERT INTO faixa_etar (id, nome) VALUES (2, '<1 Ano');
INSERT INTO faixa_etar (id, nome) VALUES (3, '1-4');
INSERT INTO faixa_etar (id, nome) VALUES (4, '5-9');
INSERT INTO faixa_etar (id, nome) VALUES (5, '10-14');
INSERT INTO faixa_etar (id, nome) VALUES (6, '15-19');
INSERT INTO faixa_etar (id, nome) VALUES (7, '20-39');
INSERT INTO faixa_etar (id, nome) VALUES (8, '40-59');
INSERT INTO faixa_etar (id, nome) VALUES (9, '60-64');
INSERT INTO faixa_etar (id, nome) VALUES (10, '65-69');
INSERT INTO faixa_etar (id, nome) VALUES (11, '70-79');
INSERT INTO faixa_etar (id, nome) VALUES (12, '80+');

INSERT INTO uf (id, nome) VALUES
(12, 'Acre'),
(27, 'Alagoas'),
(13, 'Amazonas'),
(16, 'Amapá'),
(29, 'Bahia'),
(23, 'Ceará'),
(53, 'Distrito Federal'),
(32, 'Espírito Santo'),
(52, 'Goiás'),
(21, 'Maranhão'),
(31, 'Minas Gerais'),
(50, 'Mato Grosso do Sul'),
(51, 'Mato Grosso'),
(15, 'Pará'),
(25, 'Paraíba'),
(26, 'Pernambuco'),
(22, 'Piauí'),
(41, 'Paraná'),
(33, 'Rio de Janeiro'),
(24, 'Rio Grande do Norte'),
(43, 'Rio Grande do Sul'),
(11, 'Rondônia'),
(14, 'Roraima'),
(42, 'Santa Catarina'),
(28, 'Sergipe'),
(35, 'São Paulo'),
(17, 'Tocantins');

"""