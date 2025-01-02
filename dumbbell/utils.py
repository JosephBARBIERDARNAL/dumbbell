def _is_numerical(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
