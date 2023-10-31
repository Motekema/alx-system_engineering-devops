#!/usr/bin/env ruby

# Accepts one command-line argument and extracts and prints only the capital letters.
# Removes any non-capital letters from the argument.

if ARGV[0]
  capital_letters = ARGV[0].scan(/[A-Z]/).join
  puts capital_letters
end

