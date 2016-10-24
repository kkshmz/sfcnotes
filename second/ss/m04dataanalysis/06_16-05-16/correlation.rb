#!/usr/bin/env ruby

# regular expression for matching 2 floating numbers
re = /([-+]?\d+(?:\.\d+)?)\s+([-+]?\d+(?:\.\d+)?)/

sum_x = 0.0	# sum of x
sum_y = 0.0	# sum of y
sum_xx = 0.0	# sum of x^2
sum_yy = 0.0	# sum of y^2
sum_xy = 0.0	# sum of xy
cc = 0.0	# correlation coefficient
n = 0		# the number of data

ARGF.each_line do |line|
    if re.match(line)
      x = $1.to_f
      y = $2.to_f
      sum_x += x
      sum_y += y
      sum_xx += x**2
      sum_yy += y**2
      sum_xy += x * y
      n += 1
    end
end

denom = (sum_xx - sum_x**2 / n) * (sum_yy - sum_y**2 / n)
if denom != 0.0
  cc = (sum_xy - sum_x * sum_y / n) / Math.sqrt(denom)
end
printf "n:%d cc:%.3f\n", n, cc

