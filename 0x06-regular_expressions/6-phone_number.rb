#!/usr/bin/env ruby
# Accepts one command-line argument and checks if it matches the regular expression pattern for a 10-digit phone number.
# The pattern matches a sequence of exactly 10 digits (0-9).
# Prints the matched string if found.

puts ARGV[0].scan(/^\d{10}$/).join
