def fibonacci_sequence(n):
  if n <= 0:
    return[]
  elif n == 1:
    return [0]
  else:
    sequence= [0, 1]
    while len(sequence) < n:
      sequence.append(sequence[-1] + sequence[-2])
    return sequence
    
