#!/usr/bin/env ruby

# regular expression to read data
re = /^(\d+(\.\d+)?)/

z95 = 1.960	# z_{1-0.05/2}
z90 = 1.645	# z_{1-0.10/2}

sum = 0.0	# sum of data
n = 0		# the number of data
sqsum = 0.0	# su of squares
ARGF.each_line do |line|
    if re.match(line)
      v = $1.to_f
      sum += v
      sqsum += v**2
      n += 1
    end
end

mean = sum / n			# mean
var = sqsum / n - mean**2	# variance
stddev = Math.sqrt(var)		# standard deviation
se = stddev / Math.sqrt(n)	# standard error
ival95 = z95 * se		# intarval/2 for 95% confidence level
ival90 = z90 * se		# intarval/2 for 90% confidence level

# print n mean stddev ival95 ival90
printf "%d %.2f %.2f %.2f %.2f\n", n, mean, stddev, ival95, ival90
