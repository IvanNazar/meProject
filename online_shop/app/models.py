from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Product(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True )
    name=db.Column(db.String(100), nullable=False)
    pricename=db.Column(db.Float, nullable=False)
##for all those collumns and rows
created_at = db.Column(db.DateTime, default=db.func.now())
updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
description =db.Column(db.Text, nullable=True)
