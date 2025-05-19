#!/usr/bin/env ruby
# This script accepts one argument and matches the word "School" (case-sensitive)

if ARGV.length != 1
  puts "Usage: #{__FILE__} <string>"
  exit 1
end

input = ARGV[0]
matches = input.scan(/School/)

puts matches.join
