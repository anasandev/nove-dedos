create database db_9dedos;
use db_9dedos;

create table tb_empresa (
	emp_id int auto_increment primary key,
    emp_nome varchar(255) not null,
    emp_cnpj varchar(20) not null, 
    emp_email varchar(255) not null,
    emp_tel varchar(15) not null,
    emp_cep varchar (9) not null, 
    emp_rua varchar (255) not null,
    emp_numero varchar (10) not null,
    emp_complemento varchar (100),
    emp_bairro varchar (255) not null,
    emp_cidade varchar(255) not null,
    emp_estado char (2) not null,
    emp_pais varchar (100) not null,
    emp_data_criacao date not null
);

create table tb_usuario (
	usu_id int auto_increment primary key,
    usu_nome varchar(255) not null, 
    usu_email varchar(255) not null, 
    usu_senha varchar(255) not null,
    usu_tel varchar(15) not null,
    usu_cargo varchar(45) not null,
    usu_emp_id int,
    foreign key (usu_emp_id) references tb_empresa(emp_id)
);

create table tb_produto (
	pro_id INT PRIMARY KEY AUTO_INCREMENT,
    pro_nome VARCHAR(100) not null,
    pro_descricao varchar(255) not null,
    pro_marca VARCHAR(100) not null,
    pro_preco DECIMAL(10,2) not null,
    pro_data_validade DATE not null,
    pro_emp_id int,
    foreign key (pro_emp_id) references tb_empresa(emp_id)
);

create table tb_estoque(
	est_id int primary key auto_increment,
    est_quantidade int not null,
    est_pro_id int,
    foreign key (est_pro_id) references tb_produto(pro_id)
);

create table tb_movimentacao(
	mov_id int primary key auto_increment,
    mov_tipo enum('entrada', 'saida') not null,
    mov_quantidade int not null,
    mov_data_movimentacao datetime,
    mov_pro_id int,
    mov_est_id int,
    foreign key (mov_pro_id) references tb_produto(pro_id),
    foreign key (mov_est_id) references tb_estoque(est_id)
);

create table tb_categoria(
	cat_id int auto_increment primary key,
    cat_nome varchar(255) not null,
    cat_descricao varchar(255) not null,
    cat_pro_id int,
    foreign key (cat_pro_id) references tb_produto(pro_id)
);

create table tb_pedido(
	ped_id int auto_increment primary key,
    ped_data datetime not null,
    ped_status enum('pendente','pago','cancelado','enviado','entregue') not null,
    ped_valor_total decimal(10,2) not null, 
    ped_forma_pagamento varchar(50) not null,
    ped_data_pagamento datetime not null
);

create table tb_fornecedor(
	for_id int auto_increment primary key,
    for_nome varchar(255) not null,
    for_cnpj varchar(20) not null,
    for_tel varchar(15) not null,
    for_email varchar(255)not null,
    for_ped_id int,
    foreign key(for_ped_id) references tb_pedido(ped_id)
);

create table tb_item_pedido(
	ipe_id int auto_increment primary key,
    ipe_quantidade int not null,
    ipe_preco_unitario decimal(10,2) not null,
    ipe_pro_id int,
    ipe_usu_id int,
    ipe_ped_id int,
    foreign key (ipe_pro_id) references tb_produto(pro_id),
    foreign key (ipe_usu_id) references tb_usuario(usu_id),
    foreign key (ipe_ped_id) references tb_pedido(ped_id)
);

#Dados ficticios para teste

INSERT INTO tb_usuario (
  usu_nome,
  usu_email,
  usu_senha,
  usu_tel,
  usu_cargo
) VALUES (
  'Ana',
  'ana@gmail.com',
  '123',
  '(19)99999-9999',
  'Admin'
);

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
) VALUES (
  'Central1',
  '83.670.366/0001',
  'central@gmail.com',
  '(19)99999-9999',
  '02003-440',
  'rua um',
  '1001',
  'galpao 3',
  'Jardim secreto',
  'São Paulo',
  'sp',
  'Brasil',
  '2001-09-09'
  );