from flask import Flask, render_template, request, logging, json, make_response, jsonify
from open_audio_controller.core import core_module
app = Flask(__name__)


core_module = core_module()


@app.route('/')
def index():
    """
    Parameters:
        ----------
        None.

    Returns
        --------
        A rendered version of index.html and a http response code 200
    
    The function renders the index page for the app
    
    """
    global core_module
    if not core_module: core_module = core_module() 
    return render_template('index.html')


@app.route('/controller_state', methods=['POST'])
def controller_state():
    """
    Parameters:
        ----------
        State: JSON object 
            The state of the audio module in use.


    Returns:
        ---------
        The Jsonified version of state
    
    Checks the value of state from the front end and
    activates/deactivates the module based on that state      


    """
    
    content = request.get_json(force=True)
    state = content["state"]
    if state == True:
        # app.logger.info('Turning on Module')
        print('Turning on Module')
        core_module.start_stream()
    elif state == False:
        print('Turning off module')
        core_module.end_stream()
    else:
        app.logger.info('No state found')

    return jsonify(state)

#@app.route('/spectrum', methods['GET'])
#def spectrum():
#    return jsonify(core_module.plot_data)


@app.route('/playback', methods =['POST'])
def playback():
    """
    Parameters:
        ----------
        State: JSON object 
          The state of the audio module in use.


    Returns:
        ---------
        The Jsonified version of state
    
    
    Checks the state value of the live feedback button
    from the front end sets the playback audio variable to
    true or false depending on said state
    
    """
    content=request.get_json(force=True)
    state = content["state"]
    if state == True:
        core_module.PLAYBACK_AUDIO=True
        app.logger.info('turning on playback')
    else:
        core_module.PLAYBACK_AUDIO=False
        app.logger.info('Turning off playback')
    return jsonify(state)    
        



if __name__ == '__main__':
    core_module = core_module()
    app.run(debug=True, host='0.0.0.0', port=5000)
