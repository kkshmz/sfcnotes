#!/usr/bin/env ruby

# regular expression to read data
#	'name': 'title0': score0, 'title1': score1, ...
re = /'(.+?)':\s+(\S.*)/

name2uid = Hash.new	# keeps track of name to uid mapping
title2tid = Hash.new	# keeps track of title to tid mapping
scores = Hash.new	# scores[uid][tid]: score of title_id by user_id

# read data into scores[uid][tid]
ARGF.each_line do |line|
  next if line[0] == '#'  # skip comments
  if re.match(line)
    name = $1
    ratings = $2.split(",")

    if name2uid.has_key?(name)
      uid = name2uid[name]
    else
      uid = name2uid.length
      name2uid[name] = uid
      scores[uid] = {}	# create empty hash for title and score pairs
    end

    ratings.each do |rating|
      if rating.match(/'(.+?)':\s*(\d\.\d)/)
        title = $1
        score = $2.to_f
        if title2tid.has_key?(title)
          tid = title2tid[title]
        else
          tid = title2tid.length
          title2tid[title] = tid
        end
        scores[uid][tid] = score
      end
    end
  end
end

# compute cosine similarity between 2 users
def comp_similarity(h1, h2)
  sum_xx = 0.0	# sum of x^2
  sum_yy = 0.0	# sum of y^2
  sum_xy = 0.0	# sum of xy
  score = 0.0	# similarity score

  h1.each do |tid, score|
    sum_xx += score**2
    if h2.has_key?(tid)
      sum_xy += score * h2[tid]
    end
  end
  h2.each_value do |score|
    sum_yy += score**2
  end

  denom = Math.sqrt(sum_xx) * Math.sqrt(sum_yy)
  if denom != 0.0
    score = sum_xy / denom
  end
  return score
end

# create n x n matrix of similarities between users
n = name2uid.length
similarities = Array.new(n) { Array.new(n) }
for i in 0 .. n - 1
  printf "%-18s", name2uid.key(i) + ':'
  for j in 0 .. n - 1
    similarities[i][j] = comp_similarity(scores[i], scores[j])
    printf "%.3f ", similarities[i][j]
  end
  print "\n"
end


