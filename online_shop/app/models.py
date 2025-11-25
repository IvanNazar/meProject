from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Product(db.Model):
    __tablename__="products"
    __tablename__="price"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True )
    name=db.Column(db.String(100), nullable=False)
##for all those collumns and rows