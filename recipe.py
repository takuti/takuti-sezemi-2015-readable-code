# coding: utf-8

import sys

def main():
  argc = len(sys.argv)
  if argc < 2 or argc >3:
    sys.exit('Error: `$ python recipe.py ${recipe-filename} ${recipe_id (optional)}`')

  recipe_filename = sys.argv[1]
  if argc ==3:
    get_recipe_id = sys.argv[2]

  # read/print all recipes from recipe-data-file
  try:
    recipe_file = open(recipe_filename, 'r')
    # cut the tail '\n', and create recipe list
    recipes = map(lambda recipe: recipe.rstrip(), recipe_file.readlines())
    recipe_file.close()
  except IOError:
    print 'IOError: file `%s` does not exist' % recipe_filename

  recipe_id=1
  for recipe in recipes:
    if argc == 3:
      if int(get_recipe_id) == recipe_id:
        print str(recipe_id)+': '+recipe
    else:
      print str(recipe_id)+': '+recipe
    recipe_id+=1

if __name__ == '__main__':
  main()
