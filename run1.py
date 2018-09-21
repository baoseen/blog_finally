from flask import Flask,render_template
import flask

app = Flask(__name__)

@app.route('/temp')
def temp():
    dic = {
        'title':'我的第一个模板',
        'bookname':'《钢铁是怎样炼成的》',
    }
    print(locals())
    return render_template('temp.html', params=locals())

# locals('title':'我的第一个模板',
#         'bookname':'《钢铁是怎样炼成的》',)={
#
# }

if __name__=='__main__':
    app.run(debug=True)