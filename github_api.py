import requests, json
import pprint
import config
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas

# directions for getting a token- gist.github.com/christopheranderton/8644743
TOKEN = getattr(config, 'GITHUB_TOKEN', 'default value if not found')

# this function was made to give proof we were contributing to our capstone repo which was under NDA and this was all we could share.
def create_output_file():
    with open("commits.txt", "w") as text_file:
        # go through each commit in each branch
        for branch in repo:
            text_file.write("BRANCH_NAME: " + branch['name'])
            text_file.write("\n")
            sha = branch['commit']['sha']
            commits = requests.get(get_commits.replace("SHAFILL", sha)).json()
            for commit in commits:
                resp = {"COMMIT AUTHOR--- ": commit['commit']['author'],
                        "COMMIT MESSAGE--- ": commit['commit']['message'],
                        "COMMIT SHA--- ": commit['commit']['tree']}
                text_file.write(pprint.pformat(resp))
                text_file.write("\n")
            text_file.write("\n")

# this function is just a simple example of one way this data could interact with pandas
def pandas_metrics(repo):
    authors_commits_dict = {}
    for branch in repo:
        sha = branch['commit']['sha']
        commits = requests.get(get_commits.replace("SHAFILL", sha)).json()
        for commit in commits: 
            author = commit['commit']['author']['name']
            # account for my two names
            if author in "Steven Tucker":
                author = "slidingsteven"
            # if the author is in the author dictionary then increment their tally
            if author in authors_commits_dict:
                authors_commits_dict[author] = authors_commits_dict[author] + 1
            # else, add them to the dict
            else: 
                authors_commits_dict[author] = 1
    df = DataFrame(authors_commits_dict.items(), columns=['Authors', 'Commits'])      
    # # show the data set
    print (df)
    df.plot(x='Authors', y ='Commits', kind = 'bar')
    # # show graph 
    plt.show()

# https://api.github.com/repos/:user/:repo/branches
get_branches = 'https://api.github.com/repos/slidingsteven/SecurityQuestionEvaluator/branches?access_token=' + TOKEN
get_commits = 'https://api.github.com/repos/slidingsteven/SecurityQuestionEvaluator/commits?per_page=100&sha=SHAFILL&access_token='+TOKEN

# get the set of branches on the repo
r = requests.get(get_branches)
# pretty print the output
pprint.pprint(r.json())
# give clear output for the number of branches
print("\n\n\nNumber of branches: " + str(len(r.json())))

# save the repo info 
repo = r.json()

# get the df of authors compared to their commits
pandas_metrics(repo)

# create an output file.
# this was just to prove to a TA we were working on our capstone since we were under NDA
# I left it here to show experience with creating an input/output file
create_output_file()# Output for this function can be viewed in the commits.txt file


# Other output not including the plot is below
"""[{'commit': {'sha': '07e11936f2ee27cacd76192426bd5687a1935d6b',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/07e11936f2ee27cacd76192426bd5687a1935d6b'},
  'name': 'ProductionBranch',
  'protected': False},
 {'commit': {'sha': 'f45e6565be3ceb7bd4c2890131659a3cf86620b8',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/f45e6565be3ceb7bd4c2890131659a3cf86620b8'},
  'name': 'activebranch',
  'protected': False},
 {'commit': {'sha': 'c57907c9b049a2440c592172423feed96cd07186',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/c57907c9b049a2440c592172423feed96cd07186'},
  'name': 'activewebsite',
  'protected': False},
 {'commit': {'sha': 'be1e0165de430ea6311f6c4e57ea6add84c788df',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/be1e0165de430ea6311f6c4e57ea6add84c788df'},
  'name': 'dependabot/pip/cryptography-2.3',
  'protected': False},
 {'commit': {'sha': 'f0036bcd8447fa4aafe5285c0ff2dfe45c818fb1',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/f0036bcd8447fa4aafe5285c0ff2dfe45c818fb1'},
  'name': 'dependabot/pip/pyxdg-0.26',
  'protected': False},
 {'commit': {'sha': 'abdefe634424da439a288dd9659cda4ab8fadd97',
             'url': 'https://api.github.com/repos/SlidingSteven/SecurityQuestionEvaluator/commits/abdefe634424da439a288dd9659cda4ab8fadd97'},
  'name': 'master',
  'protected': False}]



Number of branches: 6
                Authors  Commits
0         slidingsteven      340
1            Lisa Egede       49
2       dependabot[bot]        2
3  Imra Maududi Qureshi        3"""
