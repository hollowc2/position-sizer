from wtforms import IntegerField, SelectField, RadioField, DecimalField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    base_pair       = SelectField('Base Pair', choices=[ ('usd', 'USD'),('btc', 'BTC'), ('eth', 'ETH'), ('bnb', 'BNB')], default='usd', validators=[DataRequired()])
    direction       = RadioField('Direction', choices=[('long', 'Long'), ('short', 'Short')], default='long', validators=[DataRequired()])
    trading_capital = DecimalField('Trading Capital', default=2000, validators=[DataRequired()])
    entry           = DecimalField('Entry Price', default=14, validators=[DataRequired()])
    exit            = DecimalField('Stop Loss', default=10, validators=[DataRequired()])
    risk            = DecimalField('Risk Percentage', default=1, validators=[DataRequired()])
    submit          = SubmitField('Submit')
