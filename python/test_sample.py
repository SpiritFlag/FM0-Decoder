def test_sample_LH(test, answer):
  try:
    count = 0
    for idx in range(len(test)):
      if (test[idx] < 0.5 and answer[idx] == 0) or (test[idx] >= 0.5 and answer[idx] == 1):
        count += 1
    return count

  except Exception as ex:
    print("[test_sample_LH.py]", end=" ")
    print(ex)
