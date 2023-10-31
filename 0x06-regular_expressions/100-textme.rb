#!/usr/bin/env ruby

# Accepts a log entry as a command-line argument and extracts sender, receiver, and flags.
# Outputs the sender, receiver, and flags.

log_entry = ARGV[0]

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Match the regular expression to the log entry
match = log_entry.match(regex)

if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
end

