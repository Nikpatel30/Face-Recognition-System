from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from classifier import training

def train_model():
    datadir = './pre_img'
    modeldir = './model/20170511-185253.pb'
    classifier_filename = './class/classifier.pkl'
#    print ("Training Start")
    obj=training(datadir,modeldir,classifier_filename)
    get_file=obj.main_train()
#    print('Saved classifier model to file "%s"' % get_file)
#    print('All Done')
    return 0
