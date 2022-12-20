from app import db
from sqlalchemy import ForeignKey
from datetime import datetime


class TramsportadoraModular(db.Model):
    __tablename__ = "TrackingModular"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    idModular = db.Column(db.Integer)
    tipo = db.Column(db.String)
    Documento = db.Column(db.String)
    urlpagina = db.Column(db.String)
    ultimareposicao = db.Column(db.DateTime, unique=False, nullable=False)
    notafiscal = db.Column(db.Integer)
    entrega = db.Column(db.DateTime, unique=False, nullable=False)
    destinatario = db.Column(db.String)
    remetente = db.Column(db.String)
    emissao = db.Column(db.DateTime, unique=False, nullable=False)
    cpf_cnpj = db.Column(db.String)
    nome = db.Column(db.String)
    endereco = db.Column(db.String)
    cidade = db.Column(db.String)
    filial = db.Column(db.String)
    serie = db.Column(db.Integer)
    chaveacessocte = db.Column(db.String)
    previsaoentrega = db.Column(db.DateTime, unique=False, nullable=False)
    recebidopor = db.Column(db.String)
    natureza = db.Column(db.String)
    especie = db.Column(db.String)
    volumes = db.Column(db.String)
    peso = db.Column(db.Float)
    cubagem = db.Column(db.Float)
    valormecadorias = db.Column(db.Float)
    urlpdf = db.Column(db.String)
    urlxml = db.Column(db.String)
    statusnf = db.Column(db.String)
    datastatus = db.Column(db.String)
    referenciaproduto = db.Column(db.String)


class Categorias(db.Model):
    __tablename__ = "Dim_Categoria"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Categoria = db.Column(db.Integer)
    Cod_Categoria = db.Column(db.String)
    Nome_Categoria = db.Column(db.String)


class Tempo(db.Model):
    __tablename__ = "Dim_Tempo"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Tempo = db.Column(db.Integer)
    Cod_Dia = db.Column(db.String)
    DatadIA = db.Column(db.String)
    Cod_Semana = db.Column(db.String)
    Nome_Dia_Semana = db.Column(db.String)
    Codigo_Mes = db.Column(db.String)
    Nome_Mes = db.Column(db.String)
    Cod_Mes_Ano = db.Column(db.String)
    Nome_Mes_Ano = db.Column(db.String)
    Cod_Trimestre = db.Column(db.String)
    Nome_Trimestre = db.Column(db.String)
    Cod_Trimestre_Ano = db.Column(db.String)
    Nome_Trimeste_Ano = db.Column(db.String)
    Cod_Semestre = db.Column(db.String)
    Nome_Semestre = db.Column(db.String)
    Cod_Semestre_Ano = db.Column(db.String)
    Nome_Semestre_Ano = db.Column(db.String)
    Ano = db.Column(db.String)
    BitSemana = db.Column(db.Boolean, nullable=False)

class Faturamento(db.Model):
    __tablename__ = "Dim_Categoria"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    IdFaturamento = db.Column(db.Integer)
    Faturamento = db.Column(db.Float)
    Imposto = db.Column(db.Float)
    Custo_Variavel = db.Column(db.Float)
    Quantidade_Vendida = db.Column(db.Float)
    Unidades_Vendidas = db.Column(db.Float)


class Produtos(db.Model):
    __tablename__ = "Dim_Produto"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_produto = db.Column(db.Integer)
    Cod_Produto = db.Column(db.String)
    Cod_Marca = db.Column(db.String)
    NomeProduto = db.Column(db.String)
    Marca = db.Column(db.String)

class Loja(db.Model):
    __tablename__ = "Dim_Loja"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Loja = db.Column(db.Integer)
    Cod_Loja = db.Column(db.String)
    Desc_Loja = db.Column(db.String)

class MarcaProduto(db.Model):
    __tablename__ = "Dim_Marca"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Marca = db.Column(db.Integer)
    Cod_Marca = db.Column(db.String)
    Desc_Marca = db.Column(db.String)
    Marca = db.Column(db.String)
    PrazoMarca = db.Column(db.DateTime, unique=False, nullable=False)
    BitAtivo = db.Column(db.Boolean, nullable=False)


