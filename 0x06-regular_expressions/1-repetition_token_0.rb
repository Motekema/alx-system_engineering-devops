#!/usr/bin/env ruby
# Check if the argument matches the regular expression
if ARGV[0] =~ /hbt{2,5}n/
  # If there is a match, print the matched string
  puts ARGV[0]
end
