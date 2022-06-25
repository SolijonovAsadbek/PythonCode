import random

import pygal

# 1-misol Bar diagramma hosil qilish usuli.

# bar = pygal.Bar()
# bar.add('Telegram', [1.8, 2, 3.1, 4.2, 5, 6, 7.3, 2.4])
# bar.add('Instagram', [2, 2.5, 3.6, 3, 3.5, 1])
# bar.add('Facebook', [1.5, 4.2, 3.1, 3.8, 1.3, 1.9])
# bar.add('Tik Tok', [2.3, 4, 3, 3, 1, 2.6])
# bar.add('Linkedin', [2.1, 4.2, 3.1, 3, 1.3, 1.9])
# bar.add('Youtube', [])
# bar.render_in_browser()


# 2 - misol StackedBar diagramma hosil qilish.
# stackbar = pygal.StackedBar()
# stackbar.add('Python', list(range(1, 20, 3)))
# stackbar.add('Golang', [1, 34, 29, 12, 20])
# stackbar.render_in_browser()


# 3 - misol Nodata.
# First import pygal
# # Then create a bar graph object
# bar_chart = pygal.Bar()
# # Then create a bar graph
# bar_chart1 = pygal.StackedBar()
# # adding random values
# bar_chart1.add('Series A', [0, 50, 1, 2, 3, 5, 8, 3, 1, 44, 5])
# bar_chart1.add('Series B', [1, 4, 1, 5, 2, 7, 4, 5, 7, 9, 8])
# # this will render the svgs in browser
# # save the svgs
# bar_chart.render_in_browser()


# box_plot = pygal.Box(box_mode="tukey")
# box_plot.title = 'V8 benchmark results'
# box_plot.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
# box_plot.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
# box_plot.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
# box_plot.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
# box_plot.render_in_browser()

# pygal.Pie()(1, 3, 3, 7)(1, 6, 6, 4).render_in_browser()

line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file('my_line.svg')
