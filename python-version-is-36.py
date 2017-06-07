# is python version 3.6?
#
# oh hey. this is for driving out docker image wants for concourse
# run with the interpreter directly (don't import this.. anywhere, really)

import sys

def is_version(check_version):
  actual_version_slice = sys.version_info[:len(check_version)]
  return actual_version_slice == check_version

if (is_version((3,6))):
  print("yay")
  sys.exit(0)

print("not version 3.6")
sys.exit(1)
