import cPickle, gzip, numpy
import theano
import theano.tensor

f = gzip.open('data/mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()