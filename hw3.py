import random 
import time 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

def strandsort(array):
  count = len(array)
	sortedlist = []
	while len(array)>0:
		highest = -1
		sublist = []
		i = 0
		while i < len(array):
			if array[i] >= highest:
				highest = array.pop(i)
				sublist.append(highest)
			else: 
				i += 1
		sortedlist.append(sublist)
	
	finallist = []
	while len(finallist) < count:
		lowest = 0
		for j in range(0, len(sortedlist)):
			if sortedlist[j][0] < sortedlist[lowest][0]:
				lowest = j
		finallist.append(sortedlist[lowest].pop(0))
		if len(sortedlist[lowest]) == 0:
			del sortedlist[lowest]
	return finallist

def heapsort(array):
	count = len(array)
	first = 0
	last = count - 1
	makeheap(array, first, last)
	for i in range(last, first, -1):
		array[i], array[first] = array[first], array[i]
		siftdown(array, first, i-1)
	return array

def makeheap(array, first, last):
	i = last / 2
	while i >= first:
		siftdown(array, i, last)
		i -= 1

def siftdown(array, first, last):
	while 2 * first + 1 <= last:
		k = 2 * first + 1
		if k < last and array[k] < array[k+1]:
			k += 1
		if array[first] >= array[k]:
			break
		array[first], array[k] = array[k], array[first]
		first = k

def getRunningTime(func, maxN, repetitions):
	times = []
	for n in range(1, maxN):
		start = time.clock()
		array = [0] * n
		for i in range(0,n):
			array[i] = random.randint(1,n)
		for rep in range(repetitions):
			func(array)
		end = time.clock()
		avg = (end-start)/float(repetitions)
		times.append(avg)
	return times 

def plotRunningTime(times1, times2, name="plot"): 
	x = range(len(times1))
	plot1, = pyplot.plot(x, times1, 'o')
	plot2, = pyplot.plot(x, times2, 'g^')
	pyplot.xlabel('Size of Set (n)')
	pyplot.ylabel('Time (seconds)')
	pyplot.title('Comparison of Sorting Algorithms')
	pyplot.legend([plot1, plot2], ["strandsort", "heapsort"], loc=2)
	pyplot.savefig(name + "%d.png" % len(times1))

print heapsort([32,4,6,8,4,6,43,6,7,8,4,45])
print strandsort([32,4,6,8,4,6,43,6,7,8,4,45])
run_heap_sort = getRunningTime(heapsort, 100, 100)
run_strand_sort = getRunningTime(strandsort, 100, 100)
plotRunningTime(run_strand_sort, run_heap_sort, "strandsort_and_heapsort")
