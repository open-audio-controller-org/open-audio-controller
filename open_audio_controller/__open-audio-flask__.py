from flask import Flask, render_template, request, logging, json, make_response, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/controller_state', methods=['POST'])
def controller_state():
    content = request.get_json(force=True)
    state = content["state"]
    if state == True:
         app.logger.info('Turning on Module')
    elif state == False:
         app.logger.info('Turning off module')
    else:
         app.logger.info('No state found')
         
    return jsonify(state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)