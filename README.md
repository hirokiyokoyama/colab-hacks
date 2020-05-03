# colab-hacks

1. See colab_hacks.ipynb
1. Choose cells that you want to use and find their titles.
1. Run some lines like the following to import the cells into your notebook.

```
import requests; exec(requests.get('https://raw.githubusercontent.com/hirokiyokoyama/colab-hacks/master/run_external_cell.py').text)
run_external_cell('Slack extensions')
run_external_cell('Javascript extensions')
```
