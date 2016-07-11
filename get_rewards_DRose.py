import csv
import codecs
import matplotlib.pyplot as plt

f=codecs.open("model_output.csv","rb","utf-16")
csvread=csv.reader(f,delimiter='\n')
csvread.next()
lines_list = []
passes = 0
fails = 0
rewards = []
errors = []

for line in csvread:
	lines_list.append(line)

lines_iter = iter(lines_list)

for line in lines_iter:
    if line == ['Environment.act(): Primary agent has reached destination!']:
	    passes += 1
    elif line == ['Environment.step(): Primary agent ran out of time! Trial aborted.']:
	    fails += 1
    elif line == ['Reward is']:
	    rewards += lines_iter.next()

rewards = map(float, rewards)

for reward in rewards:
    if reward < 0:
	    errors.append(reward)
		
errors = map(float, errors)

print errors

plt.plot(errors)
plt.ylabel('Negative Rewards')
plt.show()

		
print "Your cab made %d succesful trips, and %d late. It also had a total error amount of %d" % (passes, fails, sum(errors))