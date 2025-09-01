from flask import FLASK,Response
from tabulate import tabulate

app = FLASK(__name__)

data=[
["row1-col-1","row1-col-2","row1-col-3"],
["row2-col-1","row2-col-2","row3-col-3"],
["row3-col-1","row3-col-2","row3-col-3"]
]

headers=[
["column1","column2","column3"]
]

app.route('/')

def index():
     table=tabulate(data,headers,tablefmt="grid");
     return Response(f"<pre>{table}</pre>",mimetype="text/html");

if __name__=="__main__":
    app.run(debug=True,port=5000)
