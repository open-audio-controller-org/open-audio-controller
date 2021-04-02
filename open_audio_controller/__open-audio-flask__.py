from flask import Flask, render_template, request, logging
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/controller_state', methods=['POST'])
def controller_state():
    content = request.json
    state = content.state
    if state == 'true':
        app.logger.info('Turning on Module')
    elif state == 'false':
        app.logger.info('Turning off module')
    else:
        app.logger.info('No state found')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)