class Fretes(db.Model):
    __tablename__ = "Dim_Frete"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Frete = db.Column(db.Integer)
    CodFrete =db.Column(db.String)
    uf =db.Column(db.String)
    estado =db.Column(db.String)
    cidade =db.Column(db.String)
    valor = db.Column(db.Float)
    peso = db.Column(db.Float)
    data_frete = db.Column(db.DateTime, unique=False, nullable=False)
    hora_frete = db.Column(db.String)
    cep =db.Column(db.String)
    transportadora = db.Column(db.String)


class Fornecedor(db.Model):
    __tablename__ = "Dim_Fabrica"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Fabrica = db.Column(db.Integer)
    Desc_Fabrica = db.Column(db.String)
    Marca = db.Column(db.String)
    BitAtivo = db.Column(db.Boolean, nullable=False)


class Estoque(db.Model):
    __tablename__ = "Dim_Estoque"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Estoque = db.Column(db.Integer)
    Cod_Estoque = db.Column(db.String)
    Desc_Estoque =db.Column(db.String)
    Quantidade = db.Column(db.Float)
    Data_Alteracao = db.Column(db.DateTime, unique=False, nullable=False)
    Cod_Produto = db.Column(db.String)


class Cliente(db.Model):
    __tablename__ = "Dim_Cliente"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Cliente = db.Column(db.Integer)
    cod_cliente = db.Column(db.String)
    Desc_Cliente =db.Column(db.String)
    Cod_Cidade = db.Column(db.Integer)
    Desc_Cidade = db.Column(db.String)
    Cod_Estado = db.Column(db.String)
    Cod_Regiao = db.Column(db.String)
    Desc_Regiao = db.Column(db.String)
    Cod_Segmento = db.Column(db.String)
    Desc_Segmento = db.Column(db.String)
    BitAtivo = db.Column(db.Boolean, nullable=False)


class Cidade(db.Model):
    __tablename__ = "Dim_Cidade"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Cidade = db.Column(db.Integer)
    Cod_Cidade = db.Column(db.Integer)
    Desc_Cidade = db.Column(db.String)
    Uf_Cidade = db.Column(db.String)


class Categorias(db.Model):
    __tablename__ = "Dim_Categoria"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_Categoria = db.Column(db.Integer)
    Cod_Categoria =db.Column(db.String)
    Nome_Categoria = db.Column(db.String)


class FatoCustos(db.Model):
    __tablename__ = "Fato_Custos"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_FatoCustos = db.Column(db.Integer)
    CustoFornecedor = db.Column(db.Float)
    CustoFrete = db.Column(db.Float)


class FatoFaturamento(db.Model):
    __tablename__ = "Fato_Faturamento"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    IdFaturamento = db.Column(db.Integer)
    Faturamento = db.Column(db.Float)
    Imposto = db.Column(db.Float)
    Custo_Variavel = db.Column(db.Float)
    Quantidade_Vendida = db.Column(db.Float)
    Unidades_Vendidas = db.Column(db.Float)


class FatoPedido(db.model):
    __tablename__ = "Fato_Pedido"
    __bind_key__ = 'appdw'
    __table_args__ = {"schema": "dbo"}
    Id_FatoPedido = db.Column(db.Integer)
    Cod_CodCliente = db.Column(db.String)
    Cod_Marca = db.Column(db.String)
    Cod_produto =db.Column(db.String)
    cod_vendedor = db.Column(db.String)
    SKU = db.Column(db.String)
    Cod_Barras = db.Column(db.String)
    dataVenda = db.Column(db.DateTime, unique=False, nullable=False)
    horaVenda =db.Column(db.String)
    EstoqueProdutVenda =db.Column(db.Float)
    NomeProduto =db.Column(db.String)
    Marca = db.Column(db.String)
    Preco = db.Column(db.Float)
    Custo = db.Column(db.Float)
    Frete = db.Column(db.Float)
    Margem = db.Column(db.Float)
    Pagamento = db.Column(db.String)
    Loja = db.Column(db.String)
    Prazo = db.Column(db.Float)
    Quantidade = db.Column(db.Float)













 