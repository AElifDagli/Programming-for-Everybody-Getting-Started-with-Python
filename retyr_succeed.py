# Question 5
# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.
# Currently the code will keep executing the function even if it succeeds.
# Fill in the blank so the code stops trying after the operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")


print(retry(operation, 3))
print(retry(stop_service, 5))

# "If operation()" here acts as a boolean.
# It is the same as if it was written if operation() = true or runs/returns any value for a fact.
# Also note that, a function is passed as a parameter to operation. Depends on which function is called/passed.
# It can be the create_user or stop_service function where neither has a parameter value -- (empty)