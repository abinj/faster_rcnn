import pandas as pd

train = pd.read_csv('/home/abin/my_works/github_works/faster_rcnn/train.csv')

data = pd.DataFrame()
data['format'] = train['image_names']

for i in range(data.shape[0]):
    data['format'][i] = '/home/abin/my_works/github_works/faster_rcnn/datasets/image_sets/train/' + data['format'][i]

for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + \
                        str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['cell_type'][i]

data.to_csv('annotate.txt', header=None, index=None, sep=' ')
