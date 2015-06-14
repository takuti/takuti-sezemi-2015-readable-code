# coding: utf-8

import sys

def main():
  argc = len(sys.argv)
  if argc < 2 or argc > 3:
    sys.exit('Error: `$ python recipe.py ${recipe-filename} ${recipe_id (optional)}`')

  recipe_filename = sys.argv[1]

  # read/print all recipes from recipe-data-file
  try:
    recipe_file = open(recipe_filename, 'r')
    # cut the tail '\n', and create recipe list
    recipes = map(lambda recipe: recipe.rstrip(), recipe_file.readlines())
    recipe_file.close()
  except IOError:
    print 'IOError: file `%s` does not exist' % recipe_filename

  # print recipe(s) based on the given argument: all recipes or one selected recipe
  recipe_ids = range(1, len(recipes)+1) if argc == 2 else [int(sys.argv[2])]
  for recipe_id in recipe_ids:
    print '%d: %s' % (recipe_id, recipes[recipe_id-1])

if __name__ == '__main__':
  main()
