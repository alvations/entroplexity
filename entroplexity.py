import graphlab
import numpy


from sklearn.linear_model import BayesianRidge


def polynomial_sframe(feature, degree):
    # assume that degree >= 1
    # initialize the SFrame:
    poly_sframe = graphlab.SFrame()
    # and set poly_sframe['power_1'] equal to the passed feature
    poly_sframe['power_1'] = feature
    # first check if degree > 1
    if degree > 1:
        # then loop over the remaining degrees:
        # range usually starts at 0 and stops at the endpoint-1. We want it to start at 2 and stop at degree
        for power in range(2, degree+1): 
            # first we'll give the column a name:
            name = 'power_' + str(power)
            # then assign poly_sframe[name] to the appropriate power of feature
            poly_sframe[name] = poly_sframe['power_1'].apply(lambda x: x**power)
    return poly_sframe


train =graphlab.SFrame()
se = graphlab.SFrame.read_csv('sense-entropy.train', delimiter=' ', column_type_hints=[str, float])
sp = graphlab.SFrame.read_csv('sent-perplexity.train', column_type_hints=[float])
labels = graphlab.SFrame.read_csv('labels.train', column_type_hints=[bool])

train.add_columns(se)
train.add_columns(sp)
train.add_columns(labels)

test = graphlab.SFrame()
testse = graphlab.SFrame.read_csv('sense-entropy.test', delimiter=' ', column_type_hints=[str, float])
testsp = graphlab.SFrame.read_csv('sent-perplexity.test', column_type_hints=[float])

test.add_columns(testse)
test.add_columns(testsp)

#print len(train), len(test), len(testse), len(testsp)

m = graphlab.boosted_trees_classifier.create(train, target='out', features=['se', 'sp'], validation_set=None) 
for i in m.predict(test):
    print i



'''
# Scikit-learn
X = train['se', 'sp'].to_numpy()
Y = labels['out'].to_numpy()
x_test = test['se', 'sp'].to_numpy()
clf = BayesianRidge(compute_score=True)
clf.fit(X, Y)
for out in clf.predict(x_test):
    print out
'''
