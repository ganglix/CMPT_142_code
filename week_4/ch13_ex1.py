# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry", "bubblegum")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Afan": 'vanilla',
          "Janet": 'vanilla',
          "Kelei": 'strawberry',
          "Lilith": 'vanilla',
          "Chaz": 'vanilla',
          "Dominick": 'chocolate',
          "Gang": 'bubblegum',
          }

"""
Algorithm
input: survey, {name: flavour}
return: flavour_vote, {flavour: vote}
check every entry in survey
    put the flavor name down when we first see it and record 1
    next time if we see the same flavour, add 1 that that count
keep doing so until we checked every entry in survey
"""

def process_survey(survey):
    """
    Take a survey of flavour vote, and return number of vote for each flavour as a dictionary
    input: survey, dict, {name: flavour}
    return: flavour_vote, dict, {flavour: vote}
    """
    # initiate dict
    flavour_vote = {}   # flavour : vote

    # check every entry in survey
    for name in survey:
        flavour = survey[name]
        #put the flavor name down to flavour_vote when we first see it and initialize as 0
        if flavour not in flavour_vote:
            flavour_vote[flavour] = 0
        # anyways, add 1 to that count
        flavour_vote[flavour] += 1

        #keep doing so until we checked every entry in survey
    return flavour_vote

survey_results = process_survey(survey)
print(survey_results)