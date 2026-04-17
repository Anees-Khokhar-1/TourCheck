from rapidfuzz import process, fuzz

def match_or_create(new_name, existing_list, threshold=80):
    if not existing_list:
        return new_name

    # Try to find a similar existing category
    match = process.extractOne(
        new_name,
        existing_list,
        scorer=fuzz.token_sort_ratio
    )

    if match and match[1] >= threshold:
        return match[0] # Return the matched existing name
        
    return new_name # Return new name if no good match
