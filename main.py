#def to_hms(seconds: int) -> list:
"""
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
"""
    # Type your code below
def to_hms(seconds):
  """converting a input of seconds into a list in the form [hours, minutes, seconds].
  If input is not an integer, output an error message"""
  if type(seconds) != int:
    print("Unsupported input type.")
  else:
    h,s = divmod(int(seconds),3600)
    m,s = divmod(s,60)
    return [h,m,s]
  pass

