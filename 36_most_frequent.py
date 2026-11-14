def most_frequent(lst):
    if not lst:
        return None
    return max(set(lst), key=lst.count)