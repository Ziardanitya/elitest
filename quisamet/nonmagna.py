headers_base = {
    'User-Agent': 'Your User Agent String',
    'Accept': 'application/json',
    # other headers...
}

# Assuming input.pulse is a variable or an attribute from an object
pulse_value = input.pulse

# Adding the pulse key-value pair to the dictionary
headers_base['pulse'] = pulse_value

# Now headers_base includes the pulse key-value pair
print(headers_base)
