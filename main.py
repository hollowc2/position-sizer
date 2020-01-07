from flask import Flask, render_template, flash
from forms import DataForm

app = Flask(__name__)
app.secret_key = 'buttfuck69'


@app.route('/', methods = ['GET', 'POST'])
def position_sizer():
    form = DataForm()
    if form.validate_on_submit():
        size = ( (form.trading_capital.data * (form.risk.data/100)) / ( (form.entry.data - form.exit.data) if form.direction.data == 'long' else (form.exit.data- form.entry.data)) )
        if form.base_pair.data != "usd" :
            size = round(size, 8)
        return render_template('position_sizer.html', size=size)
    return render_template('position_sizer.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)
