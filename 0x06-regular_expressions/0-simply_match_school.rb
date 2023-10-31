#!/usr/bin/env ruby
# Check if the argument matches the regular expression /School/

if ARGV[0] =~ /School/
  # If there is a match, print the matched string
  puts ARGV[0].scan(/School/).join
else
  # If there is no match, print an empty line
  puts ""
end

