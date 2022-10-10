def count_users(sales):
  count = 0
  for member in get_members(sales):
    count += 1
    if is_group(member):
      count += count_users(group) -1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18