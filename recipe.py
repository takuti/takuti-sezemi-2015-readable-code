# coding: utf-8

import sys

def main():
  argc = len(sys.argv)
  if argc != 2:
    sys.exit('Error: `$ python recipe.py ${recipe-filename}`')

  recipe_filename = sys.argv[1]

  # read/print all recipes from recipe-data-file
  try:
    recipe_file = open(recipe_filename, 'r')
    # cut the tail '\n', and create recipe list
    recipes = map(lambda recipe: recipe.rstrip(), recipe_file.readlines())
    recipe_id=1
    for recipe in recipes:
      print str(recipe_id)+': '+recipe
      recipe_id+=1
    recipe_file.close()
  except IOError:
    print 'IOError: file `%s` does not exist' % recipe_filename


if __name__ == '__main__':
  main()
