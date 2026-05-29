CREATE DATABASE db_stokky;
USE db_stokky;

-- EMPRESA
CREATE TABLE tb_empresa (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_nome VARCHAR(255) NOT NULL,
    emp_cnpj VARCHAR(20) NOT NULL UNIQUE,
    emp_email VARCHAR(255) NOT NULL,
    emp_tel VARCHAR(15) NOT NULL,
    emp_cep VARCHAR(9) NOT NULL,
    emp_rua VARCHAR(255) NOT NULL,
    emp_numero VARCHAR(10) NOT NULL,
    emp_complemento VARCHAR(100),
    emp_bairro VARCHAR(255) NOT NULL,
    emp_cidade VARCHAR(255) NOT NULL,
    emp_estado CHAR(2) NOT NULL,
    emp_pais VARCHAR(100) NOT NULL,
    emp_data_criacao DATE NOT NULL
);

-- USUARIO
CREATE TABLE tb_usuario (
    usu_id INT AUTO_INCREMENT PRIMARY KEY,
    usu_nome VARCHAR(255) NOT NULL,
    usu_email VARCHAR(255) NOT NULL UNIQUE,
    usu_senha VARCHAR(255) NOT NULL,
    usu_tel VARCHAR(15) NOT NULL,
    usu_cargo VARCHAR(45) NOT NULL
);

-- PRODUTO
CREATE TABLE tb_produto (
    pro_id INT AUTO_INCREMENT PRIMARY KEY,
    pro_nome VARCHAR(100) NOT NULL,
    pro_descricao VARCHAR(255) NOT NULL,
    pro_marca VARCHAR(100) NOT NULL,
    pro_preco DECIMAL(10,2) NOT NULL,
    pro_data_validade DATE NOT NULL,
    pro_emp_id INT NOT NULL,
    FOREIGN KEY (pro_emp_id) REFERENCES tb_empresa(emp_id)
);

-- ESTOQUE
CREATE TABLE tb_estoque (
    est_id INT AUTO_INCREMENT PRIMARY KEY,
    est_quantidade INT NOT NULL,
    est_pro_id INT NOT NULL UNIQUE,
    FOREIGN KEY (est_pro_id) REFERENCES tb_produto(pro_id)
);

-- MOVIMENTACAO
CREATE TABLE tb_movimentacao (
    mov_id INT AUTO_INCREMENT PRIMARY KEY,
    mov_tipo ENUM('entrada', 'saida') NOT NULL,
    mov_quantidade INT NOT NULL,
    mov_data_movimentacao DATETIME NOT NULL,
    mov_pro_id INT NOT NULL,
    mov_usu_id INT NOT NULL,
    FOREIGN KEY (mov_pro_id) REFERENCES tb_produto(pro_id),
    FOREIGN KEY (mov_usu_id) REFERENCES tb_usuario(usu_id)
);

# Dados ficticios para teste

INSERT INTO tb_usuario (usu_nome, usu_email, usu_senha, usu_tel, usu_cargo) VALUES 
('Ana','ana@gmail.com','123','(19)99999-9999','Admin');

INSERT INTO tb_empresa (
    emp_nome,
    emp_cnpj,
    emp_email,
    emp_tel,
    emp_cep,
    emp_rua,
    emp_numero,
    emp_complemento,
    emp_bairro,
    emp_cidade,
    emp_estado,
    emp_pais,
    emp_data_criacao
) VALUES 
(
    'Mercado Bom Preco',
    '12.345.678/0001-10',
    'contato@mercadobompreco.com',
    '(11) 4002-8922',
    '06700-000',
    'Rua das Palmeiras',
    '150',
    'Loja A',
    'Centro',
    'Cotia',
    'SP',
    'Brasil',
    '2024-01-15'
),

(
    'Farmacia Vida Mais',
    '23.456.789/0001-55',
    'atendimento@vidamais.com',
    '(11) 98888-7777',
    '06000-120',
    'Avenida Sao Joao',
    '850',
    NULL,
    'Jardim America',
    'Osasco',
    'SP',
    'Brasil',
    '2023-08-10'
),

(
    'TechStorm Hardware',
    '98.765.432/0001-99',
    'suporte@techstorm.com',
    '(11) 3777-9900',
    '04567-890',
    'Rua da Tecnologia',
    '999',
    'Galpao 2',
    'Distrito Industrial',
    'Sao Paulo',
    'SP',
    'Brasil',
    '2025-03-01'
);