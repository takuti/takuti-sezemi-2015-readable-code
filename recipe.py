# coding: utf-8

import sys

def main():
  argc = len(sys.argv)
  if argc != 2:
    sys.exit('Error: `$ python recipe.py ${recipe-filename}`')

  recipe_filename = sys.argv[1]

  # read/print all recipes from recipe-data-file
  try:
    f = open(recipe_filename, 'r')
    # cut the tail '\n', and create recipe list
    recipes = map(lambda recipe: recipe.rstrip(), f.readlines())
    for r in recipes:
      print r
  except IOError:
    print 'IOError: file `%s` does not exist' % recipe_filename


if __name__ == '__main__':
  main()
