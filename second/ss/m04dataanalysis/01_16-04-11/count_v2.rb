#!/usr/bin/env ruby
count = 0
ARGF.each_line do |line|
	count += 1
end
puts count
