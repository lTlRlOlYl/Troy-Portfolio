from flask import url_for

class ProjectPortfolio():
    title = "Portfolio"
    index_desc = "The project page for the site you're currently viewing."
    live_link = "https://troypappas.azurewebsites.net/"
    code_link = "https://github.com/lTlRlOlYl/Troy-Portfolio"
    intro_text = '''
A portfolio project based on the Dopefolio template by Ram Maheshwari.
'''
    primary_text = [
'''
This project is based off a template I came across on social media. 
I chose to refactor the original code to be served by Flask, 
and hosted it on Azure's app service.
''',
    ]
    tools_used = [
        "Python",
        "Flask",
        "SASS",
        "HTML",
        "CSS",
        "JavaScript",
        "Azure App Service"
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
    primary_text = [
'''
The data for this came as a table in excel, in an entity-attribute-value format 
consisting of town, year, and amount. Publicly available shapefiles were downloaded.
Some SQL data manipulation was required. Windowing functions were used to facilite some of the 
partitioned aggregates on the dashboard. 
Parameters were leveraged in Tableau to implement the measure and gradient controls.
''',
    ]
    tools_used = [
        "Tableau",
        "T-SQL",
        "SQL Server",
        "Excel"
    ]



class ProjectAutomation():
    title = "Business Process Automation"
    index_desc = "A solution that populates DevOps based on a custom business framework using data from other systems."
    live_link = ""
    code_link = "https://github.com/lTlRlOlYl/TFS-Automation"
    intro_text = '''
An end-to-end streamlining of a business framework for a data analytics team.
'''
    primary_text = [
'''
The organization that this case is based on uses a number of systems to manage their operational data. 
This solution uses a python program to scan these systems for the initialization of new projects, 
then creates a DevOps workflow based on the data analytics unit's business framework.
''',
'''
The python program is designed to create a workflow based on new projects in DevOps as soon as they're created in the other systems by 
users outside the data analytics unit. The workflow involves more than fifty work items in a hierarchy structure, 
that need to be assigned based on file system data. The program sends detailed notification emails for workflow creation and assignment, 
as well as a dynamically populated MS Word template.
''',
'''
This solution also involves ETL from the DevOps operational data store and other systems 
to create an integrated data model using SQL Server. A hosted Power BI report built off the data model 
provides a streamlined and fully integrated view of all the work items, with color for status indication and hyperlinks 
to the work items for fast and intuitive navigation.
''',
'''
The solution enables accurate and timely reporting on the data analytics unit's metrics, 
in additional to saving hundreds of hours of manual data entry.
''',
'''
There's no active link, but feel free to check out the code on GitHub using the button below. 
Parts of the solution have been omitted to protect the organization's privacy.
''',
    ]
    tools_used = [
        "Python",
        "Azure DevOps",
        "SQL Server",
        "Power BI"
    ]


# class ProjectApp():
#     title = "LoreGate"
#     index_desc = "An independent proof-of-concept I came up with to guide me through learning the Flask framework."
#     live_link = ""
#     code_link = ""
#     intro_text = ""
#     primary_text = [
# '''
# ''',
#     ]
#     tools_used = []


# class ProjectNLP():
#     title = ""
#     index_desc = ""
#     live_link = ""
#     code_link = ""
#     intro_text = ""
#     primary_text = [
# '''
# ''',
#     ]
#     tools_used = []


