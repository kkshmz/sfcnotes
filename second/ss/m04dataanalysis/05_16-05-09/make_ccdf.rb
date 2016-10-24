#!/usr/bin/env ruby

re = /^[A-Z]+,\d+,(\d+),\d+/	# for US surnames
#re = /^\S+\s+(\d+)\s+\d+/	# for JAIST web server logs

n = 0
counts = Hash.new(0)
ARGF.each_line do |line|
  if re.match(line)
    counts[$1.to_i] += 1
    n += 1
  end
end

cum = 0
counts.sort.each do |key, value|
  comp = 1.0 - Float(cum) / n
  puts "#{key} #{value} #{comp}"
  cum += value
end

$stderr.puts "# #{n} entries matched"


