def hey(phrase):
    phrase = phrase.strip()
    if phrase == '':
    	return "Fine. Be that way!"
    elif phrase.isupper():
    	if phrase[-1] == '?':
    		return "Calm down, I know what I'm doing!"
    	else:
    		return "Whoa, chill out!"
    elif phrase[-1] == '?':
    	return "Sure."
    else:
    	return "Whatever."