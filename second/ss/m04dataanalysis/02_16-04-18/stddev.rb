#!/usr/bin/env ruby

# regular expression to read minutes and count
re = /^(\d+)\s+(\d+)/

data = Array.new

sum = 0		# sum of data
n = 0		# the number of data
ARGF.each_line do |line|
    if re.match(line)
      min = $1.to_i
      cnt = $2.to_i
      sum += min * cnt
      n += cnt
      for i in 1 .. cnt
        data.push min
      end
    end
end

mean = Float(sum) / n

sqsum = 0.0
data.each do |i|
  sqsum += (i - mean)**2
end
var = sqsum / n
stddev = Math.sqrt(var)

printf "n:%d mean:%.1f variance:%.1f stddev:%.1f\n", n, mean, var, stddev
