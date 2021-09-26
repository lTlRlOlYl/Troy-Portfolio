class ProjectPortfolio():
    title = "Portfolio"
    index_desc = "The project page for the site you're currently viewing."
    live_link = "https://troypappas.azurewebsites.net/"
    code_link = "https://github.com/lTlRlOlYl/Troy-Portfolio"
    intro_text = '''
A portfolio project based on the
<a href="https://dopefolio.netlify.app/">Dopefolio</a> template by
<a href="https://rammaheshwari.com">Ram Maheshwari</a>.
'''
    primary_text = '''
This project is based off a template I came across on social media. 
I chose to refactor the original code to be served by Flask, 
and hosted it on Azure's app service.<br>
'''
    tools_used = [
        "Python",
        "Flask",
        "SASS",
        "HTML",
        "CSS",
        "JavaScript",
        "Azure"
    ]

class ProjectMap():
    title = "Interactive Map"
    index_desc = "An interactive map of election costs in Massachusetts municipalities."
    live_link = "https://public.tableau.com/app/profile/troy.pappas/viz/ExampleVisualization/Sheet12"
    code_link = ""
    intro_text = '''
A map of historical election costs for the Commonwealth of Massachusetts, 
with inbuilt functionality for switching between measures, adjusting the gradient, and more.
'''
    primary_text = '''
The data for this came as a table in excel, in an entity-attribute-value format 
consisting of town, year, and amount. Publically available shapefiles were downloaded.
Some SQL data manipulation was required. Windowing functions were used to facilite some of the 
partitioned aggregates on the dashboard. 
Parameters were leveraged in Tableau to implement the measure and gradient controls.
'''
    tools_used = [
        "Tableau",
        "T-SQL",
        "SQL Server",
        "Excel"
    ]

class ProjectApp():
    title = "LoreGate"
    index_desc = "An independent proof-of-concept I came up with to guide me through learning the Flask framework."
    live_link = ""
    code_link = ""
    intro_text = ""
    primary_text = ""
    tools_used = []

class ProjectNLP():
    title = ""
    index_desc = ""
    live_link = ""
    code_link = ""
    intro_text = ""
    primary_text = ""
    tools_used = []


