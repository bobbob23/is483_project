from IPython.terminal.embed import InteractiveShellEmbed
from flask import jsonify

def run_script_with_ipython(script_path=r"/Users/deborahhow/Documents/Y3S2/FYP/is483_project/TSH_Application/backend/ML/logRegModel.py"):
    ipshell = InteractiveShellEmbed()
    ipshell.magic('run ' + script_path)

    return jsonify({
        'isPredicted': True,
        'message': 'Applicant\'s prediction has been received!'
    })

