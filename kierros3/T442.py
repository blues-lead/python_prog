def compare_floats(luku1, luku2, eps):
    """
    The function compares absolute difference of two floats. Two floats are the same
    if their absolute difference is less than the EPSILON
    :param luku1: first float
    :param luku2: second float
    :param eps: epsilon - error between two floats
    :return: true of false (same/not same)
    """
    if abs(luku1-luku2) < eps:
        return True
    else:
        return False
