import re

def match_concerns(description, concerns):
    for concern in concerns:
        pattern = re.compile(concern, re.IGNORECASE)
        if pattern.search(description):
            return True
    return False

def match_exclusions(description, exclusions):
    for exclude in exclusions:
        pattern = re.compile(exclude, re.IGNORECASE)
        if pattern.search(description):
            return True
    return False
