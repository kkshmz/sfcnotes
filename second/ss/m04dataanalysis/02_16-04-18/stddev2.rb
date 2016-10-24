#!/usr/bin/env ruby

# regular expression to read minutes and count
re = /^(\d+)\s+(\d+)/

sum = 0		# sum of data
n = 0		# the number of data
sqsum = 0	# sum of squares
ARGF.each_line do |line|
    if re.match(line)
      min = $1.to_i
      cnt = $2.to_i
      sum += min * cnt
      n += cnt
      sqsum += min**2 * cnt
    end
end

mean = Float(sum) / n
var = Float(sqsum) / n - mean**2
stddev = Math.sqrt(var)

printf "n:%d mean:%.1f variance:%.1f stddev:%.1f\n", n, mean, var, stddev
