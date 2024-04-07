from IPython.terminal.embed import InteractiveShellEmbed
from flask import jsonify

def run_script_with_ipython(script_path=r""):
    ipshell = InteractiveShellEmbed()
    ipshell.magic('run ' + script_path)

    return jsonify({
        'isPredicted': True,
        'message': 'Applicant\'s prediction has been received!'
    })

