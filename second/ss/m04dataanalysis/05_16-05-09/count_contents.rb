#!/usr/bin/env ruby

# output: URL req_count byte_count

# regular expression for apache combined log format
#   host ident user time request status bytes referer agent
re = /^(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"/
# regular expression for request
#   method url proto
req_re = /(\w+) (\S+) (\S+)/

contents = Hash.new([0, 0])

count = parsed = 0
ARGF.each_line do |line|
  count += 1
  if re.match(line)
    # match
    host, ident, user, time, request, status, bytes, referer, agent = $~.captures

    # ignore if the status is not success (2xx)
    next unless /2\d{2}/.match(status)

    if req_re.match(request)
      method, url, proto = $~.captures

      # ignore if the method is not GET
      next unless /GET/.match(method)

      parsed += 1

      # count contents by request and bytes
      contents[url] = [contents[url][0] + 1, contents[url][1] + bytes.to_i]
    else
      # match failed.  print a warning msg
      $stderr.puts("request match failed at line #{count}: #{line.dump}")
    end
  else
    # match failed.
    $stderr.puts("match failed at line #{count}: #{line.dump}")
  end
end

contents.sort_by{|key, value| -value[0]}.each do |key, value|
  puts "#{key} #{value[0]} #{value[1]}"
end

$stderr.puts "# #{contents.size} unique contents in #{parsed} successful GET requests"
$stderr.puts "# parsed:#{parsed} ignored:#{count - parsed}"
