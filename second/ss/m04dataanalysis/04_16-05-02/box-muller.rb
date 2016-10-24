#!/usr/bin/env ruby
#
# usage: box-muller.rb [n [m [s]]]
#

n = 1		# number of samples to output
mean = 0.0
stddev = 1.0

n = ARGV[0].to_i if ARGV.length >= 1
mean = ARGV[1].to_f if ARGV.length >= 2
stddev = ARGV[2].to_f if ARGV.length >= 3

# function box_muller implements the polar form of the box muller method,
# and returns 2 pseudo random numbers from standard normal distribution
def box_muller
  begin
    u1 = 2.0 * rand - 1.0  # uniformly distributed random numbers
    u2 = 2.0 * rand - 1.0  # ditto
    s = u1*u1 + u2*u2	   # variance
  end while s == 0.0 || s >= 1.0

  w = Math.sqrt(-2.0 * Math.log(s) / s)	# weight
  g1 = u1 * w  # normally distributed random number
  g2 = u2 * w  # ditto
  return g1, g2
end

# box_muller returns 2 random numbers.  so, use them for odd/even rounds
x = x2 = nil
n.times do
  if x2 == nil
    x, x2 = box_muller
  else
    x = x2
    x2 = nil
  end

  x = mean + x * stddev  # scale with mean and stddev

  printf "%.6f\n", x
end
