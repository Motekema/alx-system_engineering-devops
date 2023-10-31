#!/usr/bin/env ruby
# Check if the argument matches the regular expression /School/
puts ARGV[0].scan(/School/).join
