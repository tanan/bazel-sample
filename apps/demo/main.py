import platform
import numpy as np

def version():
  print(f"python version: {platform.python_version()}")

def demo():
  a = np.array([1,2,3])
  b = 2
  c = a * b
  print(f"numpy demo: {c}")

if __name__ == '__main__':
  version()
  demo()
  print("Hello, World!!")
