def validate_jstone(text):
  """Determines if the text is valid jstone or not"""
  pass

def cannonicalize_jstone(text, hasher, return_all=false):
  """Determines the cannonical form for the jstone text and returns it.

  arguments:
  text -- the JSTONE text to be cannonicalized.
  hasher -- a hash function that returns a binary hash of a binary input.

  keyword arguments:
  return_all -- If True, this function returns a dictionary where the values are every cannonicalized component of the text document and the keys are their associated hashes.
  """
  pass

def expand_jstone(text, resolver):
  """Eliminates all references to other JSTONE documents within the JSTONE document text and returns the new document. 

  arguments:
  text -- the JSTONE text to be expanded.
  resolver -- a function that takes a binary hash and returns the binary data associated with it. 
  """
  pass

