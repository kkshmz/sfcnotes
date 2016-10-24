#!/usr/bin/env ruby

# regular expression to read minutes and count
re = /^(\d+)\s+(\d+)/

cum = 0
ARGF.each_line do |line|
  begin
    if re.match(line)
      # matched
      time, cnt = $~.captures
      cum += cnt.to_i
      puts "#{time}\t#{cnt}\t#{cum}"
    end
  end
end
