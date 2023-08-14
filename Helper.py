import re


# Remove the space
def clean(item):
    return item.strip()


# Delete the min and remove the space
def clean_duration(duration):
    if duration != "Unknown":
        duration = re.findall(r"\d+", duration)[0]
        return int(duration)
    else:
        return duration


# Delete the bracket and remove the space and make it int
def clean_year(year):
    if year != "Unknown":
        year = re.findall(r"\d+", year)[0]
        return int(year)
    else:
        return year


# Delete , and return the int
def clean_gross(gross):
    if gross != "Unknown":
        gross = re.findall(r"\d+", gross)
        gross = "".join(gross)
        return int(gross)
    else:
        return gross


# Str To Int
def metascore_to_int(item):
    if item != "Unknown":
        return int(item)
    else:
        return item