from flask import *
from dotenv import find_dotenv, load_dotenv
#from response import get_llm_response
from response import get_llm_responseTuned
#from ingest import ingestPDF

load_dotenv(find_dotenv(), override=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/getQueryResult', methods=['POST'])
# def getLLMResponse():
#     if request.method == 'POST':
#         data = request.get_json()
#         generated_response = get_llm_response(
#             query=data['query'],
#         )
#         return jsonify(generated_response)
#     else:
#         return 'Request should be POST only.'
    
@app.route('/getTunedResult', methods=['POST'])
def getLLMResponseTuned():
    if request.method == 'POST':
        data = request.get_json()
        generated_responseTuned = get_llm_responseTuned(
            query=data['query'],
        )
        return jsonify(generated_responseTuned)
    else:
        return 'Request should be POST only.'
    
# @app.route('/ingestPDF', methods=['POST'])
# def ingestPDFFunc():
#     if request.method == 'POST':
#         data = request.get_json()
#         response = ingestPDF(
#             docPath = data['documentName'],
#         )
#         return jsonify({'ingest_status': response})
#     else:
#         return 'Request should be POST only.'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)