import os
from flask import Flask, render_template, send_from_directory, abort
from project_data import ProjectPortfolio, ProjectApp, ProjectMap, ProjectNLP

app = Flask(__name__)

@app.route('/')
def index():
    portfolio_project = ProjectPortfolio()
    map_project = ProjectMap()
    return render_template(
        'index.html', 
        portfolio_project=portfolio_project, 
        map_project=map_project
        )

@app.route('/project/<name>')
def project(name):
    # project_data = ProjectData(name)
    # return render_template('project.html', project_data=project_data)
    if name == 'portfolio':
        project_data = ProjectPortfolio()
        return render_template('project.html', project_data=project_data)
    elif name == 'map':
        project_data = ProjectMap()
        return render_template('project.html', project_data=project_data)
    return render_template('unavailable.html')

@app.route("/resume_download")
def resume_download():
    try:
        basepath = os.path.join(os.path.dirname(__file__), 'static')
    except Exception:
        abort(404)
    return send_from_directory(basepath, 'troy_pappas_resume.pdf', as_attachment=True)
