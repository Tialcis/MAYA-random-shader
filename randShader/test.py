import numpy as np
import matplotlib.pyplot as plt
import random

shader_counter = [0, 0, 0, 0, 0, 0, 0]

def distribute_shader(rand_number):
    if (0 < rand_number <= 475):
        shader_counter[0]+=1
    elif (475 < rand_number <= 1595):
        shader_counter[1]+=1
    elif (1595 < rand_number <= 3710):
        shader_counter[2]+=1
    elif (3710 < rand_number <= 6290):
        shader_counter[3]+=1
    elif (6290 < rand_number <= 8405):
        shader_counter[4]+=1
    elif (8405 < rand_number <= 9525):
        shader_counter[5]+=1
    elif (9525 < rand_number <= 10000):
        shader_counter[6]+=1

for i in xrange(0, 10000):
    rand_number = random.randint(0, 10001)
    # cmds.select(obj)
    shader_name = distribute_shader(rand_number)
    # self._assign_selection_to_shader(shader_name)
    print shader_name
# cmds.select(clear=True)
print shader_counter

ind = np.arange(len(shader_counter))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, shader_counter, width,
                color='SkyBlue', label='Men')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Normals')
ax.set_xticks(ind)
ax.set_xticklabels(('R', 'O', 'Y', 'G', 'B', 'I', 'V'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    # for rect in rects:
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
    #             '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")

plt.show()
