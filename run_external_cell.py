def run_external_cell(title):
  import requests
  url = 'https://raw.githubusercontent.com/hirokiyokoyama/colab-hacks/master/colab_hacks.ipynb'
  nb = requests.get(url).json()

  def is_exported(cell):
    if cell['cell_type'] != 'code':
      return False
    source = cell['source']
    if len(source) < 2:
      return False
    return source[0].startswith('#@title ') and source[1].startswith('#export')

  def key_value(cell):
    source = cell['source']
    key = source[0].split(' ', maxsplit=1)[1].strip()
    value = ''.join(source[2:])
    return key, value

  cells = {key: value for key, value in map(key_value, filter(is_exported, nb['cells']))}
  if title not in cells:
    raise ValueError('Usage: _run_external_cell(title)\ntitle: {}'.format(str(list(cells.keys()))))
  get_ipython().run_cell(cells[title])
