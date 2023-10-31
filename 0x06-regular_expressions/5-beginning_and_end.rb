#!/usr/bin/env ruby
# Accepts one command-line argument and checks if it matches the regular expression pattern.
# The pattern matches a string that starts with "h," ends with "n," and can have any single character in between.
# Prints the matched string if found.

puts ARGV[0].scan(/^h.n$/).join
