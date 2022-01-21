

// contains 5
// divisible by 5
// contains 7
// divisible by 7

// BootsAndCats tests
bootsAndCats(57) // contains both
bootsAndCats(35) // divisible by both


// Cats tests
bootsAndCats(65) // contains
bootsAndCats(60) // divisible


// Boots tests
bootsAndCats(67) // contains
bootsAndCats(63) // divisible

// no match tests
bootsAndCats(4) // none


function bootsAndCats(num) {
  const numAsStr = `${num}`
  if (helperDivisible(num, [5, 7]) || helperContains(numAsStr, ['5', '7'])) {
    console.log('BootsAndCats')
    return
  }
  if (helperDivisible(num, [5]) || helperContains(numAsStr, ['5'])) {
    console.log('Cats')
    return
  }
  if (helperDivisible(num, [7]) || helperContains(numAsStr, ['7'])) {
    console.log('Boots')
    return
  }

  console.log(num)
}

function helperDivisible(num, targetNums) {
  for (const targetNum of targetNums) {
    if (num % targetNum !== 0) return false
  }
  return true
}

function helperContains(numStr, targetNumStrs) {
  for (const targetNumStr of targetNumStrs) {
    if (!numStr.includes(targetNumStr)) return false
  }
  return true
}


function generateTestSet() {
  const generateCombinations = (length) => {
    if (length === 1) return [[true], [false]]
    const suffixes = generateCombinations(length - 1)
    const result = []
    for (const suffix of suffixes) {
      result.push([true, ...suffix])
      result.push([false, ...suffix])
    }
    return result
  }

  const combinations = generateCombinations(4)

  let combinationsMatched = 0
  let candidate = 1
  const numSet = []
  while (combinationsMatched < combinations.length) {
    for (var i = 0; i < combinations.length; i++) {
      const combination = combinations[i]
      if (!combination || !checkCombination(candidate, combination)) continue
      combinations[i] = null
      combinationsMatched++
      numSet.push(candidate)
      break
    }
    candidate++
  }
  return numSet
}

const contains = (searchNum) => (num) => `${num}`.includes(`${searchNum}`)
const divisibleBy = (divisor) => (num) => num % divisor === 0
const conditions = [contains(5), contains(7), divisibleBy(5), divisibleBy(7)]

function checkCombination(candidate, combination) {
  for (var i = 0; i < conditions.length; i++) {
    if (combination[i] !== conditions[i](candidate)) return false
  }

  return true
}

console.log(generateTestSet())
